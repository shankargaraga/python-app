'''Managing IAM users and playing around'''
import boto3
def pager():
    iam=boto3.client('iam')
    response=iam.create_user(UserName='shankar')
    print(response)

    users=iam.get_paginator('list_users')
    print(users)
    print(users.paginate())

    for resp in users.paginate():
        print(resp)

    iam.update_user(UserName='Shankar',NewUserName="swamy")
    iam.delete_user(UserName="swamy")

    
