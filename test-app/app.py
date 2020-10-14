import numpy as np
import tensorflow as tf
import os
import cv2
from flask import Flask, request, jsonify
import requests
import io
from werkzeug import secure_filename
from PIL import Image


app = Flask(__name__)


@app.route("/predict", methods=["POST"])


def predict():

    js = {}

    if request.method == 'POST': 
        
        if request.files.get("image"):
  
            img = request.files['image']
            fname = secure_filename(img.filename)
            img = Image.open(img)
            #print(fname)
            img.save(fname)


            # accessing pod running covidxr3a model
            url1 = "http://adbeb03aa57004399a9e9af0ea7a5bd5-719317157.us-east-2.elb.amazonaws.com:5001/predict"

            # accessing pod running covidxr3b model
            url2 = "http://adbeb03aa57004399a9e9af0ea7a5bd5-719317157.us-east-2.elb.amazonaws.com:5001/predict"

            # accessing pod running covidxr3c model
            url3 = "http://adbeb03aa57004399a9e9af0ea7a5bd5-719317157.us-east-2.elb.amazonaws.com:5001/predict"

            # accessing pod running covidxr4a model
            url4 = "http://adbeb03aa57004399a9e9af0ea7a5bd5-719317157.us-east-2.elb.amazonaws.com:5001/predict"

            # accessing pod running covidxr4b model
            url5 = "http://adbeb03aa57004399a9e9af0ea7a5bd5-719317157.us-east-2.elb.amazonaws.com:5001/predict"

            # accessing pod running covidxr4c model
            url6 = "http://adbeb03aa57004399a9e9af0ea7a5bd5-719317157.us-east-2.elb.amazonaws.com:5001/predict"



            path = os.path.abspath(os.getcwd()+'/'+fname)
            #print(path)


            req1 = requests.post(url1, files = {'image': open(path, 'rb')},)
            req2 = requests.post(url2, files = {'image': open(path, 'rb')},)
            req3 = requests.post(url3, files = {'image': open(path, 'rb')},)

            
            result1 = req1.json()
            result2 = req2.json()
            result3 = req3.json()

            result1.pop('filename',None)
            result2.pop('filename',None)
            result3.pop('filename',None)

            result1.update({'Model':'COVIDXR3A Model'})
            result2.update({'Model':'COVIDXR3B Model'})
            result3.update({'Model':'COVIDXR3C Model'})


            str1 = "COVID-19"
            str2 = 'normal'
            str3 = 'pneumonia'

            #test A
            if(result1['prediction']==str1 and result2['prediction']==str1 and result3['prediction']==str1):

                print("Test completes at Test A, patient is covid positive ")
                print(result1)
                print(result2)
                print(result3)

                js = { 'Test': 'Test A',
                    'prediction' : 'COVID-19',
                    'result 1' : result1,
                    'result 2' : result2,
                    'result 3' : result3,
 
                }


                #return(jsonify(js))


            elif(result1['prediction']==str2 and result2['prediction']==str2 and result3['prediction']==str2):

                print("Test completes at Test A, patient is normal ")
                print(result1)
                print(result2)
                print(result3)

                js = { 'Test': 'Test A',
                    'prediction' : 'normal',
                    'result 1' : result1,
                    'result 2' : result2,
                    'result 3' : result3,
 
                }


            
            elif(result1['prediction']==str3 and result2['prediction']==str3 and result3['prediction']==str3):

                print("Test completes at Test A, patient has pneumonia ")
                print(result1)
                print(result2)
                print(result3)

                js = { 'Test': 'Test A',
                    'prediction' : 'pneumonia',
                    'result 1' : result1,
                    'result 2' : result2,
                    'result 3' : result3,
 
                }

                
            #test B
            else:

                

                req4 = requests.post(url4, files = {'image': open(path, 'rb')},)
                req5 = requests.post(url5, files = {'image': open(path, 'rb')},)
                req6 = requests.post(url6, files = {'image': open(path, 'rb')},)


                result4 = req4.json()
                result5 = req5.json()
                result6 = req6.json()

                result4.pop('filename',None)
                result5.pop('filename',None)
                result6.pop('filename',None)

                result4.update({'Model':'COVIDXR4A Model'})
                result5.update({'Model':'COVIDXR4B Model'})
                result6.update({'Model':'COVIDXR4C Model'})               

                if(result4['prediction']==str1 and result5['prediction']==str1 and result6['prediction']==str1):

                    print("Test completes at Test B, patient is covid positive ")
                    print(result1)
                    print(result2)
                    print(result3)  
                    print(result4)
                    print(result5)
                    print(result6)   

                    js = { 'Test': 'Test B',
                        'prediction' : 'COVID-19',
                        'result 1' : result1,
                        'result 2' : result2,
                        'result 3' : result3,
                        'result 4' : result4,
                        'result 5' : result5,
                        'result 6' : result6,
    
                    }       

                elif(result4['prediction']==str2 and result5['prediction']==str2 and result6['prediction']==str2):

                    print("Test completes at Test B, patient is normal ")
                    print(result1)
                    print(result2)
                    print(result3)  
                    print(result4)
                    print(result5)
                    print(result6)     

                    js = { 'Test': 'Test B',
                        'prediction' : 'normal',
                        'result 1' : result1,
                        'result 2' : result2,
                        'result 3' : result3,
                        'result 4' : result4,
                        'result 5' : result5,
                        'result 6' : result6,
    
                    }          

                elif(result4['prediction']==str3 and result5['prediction']==str3 and result6['prediction']==str3):

                    print("Test completes at Test B, patient is pneumonia ")
                    print(result1)
                    print(result2)
                    print(result3)  
                    print(result4)
                    print(result5)
                    print(result6)   

                    js = { 'Test': 'Test B',
                        'prediction' : 'pneumonia',
                        'result 1' : result1,
                        'result 2' : result2,
                        'result 3' : result3,
                        'result 4' : result4,
                        'result 5' : result5,
                        'result 6' : result6,
    
                    }             
 

                else:
                    print("Test completes at Test B, patient condition is unpredictable ")
                    print(result1)
                    print(result2)
                    print(result3)  
                    print(result4)
                    print(result5)
                    print(result6)      

                    js = { 'Test': 'Test B',
                        'prediction' : 'Unpredictable, check results of each test',
                        'result 1' : result1,
                        'result 2' : result2,
                        'result 3' : result3,
                        'result 4' : result4,
                        'result 5' : result5,
                        'result 6' : result6,
    
                    }      


            return jsonify(js)

    return jsonify({'prediction' : 'No test performed, technical issue'})



# Model is very big so it's processing 1 request at a time
if __name__ == '__main__':
    app.run(host='0.0.0.0')


