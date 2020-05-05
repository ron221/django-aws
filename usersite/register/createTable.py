import boto3

# # Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

# Create the DynamoDB table.
table = dynamodb.create_table(
    
    TableName='userRegister',
    KeySchema=[
        {'AttributeName': 'username', 'KeyType': 'HASH'},
        {'AttributeName': 'email', 'KeyType': 'RANGE'},
    ],
    AttributeDefinitions=[
        {'AttributeName': 'username', 'AttributeType': 'S'},
        {'AttributeName': 'email', 'AttributeType': 'S'},
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='userRegister')

# Print out some data about the table.
print(table.item_count)

# table = dynamodb.Table('users')

# table.put_item(
#    Item={
#         'username': 'janedoe',
#         'first_name': 'Jane',
#         'last_name': 'Doe',
#         'age': 25,
#         'account_type': 'standard_user',
#     }
# )
