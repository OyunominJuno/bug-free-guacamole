import aws_cdk as core
import aws_cdk.assertions as assertions

from src.stack.bug_free_guacamole_stack import BugFreeGuacamoleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in bug_free_guacamole/bug_free_guacamole_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BugFreeGuacamoleStack(app, "bug-free-guacamole")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
