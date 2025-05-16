def handler(event, context):
    print("Lambda Function 2 is triggered!")
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda 2'
    }