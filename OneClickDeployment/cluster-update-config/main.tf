resource "null_resource" "step" {



  provisioner "local-exec" {
        
        command = "./updateConfig.sh"
        interpreter = ["sh"]
      
  }
}