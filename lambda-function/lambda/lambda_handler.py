import json
import os
from datetime import datetime

def lambda_handler(event, context):
    """Lambda function handler."""
    name = event.get('name', 'World')
    environment = os.environ.get('ENVIRONMENT', 'dev')
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Hello, {name}!',
            'environment': environment,
            'timestamp': datetime.utcnow().isoformat()
        })
    }