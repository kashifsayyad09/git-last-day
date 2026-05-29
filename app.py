import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('YourTableName')

# Insert an item
table.put_item(
   Item={
        'username': 'jdoe',
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
    }
)

# Get an item
response = table.get_item(Key={'username': 'jdoe'})
item = response.get('Item')
print(item)

