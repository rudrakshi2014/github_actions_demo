import aws_cdk as core
import aws_cdk.assertions as assertions

from rudrakshi_cdk.rudrakshi_cdk_stack import RudrakshiCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in rudrakshi_cdk/rudrakshi_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RudrakshiCdkStack(app, "rudrakshi-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
