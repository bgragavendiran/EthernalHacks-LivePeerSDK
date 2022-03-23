#!/bin/bash
set -euo pipefail
trap 'echo && echo "ERROR: $BASH_SOURCE:$LINENO $BASH_COMMAND" >&2' ERR

# Args and env

FILENAME="${1:?"Usage: $0 {filename}"}"
FILE_BASENAME=${FILENAME##*/}
ASSET_NAME="${2:-${ASSET_NAME:-${FILE_BASENAME%".mp4"}}}"
NFT_METADATA="${3:-${NFT_METADATA:-"{}"}}"

if test -f "$NFT_METADATA"; then
  NFT_METADATA=$(cat $NFT_METADATA)
fi
if [[ "$NFT_METADATA" != "{}" ]] ; then
  echo "Using metadata for NFT:"
  echo "$NFT_METADATA" | jq
fi

HOST="${HOST:-"livepeer.com"}"
LP_API_TOKEN="799ec2b2-9108-434d-91ac-abec0b9b0f09"

# API Functions

function getAsset() {
  curl -s \
    -H "authorization: Bearer $LP_API_TOKEN" \
    $HOST/api/asset/$1
}

function getTask() {
  curl -s \
    -H "authorization: Bearer $LP_API_TOKEN" \
    $HOST/api/task/$1
}

function requestUploadUrl() {
  curl -s \
    -X POST \
    -H "authorization: Bearer $LP_API_TOKEN" \
    -H "content-type: application/json" \
    --data-raw "{\"name\": \"$1\"}" \
    $HOST/api/asset/request-upload
}

function uploadFile() {
  curl -s \
    -H "authorization: Bearer $LP_API_TOKEN" \
    -X PUT \
    --header 'Content-Type: video/mp4'  \
    --data-binary "@$1" \
    $2
}

function exportAsset() {
  curl -s \
    -X POST \
    -H "authorization: Bearer $LP_API_TOKEN" \
    -H "content-type: application/json" \
    --data-raw "{\"ipfs\": {\"nftMetadata\":$NFT_METADATA}}" \
    $HOST/api/asset/$1/export
}

# Uploading the file

echo -n "1. Requesting upload URL... "

uploadJson=$(requestUploadUrl "$ASSET_NAME")
uploadUrl="$(echo $uploadJson | jq -re '.url')"
asset="$(echo $uploadJson | jq -re '.asset')"
assetId="$(echo $uploadJson | jq -re '.asset.id')"

echo "Pending asset with ID $assetId!"

echo "2. Uploading file..."
uploadFile "$FILENAME" "$uploadUrl"

echo -n "Waiting for asset to be ready..."
while [[ "$(echo "$asset" | jq -re '.status')" == "waiting" ]]; do
  sleep 1
  echo -n "."
  asset=$(getAsset $assetId)
done
echo

if [[ "$(echo $asset | jq -re '.status')" != "ready" ]]; then
  echo "Asset upload failed. Asset:"
  echo "$asset" | jq
  exit 1
fi

# Exporting the file to IPFS

echo -n "3. Starting export... "

task=$(exportAsset $assetId | jq -cre '.task')
taskId=$(echo $task | jq -cre '.id')

echo "Created export task with ID $taskId!"

echo "Waiting for export task completion..."
lastProgress="0"
while ! [[ $(echo $task | jq -re '.status.phase') =~ ^(completed|failed)$ ]]; do
  progress=$(echo $task | jq -r '.status.progress')
  if [[ "$progress" != "null" ]] && [[ "$progress" != "$lastProgress" ]]; then
    echo " - Export progress: ${progress}"
    lastProgress="$progress"
  fi
  sleep 1
  task=$(getTask $taskId)
done

if [[ $(echo $task | jq -re '.status.phase') != "completed" ]]; then
  echo "Export task failed. Status:"
  echo "$task" | jq '.status'
  exit 1
fi

echo "4. Export successful! Result:"
echo $task | jq '.output.export.ipfs'