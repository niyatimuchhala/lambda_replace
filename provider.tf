provider "aws" {
  region = "eu-central-1"
  access_key=var.aws_access_key
  secret_key=var.aws_secret_key
}

variable "aws_access_key"{
default = "AXXXXXXXXXXXXXXXXX"
}
variable "aws_secret_key"{
default = "uXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}