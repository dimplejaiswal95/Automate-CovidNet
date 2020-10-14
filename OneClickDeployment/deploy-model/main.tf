resource "null_resource" "step1" {



  provisioner "local-exec" {
        
        command = "./covidDeploy.sh"
        interpreter = ["sh"]
      
  }
}

