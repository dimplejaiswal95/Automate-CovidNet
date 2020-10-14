dependency "cluster" {
  config_path = "../cluster"
}


dependency "configeks" {
  config_path = "../cluster-update-config"
  skip_outputs = true
}
