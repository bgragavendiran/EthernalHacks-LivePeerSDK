

class LivePeerSDK(builtins.object)
 |  LivePeerSDK(APIKEY)
 |
 |  Methods defined here:
 |
 |  __init__(self, APIKEY)
 |      INITIALIZE LIVEPEER WITH APIKEY FROM LIVEPEER DASHBOARD
 |
 |  createUploadUrl(self, name)
 |      Creates a new Upload URL to directly upload a video Asset to Livepeer
 |
 |      :parameter
 |      "name":"Example name"
 |
 |      :returns
 |      dict
 |      {
 |      url:<URL>,
 |      asset:{'id':<assetid>, 'playbackId':<playbackId>, 'userId':<userId>, 'createdAt':<timestamp>, 'status':<STATUS>, 'name':<name>}
 |      task:{'id':<taskid>, 'createdAt':<timestamp>, 'type':<importType>, 'outputAssetId':<outassetid>, 'userId':<uid>, 'params':{'uploadedObjectKey': <type>}}, 'status':{'phase': <STATUS>, 'updatedAt': <timestamp>}}
 |      }
 |
 |  exportAssetToIPFS(self, assetID)
 |      EXPORT A SPECIFIC ASSET ID TO IPFS IT INITIALIZES A CLOUD ASYNC CALL IN LIVEPEER WHICH CREATES A RESPECTIVE TASK ID
 |      "assetID obtained from createUploadURL(name)"
 |
 |  importWebAsset(self, url, name)
 |      Import a video Asset to Livepeer from an external URL through the POST /api/asset/import API.
 |      :param
 |      "url":"$EXTERNAL_URL",
 |      "name":"Example name"
 |
 |  listAssets(self)
 |      LIST ALL ASSETS CURRENTLY UPLOADED TO LIVEPEER in the form of a DICTIONARY
 |      :param : NONE
 |
 |      :returns
 |      <class 'list'>
 |      LIST OF DICTIONARIES OF FORMAT
 |
 |      FOR UPLOADED VIDEOS
 |      {
 |      id : <ID>,
 |      hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]
 |      name : <name>,
 |      size : <size>,
 |      status : ready,
 |      userId : <userID>,
 |      createdAt : <timestamps>,
 |      updatedAt : <timestamps>,
 |      videoSpec : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
 |      playbackId : <playbackID>,
 |      downloadUrl : <downloadURLfromLIVEPEERCDN>
 |      }
 |
 |      FOR PENDING VIDEOS
 |      {
 |      'id': <ID>,
 |      'name':  <name>,
 |      'status': 'waiting',
 |      'userId': <userID>,
 |      'createdAt': <timestamps>,
 |      'playbackId': <playbackID>,
 |      }
 |      "
 |
 |  listTasks(self)
 |      LIST ALL TASKS CURRENTLY UPLOADED TO LIVEPEER
 |      :param : NONE
 |
 |      :returns
 |      <class 'list'>
 |      LIST OF DICTIONARIES OF FORMAT
 |
 |      FOR EXPORT
 |      {
 |      'id':<id>,
 |      'type':<type>,
 |      'output': {'export': {'ipfs': {'videoFileCid':<videoFileCid>,'nftMetadataCid':<nftMetadataCid>,'videoFileUrl':<videoFileUrl>,'videoFileGatewayUrl':<videoFileGatewayUrl>,'nftMetadataUrl':<nftMetadataUrl>,'nftMetadataGatewayUrl':<nftMetadataGatewayUrl>,'params': {'export': {'ipfs': {<ipfsMetadata>}}},'status': {'phase':<phase>,'updatedAt': <timestamps>},'userId':<userId>,'createdAt': <timestamps>,'inputAssetId':<inputAssetId>}
 |      }
 |
 |      FOR IMPORT
 |      {
 |      'id': <taskID>,
 |      'type': 'import',
 |      'output': {'import': {'assetSpec': {'hash': [hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]],
 |      'name': <name>,
 |      'size': <size>,
 |      'type': 'video',
 |      'videoSpec' : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
 |      }}},
 |      'params': {'import': {'uploadedObjectKey': <uploadKey>}},
 |      'status': {
 |          'phase': <status>,
 |          'userId' : <userID>,
 |          'createdAt': <timestamps>,
 |          'updatedAt' : <timestamps>,
 |          'outputAssetId': <outputassetID>
 |          }
 |      }
 |
 |      "
 |
 |  retrieveAsset(self, assetID)
 |      RETRIEVE A SPECIFIC ASSET ID FROM LIVE PEER
 |      :param
 |      assetID obtained from createUploadURL(name)
 |
 |      :returns
 |      <class 'dict'>
 |      dict of following format
 |      FOR UPLOADED VIDEOS
 |      {
 |      id : <ID>,
 |      hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]
 |      name : <name>,
 |      size : <size>,
 |      status : ready,
 |      userId : <userID>,
 |      createdAt : <timestamps>,
 |      updatedAt : <timestamps>,
 |      videoSpec : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
 |      playbackId : <playbackID>,
 |      downloadUrl : <downloadURLfromLIVEPEERCDN>
 |      }
 |
 |      FOR PENDING VIDEOS
 |      {
 |      'id': <ID>,
 |      'name':  <name>,
 |      'status': 'waiting',
 |      'userId': <userID>,
 |      'createdAt': <timestamps>,
 |      'playbackId': <playbackID>,
 |      }
 |      "
 |
 |  retrieveTask(self, taskID)
 |      RETRIEVE A SPECIFIC TASK ID FROM LIVEPEER with IPFS LINK
 |      :param
 |      "taskID obtained from listTASKS
 |
 |      :returns
 |      <class 'dict'>
 |      Dictionary of Format
 |       FOR EXPORT
 |      {
 |      'id':<id>,
 |      'type':<type>,
 |      'output': {'export': {'ipfs': {'videoFileCid':<videoFileCid>,'nftMetadataCid':<nftMetadataCid>,'videoFileUrl':<videoFileUrl>,'videoFileGatewayUrl':<videoFileGatewayUrl>,'nftMetadataUrl':<nftMetadataUrl>,'nftMetadataGatewayUrl':<nftMetadataGatewayUrl>,'params': {'export': {'ipfs': {<ipfsMetadata>}}},'status': {'phase':<phase>,'updatedAt': <timestamps>},'userId':<userId>,'createdAt': <timestamps>,'inputAssetId':<inputAssetId>}
 |      }
 |
 |      FOR IMPORT
 |      {
 |      'id': <taskID>,
 |      'type': 'import',
 |      'output': {'import': {'assetSpec': {'hash': [hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]],
 |      'name': <name>,
 |      'size': <size>,
 |      'type': 'video',
 |      'videoSpec' : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
 |      }}},
 |      'params': {'import': {'uploadedObjectKey': <uploadKey>}},
 |      'status': {
 |          'phase': <status>,
 |          'userId' : <userID>,
 |          'createdAt': <timestamps>,
 |          'updatedAt' : <timestamps>,
 |          'outputAssetId': <outputassetID>
 |          }
 |      }
 |      "
 |
 |  uploadContent(self, filePATH, assetURL)
 |      Create a new Direct Upload URL  to directly upload a video Asset to Livepeer
 |      :param
 |      "filePATH":"PASS THE FILE PATH OF VIDEO IN H264 and AAC codec
 |      "assetURL":ASSET URL FOR THE FILE"
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)



