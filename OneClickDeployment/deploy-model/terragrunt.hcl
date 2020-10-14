dependency "helm" {
  config_path = "../helm-chart"
  skip_outputs = true
}

dependency "cluster" {
  config_path = "../cluster"
  skip_outputs = true
}

dependency "configeks" {
  config_path = "../cluster-update-config"
  skip_outputs = true
}
