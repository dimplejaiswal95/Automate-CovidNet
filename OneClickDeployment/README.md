# OneClickDeployment using Terragrunt and terraform 
- Cluster creation  (cluster dir)
- update kube-config (cluster-update-config dir) 
- helm-chart deployment (helm-chart dir)
- deployment of model to cluster (deploy-model dir)

# Note: if deployment is done only using terraform, then, run these commands in each directory:
 - terraform init
 - terraform apply

 #  if deployment using terragrunt and terraform, then, run the following command in current working dir (eg: here OneClickDeployment dir)
 - terragrunt apply-all
 



Dependencies:
- aws iam authenticator
- kubectl
- awscli
- terraform
- helm
- terragrunt

Note- update cluster name and region according to your location here
1. [In cluster dir](https://github.com/dimplejaiswal95/Automate-CovidNet/blob/main/OneClickDeployment/cluster/terraform.tfvars)
2. [In helm dir](https://github.com/dimplejaiswal95/Automate-CovidNet/blob/main/OneClickDeployment/helm-chart/terraform.tfvars)
