from django.http import HttpResponse
from django.shortcuts import render
import boto3

import datetime

def hello(request):
    today = datetime.datetime.now().date()
    return render(request,"hello.html",{"today" : today})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def aws_vpcs():
    print("Returning list of vpcs now")
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.describe_vpcs(
        Filters=[
            {
                'state': 'available'
            }
        ]
    )
    resp = response['Vpcs']
    print(resp)