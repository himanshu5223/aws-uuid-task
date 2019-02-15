import boto3
import uuid
def lambda_handler(event, context):

   # this will create dynamodb resource object and
   # here dynamodb is resource name
   client = boto3.resource('dynamodb')
   # this will search for dynamoDB table
   # your table name may be different
   table = client.Table("user")
   print(table.table_status)
   table.put_item(Item= { 'uuid' : str(uuid.uuid4()),'email': 'nhimanshu190@gmail.com','password':  '123!@#$',})
   table.put_item(Item= { 'uuid' : str(uuid.uuid4()),'email': 'tiwariabhishek@852.com','password':  '1@#$',})
   table.put_item(Item= { 'uuid' : str(uuid.uuid4()),'email': 'nhima190@gmail.com','password':  '123#$',})