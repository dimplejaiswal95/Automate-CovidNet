
import os
from flask import Flask, request, jsonify
import requests
from werkzeug import secure_filename
from PIL import Image
import time


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
            url1 = "http://a5870bd1984bc448f9f3a36ed9e8ed23-704563747.us-east-2.elb.amazonaws.com:8000/predict"

            # accessing pod running covidxr3b model
            url2 = "http://abf9ec2fb1f204961974d5f5a387c455-817119906.us-east-2.elb.amazonaws.com:8001/predict"

            # accessing pod running covidxr3c model
            url3 = "http://aa26a39348a0a4c86b5031669be1af8a-1986313110.us-east-2.elb.amazonaws.com:8002/predict"

            # accessing pod running covidxr4a model
            url4 = "http://a97f35d8860cc4b8b83e49b6b801965c-989121730.us-east-2.elb.amazonaws.com:8003/predict"

            # accessing pod running covidxr4b model
            url5 = "http://a8c5d5019818e4aadafb338fbf821214-680025782.us-east-2.elb.amazonaws.com:8004/predict"

            # accessing pod running covidxr4c model
            url6 = "http://ae2ebba71008147279992f76bb729356-1915655231.us-east-2.elb.amazonaws.com:8005/predict"



            path = os.path.abspath(os.getcwd()+'/'+fname)
            #print(path)

            try:
                req1 = requests.post(url1, files = {'image': open(path, 'rb')},timeout=(300,300))
            except requests.exceptions.RequestException:
                raise Exception('Failed to connect to %s' % url) from None
            #time.sleep(30)
            try:
                req2 = requests.post(url1, files = {'image': open(path, 'rb')},timeout=(300,300))
            except requests.exceptions.RequestException:
                raise Exception('Failed to connect to %s' % url) from None
            #time.sleep(30)

            try:

                req3 = requests.post(url1, files = {'image': open(path, 'rb')},timeout=(300,300))

            except requests.exceptions.RequestException:
                raise Exception('Failed to connect to %s' % url) from None
            #time.sleep(30)
            
            result1 = req1.json()
            print(result1)            
            result2 = req2.json()
            print(result2)
            result3 = req3.json()
            print(result3)



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

                js = { 'Test': 'Test completes at Test A, patient is covid positive',
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

                js = { 'Test': 'Test completes at Test A, patient is normal ',
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

                js = { 'Test': 'Test completes at Test A, patient has pneumonia ',
                    'prediction' : 'pneumonia',
                    'result 1' : result1,
                    'result 2' : result2,
                    'result 3' : result3,
 
                }

                
            #test B
            else:

                
                try:

                    req4 = requests.post(url1, files = {'image': open(path, 'rb')},timeout=(300,300))
                except requests.exceptions.RequestException:
                    raise Exception('Failed to connect to %s' % url) from None
                #time.sleep(60)
                try:
                    req5 = requests.post(url1, files = {'image': open(path, 'rb')},timeout=(300,300))
                except requests.exceptions.RequestException:
                    raise Exception('Failed to connect to %s' % url) from None
                #time.sleep(60)
                try:

                    req6 = requests.post(url1, files = {'image': open(path, 'rb')},timeout=(300,300))
                except requests.exceptions.RequestException:
                    raise Exception('Failed to connect to %s' % url) from None
                #time.sleep(60)


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

                    js = { 'Test': 'Test completes at Test B, patient is covid positive ',
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

                    js = { 'Test': 'Test completes at Test B, patient is normal ',
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

                    js = { 'Test': 'Test completes at Test B, patient is pneumonia ',
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

                    js = { 'Test': 'Test completes at Test B, patient condition is unpredictable ',
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


