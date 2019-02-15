import boto3
#import uuid
def lambda_handler(event, context):
   # this will create dynamodb resource object and
   # here dynamodb is resource name
   client = boto3.resource('dynamodb')

   # this will search for dynamoDB table
   # your table name may be different
   table = client.Table("detail_user")
   print(table.table_status)
   table.put_item(Item= {'name': 'himanshu','age':  '20', 'uuid':'84f7e456-75eb-4080-a2e0-bb027888bfcf'})
   table.put_item(Item= {'name': 'tiwari','age':  '50', 'uuid':'d7d03ebe-abb2-402a-b6a0-fe2c2bad8142'})
   table.put_item(Item= {'name': 'kapil','age':  '05','uuid':'99b1602a-7506-43ca-9793-cbbfc3379da8'})
   c=table.get_item(Key = {'uuid' : '84f7e456-75eb-4080-a2e0-bb027888bfcf'})
   print(c)