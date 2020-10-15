# Automate-CovidNet
## Requirements - 
- Dokcer
- python 
- Tensorflow
- Terraform
- Terragrunt 
- AWS cli
- Helm
- Kubectl
- Flask

## Set Up Instructions
* Dockerizing all the models-
  All the flask APIs are present [here](https://github.com/dimplejaiswal95/Automate-CovidNet/tree/main/flask-apis-for-model)
  Commands to create docker image-
  1. sudo docker build -t <**MODEL-Name**>:latest .
  1. sudo docker run -d -p 5000:5000 **MODEL-Name**
  1. Test the model, if it is successfully running -
      1. sudo docker ps -a
      1. curl -X POST -F image=@**IMAGE.jpg** 'http://localhost:5000/predict'
  1. Get image id for the container - sudo docker images
  1. sudo docker tag <**your image id**> <**your docker hub id**>/<**MODEL-Name**>
  1. sudo docker push <**your docker hub name**>/<**MODEL-Name**>
 
* One click deployment-
  Instructions for one click deployment are [here](https://github.com/dimplejaiswal95/Automate-CovidNet/tree/main/OneClickDeployment)
 
 * Dockerizing the [test-app](https://github.com/dimplejaiswal95/Automate-CovidNet/tree/main/test-app)-
 Similar to dockerizing the models.
 
 * Deploying the [test](https://github.com/dimplejaiswal95/Automate-CovidNet/tree/main/deploy-test) on Cluster -
    command: kubectl apply -f [deploy-test-app.yaml](https://github.com/dimplejaiswal95/Automate-CovidNet/blob/main/deploy-test/deploy-test-app.yaml)


## Presentation

Here is the link for [presentation](https://github.com/dimplejaiswal95/Automate-CovidNet/blob/main/Presentation.pdf)

