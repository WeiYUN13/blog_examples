from aws_cdk import (
    aws_lambda as lambda_,
    Stack,
    aws_s3 as s3,
    aws_s3_notifications,
)
from constructs import Construct


class S3TriggerLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create lambda function
        function = lambda_.Function(self, "lambda_function_example",
                                    runtime=lambda_.Runtime.PYTHON_3_9,
                                    handler="lambda_handler.lambda_handler",
                                    code=lambda_.Code.from_asset("./lambda"))

        # create s3 buckets
        s3_bucket = s3.Bucket(self, "my_s3_bucket")

        # s3 notification to lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # send notification after event
        s3_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, notification)
