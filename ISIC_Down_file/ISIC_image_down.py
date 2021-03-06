import urllib
import os
from isic_api import ISICApi

# Initialize the API; no login is necessary for public data

## userid = input('id :')
## pswd = getpass.getpass('Password:')

api = ISICApi()
savePath = 'ISICArchive/'

if not os.path.exists(savePath):
    os.makedirs(savePath)

loop_count = 300
loop_onece_count = 100
all_count = 0
for get_num in range (0,loop_count):
    offset_num = get_num * loop_onece_count
    imageList = api.getJson('image?limit='+str(loop_onece_count)+'&offset='+str(offset_num)+'&sort=name')
    print('Downloading %s images' % len(imageList))
    print("offset is ", offset_num)
    imageDetails = []
    for image in imageList:
        print("image id : ",image['_id'],"image name : " ,image['name'])
        imageFileResp = api.get('image/%s/download' % image['_id'])
        imageFileResp.raise_for_status()
        imageFileOutputPath = os.path.join(savePath, '%s.jpg' % image['name'])
        with open(imageFileOutputPath, 'wb') as imageFileOutputStream:
            for chunk in imageFileResp:
                imageFileOutputStream.write(chunk)