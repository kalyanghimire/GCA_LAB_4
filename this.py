import boto3
import base64
import json
import os

rekognition_client=boto3.client('rekognition')

for file in ('kalyan.jpg','srk.jpg','women.jpg'):
    print('')
    print(file)
    file = open(file,'rb').read()
    response = rekognition_client.detect_faces(
        Image = {
            'Bytes': file
        },
        Attributes = ['ALL']
    )


    for face in response['FaceDetails']:
    	
        print('The candidate is aged between ' + str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']))
    	
        print('The candidate is ' + str(face['Gender']['Value']))
    	
        Sunglass = str(face['Sunglasses']['Value'])
        if Sunglass == 'True': 

            print('The candidate is wearing sunglass')
        else:
        
            print('The candidate is not wearing sunglass')

        
        for emotion in face['Emotions']:
            if (emotion['Confidence'] > 70):
          	     print('The person is {} with confidence of {}'.format(emotion['Type'],emotion['Confidence']))

        Smile = str(face['Smile']['Value'])
        if Smile == 'True': 

            print('The candidate looks happy in this picture. Keep loving you life ')
        else:
        
            print('The candidate doesnot look much happy. After you join our company we will put a smile on that face for sure. ')

