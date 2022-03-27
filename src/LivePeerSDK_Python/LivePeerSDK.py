# MIT License
#
# Copyright (c) 2022 RAGAVENDIRAN BALASUBRAMANIAN.
# GMAIL   : bgragavendiran@gmail.com
# LINKEDIN: https://www.linkedin.com/in/ragavendiranbalasubramanian/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#    *)The owner and source contributors names and details  shall not to be removed from the project
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import requests
import json


class LivePeerSDK:
    # ASSET ENDPOINTS
    __IMPORT_ASSET = 'https://livepeer.com/api/asset/import'
    __REQUEST_UPLOAD = 'https://livepeer.com/api/asset/request-upload'
    __LIST_ASSETS = 'https://livepeer.com/api/asset'
    __RETRIEVE_ASSETS = 'https://livepeer.com/api/asset/'  # ENDS WITH $ASSET_ID
    __EXPORT_ASSET = 'https://livepeer.com/api/asset/'  # ENDS WITH $ASSET_ID/export
    # TASK ENDPOINTS
    __RETRIEVE_TASK = 'https://livepeer.com/api/task/'  # ENDS WITH $TASK_ID
    __LIST_TASKS = 'https://livepeer.com/api/task/'

    global __currentAssetURL

    def __init__(self, APIKEY):
        """INITIALIZE LIVEPEER WITH APIKEY FROM LIVEPEER DASHBOARD"""
        self.__currentAssetURL = None
        self.APIKEY = APIKEY

    def createUploadUrl(self, name):
        """
        Creates a new Upload URL to directly upload a video Asset to Livepeer

        :parameter
        "name":"Example name"

        :returns
        dict
        {
        url:<URL>,
        asset:{'id':<assetid>, 'playbackId':<playbackId>, 'userId':<userId>, 'createdAt':<timestamp>, 'status':<STATUS>, 'name':<name>}
        task:{'id':<taskid>, 'createdAt':<timestamp>, 'type':<importType>, 'outputAssetId':<outassetid>, 'userId':<uid>, 'params':{'uploadedObjectKey': <type>}}, 'status':{'phase': <STATUS>, 'updatedAt': <timestamp>}}
        }
        """
        dic = {"name": name}
        data = json.dumps(dic)
        r = requests.post(url=self.__REQUEST_UPLOAD, headers={'Authorization': 'Bearer ' + self.APIKEY,
                                                              'Content-Type': 'application/json'}, data=data)
        result = json.loads(r.text)
        # print(result["url"])
        self.__currentAssetURL = result["url"]
        return result

    def exportAssetToIPFS(self, assetID):
        '''EXPORT A SPECIFIC ASSET ID TO IPFS IT INITIALIZES A CLOUD ASYNC CALL IN LIVEPEER WHICH CREATES A RESPECTIVE TASK ID
        "assetID obtained from createUploadURL(name)
        :param
        "assetID":"$AssetID"

        :returns
        {}
        '''
        dic = {"ipfs": {}}
        data = json.dumps(dic)
        r = requests.post(self.__EXPORT_ASSET + assetID + '/export',
                          headers={'Authorization': 'Bearer ' + self.APIKEY,
                                   'Content-Type': 'application/json'}, data=data)
        return (r.json())

    def importWebAsset(self, url, name):
        """Import a video Asset to Livepeer from an external URL through the POST /api/asset/import API.
        :param
        "url":"$EXTERNAL_URL",
        "name":"Example name\"

        :returns
        {}
        """
        dic = {"name": name, "url": url}
        data = json.dumps(dic)
        r = requests.post(url=self.__REQUEST_UPLOAD,
                          headers={'Authorization': 'Bearer ' + self.APIKEY, 'Content-Type': 'application/json'},
                          data=data)
        result = json.loads(r.text)
        return result

    def listAssets(self):
        """LIST ALL ASSETS CURRENTLY UPLOADED TO LIVEPEER in the form of a DICTIONARY
        :param : NONE

        :returns
        <class 'list'>
        LIST OF DICTIONARIES OF FORMAT

        FOR UPLOADED VIDEOS
        {
        id : <ID>,
        hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]
        name : <name>,
        size : <size>,
        status : ready,
        userId : <userID>,
        createdAt : <timestamps>,
        updatedAt : <timestamps>,
        videoSpec : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
        playbackId : <playbackID>,
        downloadUrl : <downloadURLfromLIVEPEERCDN>
        }

        FOR PENDING VIDEOS
        {
        'id': <ID>,
        'name':  <name>,
        'status': 'waiting',
        'userId': <userID>,
        'createdAt': <timestamps>,
        'playbackId': <playbackID>,
        }
        \""""
        r = requests.get(self.__LIST_ASSETS, headers={'Authorization': 'Bearer ' + self.APIKEY})
        return r.json()

    def listTasks(self):
        """LIST ALL TASKS CURRENTLY UPLOADED TO LIVEPEER
        :param : NONE

        :returns
        <class 'list'>
        LIST OF DICTIONARIES OF FORMAT

        FOR EXPORT
        {
        'id':<taskID>,
        'type':<type>,
        'output': {'export': {'ipfs': {'videoFileCid':<videoFileCid>,'nftMetadataCid':<nftMetadataCid>,'videoFileUrl':<videoFileUrl>,'videoFileGatewayUrl':<videoFileGatewayUrl>,'nftMetadataUrl':<nftMetadataUrl>,'nftMetadataGatewayUrl':<nftMetadataGatewayUrl>,'params': {'export': {'ipfs': {<ipfsMetadata>}}},'status': {'phase':<phase>,'updatedAt': <timestamps>},'userId':<userId>,'createdAt': <timestamps>,'inputAssetId':<inputAssetId>}
        }

        FOR IMPORT
        {
        'id': <taskID>,
        'type': 'import',
        'output': {'import': {'assetSpec': {'hash': [hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]],
        'name': <name>,
        'size': <size>,
        'type': 'video',
        'videoSpec' : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
        }}},
        'params': {'import': {'uploadedObjectKey': <uploadKey>}},
        'status': {
            'phase': <status>,
            'userId' : <userID>,
            'createdAt': <timestamps>,
            'updatedAt' : <timestamps>,
            'outputAssetId': <outputassetID>
            }
        }

        \""""
        r = requests.get(self.__LIST_TASKS,
                         headers={'Authorization': 'Bearer ' + self.APIKEY})
        return (r.json())

    def retrieveAsset(self, assetID):
        """RETRIEVE A SPECIFIC ASSET ID FROM LIVE PEER
        :param
        assetID obtained from createUploadURL(name)

        :returns
        <class 'dict'>
        dict of following format
        FOR UPLOADED VIDEOS
        {
        id : <ID>,
        hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]
        name : <name>,
        size : <size>,
        status : ready,
        userId : <userID>,
        createdAt : <timestamps>,
        updatedAt : <timestamps>,
        videoSpec : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
        playbackId : <playbackID>,
        downloadUrl : <downloadURLfromLIVEPEERCDN>
        }

        FOR PENDING VIDEOS
        {
        'id': <ID>,
        'name':  <name>,
        'status': 'waiting',
        'userId': <userID>,
        'createdAt': <timestamps>,
        'playbackId': <playbackID>,
        }
        \""""
        r = requests.get(self.__RETRIEVE_ASSETS + assetID,
                         headers={'Authorization': 'Bearer ' + self.APIKEY})
        return (r.json())

    def retrieveTask(self, taskID):
        """RETRIEVE A SPECIFIC TASK ID FROM LIVEPEER with IPFS LINK
            :param
            "taskID obtained from listTASKS

            :returns
            <class 'dict'>
            Dictionary of Format
             FOR EXPORT
            {
            'id':<id>,
            'type':<type>,
            'output': {'export': {'ipfs': {'videoFileCid':<videoFileCid>,'nftMetadataCid':<nftMetadataCid>,'videoFileUrl':<videoFileUrl>,'videoFileGatewayUrl':<videoFileGatewayUrl>,'nftMetadataUrl':<nftMetadataUrl>,'nftMetadataGatewayUrl':<nftMetadataGatewayUrl>,'params': {'export': {'ipfs': {<ipfsMetadata>}}},'status': {'phase':<phase>,'updatedAt': <timestamps>},'userId':<userId>,'createdAt': <timestamps>,'inputAssetId':<inputAssetId>}
            }

            FOR IMPORT
            {
            'id': <taskID>,
            'type': 'import',
            'output': {'import': {'assetSpec': {'hash': [hash : [{'hash': <hash>, 'algorithm': 'md5'}, {'hash': <hash>, 'algorithm': 'sha256'}]],
            'name': <name>,
            'size': <size>,
            'type': 'video',
            'videoSpec' : {'format': <format>, 'tracks': [{'fps': <fps>, 'type': 'video', 'codec': 'h264', 'width': <width>, 'height': <height>, 'bitrate': <bitrate>, 'duration': <duration>, 'pixelFormat': 'yuv420p'}, {'type': 'audio', 'codec': 'aac', 'bitrate': <birate>, 'channels': 2, 'duration': <duration>, 'sampleRate': <samplerate>}], 'duration': <duration>}
            }}},
            'params': {'import': {'uploadedObjectKey': <uploadKey>}},
            'status': {
                'phase': <status>,
                'userId' : <userID>,
                'createdAt': <timestamps>,
                'updatedAt' : <timestamps>,
                'outputAssetId': <outputassetID>
                }
            }
            \""""

        r = requests.get(self.__RETRIEVE_TASK + taskID, headers={'Authorization': 'Bearer ' + self.APIKEY})
        return r.json()

    def uploadContent(self, filePATH, assetURL):
        """Create a new Direct Upload URL  to directly upload a video Asset to Livepeer
            :param
            "filePATH":"PASS THE FILE PATH OF VIDEO IN H264 and AAC codec
            "assetURL":ASSET URL FOR THE FILE
            :returns
            {}
        \""""
        self.__currentAssetURL = assetURL
        with open(filePATH, 'rb') as fp:
            r = requests.put(self.__currentAssetURL, headers={'Content-Type': 'video/mp4'}, data=fp)
            return (r.text)


if __name__ == '__main__':
    pass
