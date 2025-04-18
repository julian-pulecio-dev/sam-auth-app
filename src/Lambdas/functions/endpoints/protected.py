from headers import get_headers



def lambda_handler(event, context):    
    return {
        "statusCode": 200,
        "headers": get_headers(),
        "body": 'very secret'
    }
