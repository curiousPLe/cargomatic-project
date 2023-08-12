# Cargomatic Project Challenge

Welcome to the 🚙 **Cargomatic Project Challenge**

![VhdI](https://github.com/curiousPLe/cargomatic-project/assets/43125083/7f85ed53-8200-4b56-93b3-b44e6186c814)

This repository houses the solutions for the **Cargomatic Project Challenge 01**, which focuses on managing AWS EC2 instances through Python scripts and Terraform configurations. The challenge comprises three key tasks:

### Python Script (`ec2-management.py`)

- **Objective**: List all running EC2 instances in a specified AWS region.
- **Usage**: Run the Python script using the command: `python ec2-managment.py list-running-instances <AWS_REGION>`
- **Dependencies**: Requires Boto3. Install using `pip install boto3`.

### Integration (`stop_old_instances.py`)

- **Objective**: Stop EC2 instances created more than a week ago.
- **Usage**: Run the Python script using the command: `python ec2-managment.py stop-instances <AWS_REGION>`
- **Dependencies**: Requires Boto3. Install using `pip install boto3`.

### Terraform Configuration (`main.tf`)

- **Objective**: Provision an EC2 instance with the latest version of Python3 installed using user-data.
- **Usage**: Apply the Terraform configuration using `terraform init` and `terraform apply`.
- **Note**: Replace placeholders (`AMI_ID`, `SUBNET_ID`, etc.) with desired values.


## Getting Started

1. **Clone the Repository**

    Begin by cloning this repository to your local machine:

    ```sh
    git clone https://github.com/curiousPLe/cargomatic-project.git
    cd cargomatic-project
    ```

2. **Configure AWS Credentials**

    To interact with AWS services, ensure you have configured your AWS credentials and selected a default region. You can use the AWS CLI or environment variables to set your credentials.

3. **Task Execution**

    For each task, navigate to the respective directory and follow the instructions provided in the individual task usage of the README file.

##########

Thank you for reading 😄 Have a great day!

![fxUT](https://github.com/curiousPLe/cargomatic-project/assets/43125083/4be705cd-6a3c-4ce9-948d-0d0d54e33258)

