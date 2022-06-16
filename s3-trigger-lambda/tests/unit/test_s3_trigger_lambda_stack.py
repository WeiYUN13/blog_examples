import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_trigger_lambda.s3_trigger_lambda_stack import S3TriggerLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_trigger_lambda/s3_trigger_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3TriggerLambdaStack(app, "s3-trigger-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
