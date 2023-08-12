# Cargomatic Project Challenge

Welcome to the Cargomatic Challenge repository!

─▄▀▀▀▀▄─█──█────▄▀▀█─▄▀▀▀▀▄─█▀▀▄
─█────█─█──█────█────█────█─█──█
─█────█─█▀▀█────█─▄▄─█────█─█──█
─▀▄▄▄▄▀─█──█────▀▄▄█─▀▄▄▄▄▀─█▄▄▀

─────────▄██████▀▀▀▀▀▀▄
─────▄█████████▄───────▀▀▄▄
──▄█████████████───────────▀▀▄
▄██████████████─▄▀───▀▄─▀▄▄▄──▀▄
███████████████──▄▀─▀▄▄▄▄▄▄────█
█████████████████▀█──▄█▄▄▄──────█
███████████──█▀█──▀▄─█─█─█───────█
████████████████───▀█─▀██▄▄──────█
█████████████████──▄─▀█▄─────▄───█
█████████████████▀███▀▀─▀▄────█──█
████████████████──────────█──▄▀──█
████████████████▄▀▀▀▀▀▀▄──█──────█
████████████████▀▀▀▀▀▀▀▄──█──────█
▀████████████████▀▀▀▀▀▀──────────█
──███████████████▀▀─────█──────▄▀
──▀█████████████────────█────▄▀
────▀████████████▄───▄▄█▀─▄█▀
──────▀████████████▀▀▀──▄███
──────████████████████████─█
─────████████████████████──█
────████████████████████───█
────██████████████████─────█
────██████████████████─────█
────██████████████████─────█
────██████████████████─────█
────██████████████████▄▄▄▄▄█

─────────────█─────█─█──█─█───█
─────────────█─────█─█──█─▀█─█▀
─────────────█─▄█▄─█─█▀▀█──▀█▀
─────────────██▀─▀██─█──█───█




# Cargomatic Project:

Welcome to the Cargomatic Project Challenge. This repository houses the solutions for **Cargomatic Project Challenge 01**, which focuses on managing AWS EC2 instances through Python scripts and Terraform configurations. The challenge comprises three key tasks:

### Python Script (`ec2-management.py`) - list_running_instances() method

- **Objective**: List all running EC2 instances in a specified AWS region.
- **Usage**: Run the Python script using the command: `python ec2-managment.py list-running-instances <AWS_REGION>`
- **Dependencies**: Requires Boto3. Install using `pip install boto3`.

### Integration (`stop_old_instances.py`) - stop_instances() method

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
