from isic_api import ISICApi
import pprint
import getpass
import csv  

# Initialize the API; no login is necessary for public data
## userid = input('id :')
## pswd = getpass.getpass('Password:')

api = ISICApi()



loop_count = 300
loop_onece_count = 100
all_count = 0

div_1_dict_list = ['_id','name','_modelType','created']
div_2_dict_list = ['creator']
div_2_dict_list_2_creator = ['_id','name']

div_3_dict_list = ['meta']
div_3_dict_list_2_meta = ['acquisition','clinical']
div_3_dict_list_3_acquisition = ['image_type','pixelsX','pixelsY']
div_3_dict_list_3_clinical = ['age_approx','anatom_site_general','benign_malignant','diagnosis' \
                                ,'diagnosis_confirm_type','melanocytic','sex']

with open('ISICArchive_Detail.csv', 'w', encoding='utf-8',newline='') as csvfile:
    fieldnames = ['_id', 'name','_modelType',
                    'created',
                    'creator-_id','creator-name',
                    'meta-acquisition-image_type','meta-clinical-age_approx',
                    'meta-acquisition-pixelsX',   'meta-clinical-anatom_site_general',
                    'meta-acquisition-pixelsY',   'meta-clinical-benign_malignant',
                                                  'meta-clinical-diagnosis',
                                                  'meta-clinical-diagnosis_confirm_type',
                                                  'meta-clinical-melanocytic',
                                                  'meta-clinical-sex']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for get_num in range (0,loop_count):
        offset_num = get_num * loop_onece_count
        imageList = api.getJson('image?limit='+str(loop_onece_count)+'&offset='+str(offset_num)+'&sort=name')
        imageDetails = []
        for image in imageList:
            print(' ', image['name'], end='', flush=True)
            # Fetch the full image details
            imageDetail = api.getJson('image/%s' % image['_id'])
            imageDetails.append(imageDetail)
        for imageDetail in imageDetails:
            rowDict = {}
            for div_1_dict in imageDetail:
                if div_1_dict in div_1_dict_list:
                    #print(div_1_dict, ":" ,imageDetail[div_1_dict])
                    rowDict[div_1_dict] = imageDetail[div_1_dict]
                elif div_1_dict in div_2_dict_list:
                    for div_2_dict in imageDetail[div_1_dict] :
                        if div_2_dict in div_2_dict_list_2_creator : 
                            #print(div_1_dict,"-",div_2_dict, ":" , imageDetail[div_1_dict][div_2_dict])
                            rowDict[str(div_1_dict)+"-"+str(div_2_dict)] = imageDetail[div_1_dict][div_2_dict]
                elif div_1_dict in div_3_dict_list:
                    for div_2_dict in imageDetail[div_1_dict] :
                        if div_2_dict in div_3_dict_list_2_meta : 
                            for div_3_dict in imageDetail[div_1_dict][div_2_dict] :
                                if div_3_dict in div_3_dict_list_3_clinical :
                                    #print(div_1_dict," -",div_2_dict,"-",div_3_dict,":",imageDetail[div_1_dict][div_2_dict][div_3_dict])
                                    rowDict[str(div_1_dict)+"-"+str(div_2_dict)+"-"+str(div_3_dict)] = imageDetail[div_1_dict][div_2_dict][div_3_dict] 
                                elif div_3_dict in div_3_dict_list_3_acquisition :
                                    #print(div_1_dict,"-",div_2_dict,"-",div_3_dict,":",imageDetail[div_1_dict][div_2_dict][div_3_dict])
                                    rowDict[ str(div_1_dict)+"-"+str(div_2_dict)+"-"+str(div_3_dict)] = imageDetail[div_1_dict][div_2_dict][div_3_dict]
            all_count += 1
            writer.writerow(rowDict)
        print("")
        print("현재 csv row 수 : ",all_count)
    print("")
    print("전체 csv row 수 : ",all_count)



'''
fields :
 id 
 - ['_id']   :  해당 이미지에 대한 id 
 name 
 - ['name']  :
 modelType
 - ['_modelType'] :
 created 
 - ['created']    : 
 
 creator           
 - ['creator']  - ['_id']  :
                - ['name'] :

 meta         
 - ['meta'] - ['acquisition']  - ['image_type'] :
                               - ['pixelsX']    :
                               - ['pixelsY']    :

 - ['meta'] - ['clinical']    - ['age_approx']
                              - ['anatom_site_general']
                              - ['benign_malignant']
                              - ['diagnosis']
                              - ['diagnosis_confirm_type']
                              - ['melanocytic']
                              - ['sex']


example ) ISIC_0000000
@@ csv 허용
// 추후 기약...;;

{@@'_id': '5436e3abbae478396759f0cf',
 @@'_modelType': 'image',
 @@'created': '2014-10-09T19:36:11.989000+00:00',
 @@'creator': {'_id': '5450e996bae47865794e4d0d', 'name': 'User 6VSN'},
 /////'dataset': {'_accessLevel': 0,
             '_id': '5a2ecc5e1165975c945942a2',
             'description': 'Moles and melanomas.\n'
                            'Biopsy-confirmed melanocytic lesions. Both '
                            'malignant and benign lesions are included.',
             'license': 'CC-0',
             'name': 'UDA-1',
             'updated': '2014-11-10T02:39:56.492000+00:00'},
 'meta': {@@'acquisition': {'image_type': 'dermoscopic',
                          'pixelsX': 1022,
                          'pixelsY': 767},
          @@'clinical': {'age_approx': 55,
                       'anatom_site_general': 'anterior torso',
                       'benign_malignant': 'benign',
                       'diagnosis': 'nevus',
                       'diagnosis_confirm_type': None,
                       'melanocytic': True,
                       'sex': 'female'},
         /////// 'unstructured': {'diagnosis': 'dysplastic nevus',
                           'id1': '1',
                           'localization': 'Abdomen',
                           'site': 'bar'},
          'unstructuredExif': {}},
 @@ 'name': 'ISIC_0000000',
////// 'notes': {'reviewed': {'accepted': True,
                        'time': '2014-11-10T02:39:56.492000+00:00',
                        'userId': '5436c6e7bae4780a676c8f93'},
           'tags': ['ISBI 2016: Training',
                    'ISBI 2017: Training',
                    'Challenge 2018: Task 1-2: Training',
                    'Challenge 2019: Training']},
 //////'updated': '2015-02-23T02:48:17.495000+00:00'}

'''