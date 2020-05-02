from __future__ import print_function # Python 2/3 compatibility
import boto3
 
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8080")
 
 
table = dynamodb.create_table(
    TableName='DynamoHits',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
 
print("Table status:", table.table_status)