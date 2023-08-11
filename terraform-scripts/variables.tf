variable "aws_access_key" {
  description = "AWS Access Key"
}

variable "aws_secret_key" {
  description = "AWS Secret Key"
}

variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  default     = "ami-08a52ddb321b32a8c"  # Amazon Linux 2 AMI ID
}

variable "subnet_id" {
  description = "Subnet ID"
}


variable "user_data_script" {
  description = "Provide initialization scripts that are executed when an instance is launched"
  default = ""
}