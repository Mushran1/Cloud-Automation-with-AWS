... import boto3
... import time
... from datetime import datetime, timedelta
... 
... # Initial Setup
... aws_access_key_id = 'YOUR_ACCESS_KEY'
... aws_secret_access_key = 'YOUR_SECRET_KEY'
... region_name = 'us-east-1'
... 
... ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
... cloudwatch_client = boto3.client('cloudwatch', region_name=region_name)
... 
... # Creating EC2 instance
... def create_instance():
...     tags = [{"ResourceType": "instance", "Tags": [{"Key": "Name", "Value": "baseline VM"}]}]
...     new_instance = ec2_client.run_instances(ImageId='ami-0df435f331839b2d6', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='easy', TagSpecifications=tags)
...     instance_id = new_instance['Instances'][0]['InstanceId']
...     print(f"New Instance Created: {instance_id}")
...     return instance_id
... 
... # Monitoring Instance CPU Utilization
... def monitor_instance(instance_id):
...     secondary_instance_id = ""
...     start_time = datetime.now()
...     while True:
...         end_time = datetime.now()
...         response = cloudwatch_client.get_metric_statistics(Namespace='AWS/EC2',
...                                                            MetricName='CPUUtilization',
...                                                            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
...                                                            StartTime=start_time - timedelta(seconds=600),
...                                                            EndTime=end_time,
...                                                            Period=60,
...                                                            Statistics=['Average'],
...                                                            Unit='Percent')
...         cpu_usage = response['Datapoints'][0]['Average'] if response['Datapoints'] else 0
...         print(f"Current CPU Usage: {cpu_usage}%")
... 
...         if cpu_usage > 50:
...             if not secondary_instance_id:
...                 secondary_instance_id = create_instance()
...         elif cpu_usage < 50 and secondary_instance_id:
...             ec2_client.terminate_instances(InstanceIds=[secondary_instance_id])
...             print(f"Terminated Secondary Instance: {secondary_instance_id}")
...             secondary_instance_id = ""
... 
...         time.sleep(60)  # loop every minute
... 
... # Main function
... if __name__ == "__main__":
...     baseline_instance_id = create_instance()
...     monitor_instance(baseline_instance_id)
