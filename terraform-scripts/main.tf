provider "aws" {
  region     = var.region
}

resource "aws_instance" "example" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  user_data = var.user_data_script
  tags = {
    Name = "Cargomatic-Project"
  }
}
