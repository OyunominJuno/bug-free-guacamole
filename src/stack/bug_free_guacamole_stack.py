from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class BugFreeGuacamoleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_lambda = _lambda.Function(
            self, 'HelloWorldFunction',
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler='lambda.lambda_handler',
            code=_lambda.Code.from_asset('lambda/lambda_handler'),
            timeout=Duration.seconds(30),
            environment={
                'ENVIRONMENT': self.node.try_get_context('environment') or 'dev'
            }
        )
        
        api = apigw.LambdaRestApi(
            self, 'HelloWorldApi',
            handler=hello_lambda,
            proxy=False
        )
        
        hello_resource = api.root.add_resource('hello')
        hello_resource.add_method('GET')
        hello_resource.add_method('POST')
        
        CfnOutput(self, 'ApiUrl', value=api.url)
