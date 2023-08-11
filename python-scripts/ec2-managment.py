import sys
from datetime import datetime, timezone
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import pytz

'''
The script will read your AWS configuration and credentials
from the ~/.aws/config and ~/.aws/credentials files.
'''

def list_running_instances(aws_region):
	''' This method returns all running EC2 instances in a given AWS region '''

	try:
		# Create a Boto3 EC2 client
		ec2_client = boto3.client('ec2', region_name=aws_region)

		# List all running instances
		response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
		for reservation in response['Reservations']:
			for instance in reservation['Instances']:
			    print("=" * 30)
			    print("Instance ID: ", instance['InstanceId'])
			    print("Instance Type: ", instance['InstanceType'])
			    print("Public IP: ", instance.get('PublicIpAddress', 'N/A'))
			    print("Private IP: ", instance['PrivateIpAddress'])
			    print("State: ", instance['State']['Name'])
			    print("=" * 30)

	except (BotoCoreError, ClientError) as e:
		print("An error occurred:", e )
	


def stop_instances(aws_region, max_age=7):
	''' This method stop any EC2 instance that is more than <day> olds'''

	try:
		# Create a Boto3 EC2 client
		ec2_client = boto3.client('ec2', region_name=aws_region)

		# List all running instances
		response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
		
		for reservation in response['Reservations']:
			for instance in reservation['Instances']:
			  	instance_id = instance['InstanceId']

			  	# Convert launch_time to datetime in UTC
			  	launch_time = instance['LaunchTime'].replace(tzinfo=pytz.UTC)

			  	# Get the current time in UTC
			  	now = datetime.now(timezone.utc)
			  	
			  	# Calculate instance age and stop instances older than max_age
			  	instance_age = (now - launch_time).days
			  	if instance_age < max_age:
			  		print("Stopping instance ", instance_id, " - Instance age: ", instance_age, " days)")
			  		ec2_client.stop_instances(InstanceIds=[instance_id])

	except (BotoCoreError, ClientError) as e:
		print("An error occurred:", e )


def main():
	if len(sys.argv) < 2:
		print("Usage: python ec2-managment.py <METHOD>")
		sys.exit(1)

	method_name = sys.argv[1]

	# Check the command-line argument and execute the specified method
	if sys.argv[1] == "list-running-instances":
		if not sys.argv[2]:
			print("Usage: python ec2-managment.py list-running-instances <AWS_REGION>")
			sys.exit(1)

		# Use the AWS region provided as a command-line argument
		aws_region = sys.argv[2]

		# Call the function to list running instances
		list_running_instances(aws_region)

	elif sys.argv[1] == "stop-instances":
		if not sys.argv[2]:
			print("Usage: python ec2-managment.py stop-instances <AWS_REGION>")
			sys.exit(1)

		# Use the AWS region provided as a command-line argument
		aws_region = sys.argv[2]

		# Call the function to stop running instances
		stop_instances(aws_region)

	print("  \\   ^__^")
	print("   \\  (oo)\\_______")
	print("      (__)\\       )\\/\\")
	print("          ||----w |")
	print("          ||     ||")


if __name__ == "__main__":
	main()
