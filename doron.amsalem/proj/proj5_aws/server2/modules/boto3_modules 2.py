import boto3


def store_data(data, table_name):
    db = boto3.resource('dynamodb')
    table = db.Table(table_name)

    table.put_item(
        Item={
          'weather data': str(data['days'])
        }
    )
