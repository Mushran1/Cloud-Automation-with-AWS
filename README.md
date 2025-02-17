# Cloud-Automation with AWS
In the fast-paced tech world, solutions that solve complex problems and streamline processes are critical. Cloud automation stands out by offering the flexibility to manage and monitor virtual resources efficiently. This GitHub repository hosts the Cloud Automation project, focusing on dynamic resource management using AWS services.

## Project Overview

This project revolves around automating the operations of virtual machines (VMs) within Amazon Web Services (AWS) using Python and the Boto3 SDK. The main goal is to automate the management of EC2 instances based on CPU utilization metrics, which are reliably captured through CloudWatch

## Functionality

The Python script developed for this project performs several key functions:

 1. Initializes an Amazon EC2 instance ("baseline VM") using specified parameters.
 2. Monitors the baseline VM's CPU utilization in real-time, adapting to changes by managing additional resources, thereby optimizing performance and cost.
 3. Responds dynamically to CPU utilization changes:
    - When CPU utilization exceeds 50% for five consecutive checks, it provisions a secondary 'micro'        type EC2 instance to manage the increased load.
    - Conversely, when CPU utilization falls below 50% equally consecutively, it terminates this             secondary instance to reduce unnecessary costs.
      
## Practical Applications

This project is an exemplary case of cloud automation, managing cloud infrastructure responsively based on real-time data. It is especially beneficial in scenarios with fluctuating workloads, where manual monitoring is inefficient and prone to errors.

## Tools and Technologies Used


 - AWS Boto3: Python SDK for AWS providing direct interaction with AWS services.
 - AWS EC2 & CloudWatch: Employed for creating and monitoring virtual machines.
 - Python: All backend scripts are authored in Python, interfacing with AWS SDKs to manipulate AWS        resources.

This integrated approach of cloud services and custom automation scripts illustrates how businesses can achieve significant cost-efficiency and performance optimization.

## Additional Documentation

For a comprehensive guide and a deeper insight into the project implementation, refer to the PDF document provided in this repository, which includes screenshots along with detailed code explanations.
