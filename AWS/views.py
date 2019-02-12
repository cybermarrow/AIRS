from django.http import HttpResponse
from django.shortcuts import render
import boto3

import datetime

def hello(request):
    today = datetime.datetime.now().date()
    return render(request,"hello.html",{"today" : today})

def aws_vpcs(request):
    vpc_list = []
    print("Returning list of vpcs now")
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.describe_vpcs(
        Filters=[
            {
                'Name': 'state',
                'Values': ['available']
            }
        ]
    )
    resp = response['Vpcs']

    for vpc in resp:
        for k, v in vpc.items():
            if (k == 'VpcId'):
                vpc_list.append(v)
    return render(request,"vpc.html",{"vpc_list" : vpc_list})

def listInstances(request):
    print("List ec2 instance")

    client = boto3.client('ec2', region_name='us-east-1')

    response = client.describe_instances()
    reservations = response['Reservations']
    instances_list = []

    for reservation in reservations:
        instances = reservation['Instances']
        for instance in instances:
            instances_list.append(instance['InstanceId'])

    return render(request, "instances.html", {"instances": instances_list})
