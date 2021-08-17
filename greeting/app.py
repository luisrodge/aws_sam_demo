import json


def lambda_handler(event, context):
    name = "stranger"

    if (
        "queryStringParameters" in event
        and event["queryStringParameters"] is not None
        and "name" in event["queryStringParameters"]
    ):
        name = event["queryStringParameters"]["name"]

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": f"Hello there {name}",
            }
        ),
    }
