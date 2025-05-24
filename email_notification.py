import boto3
from botocore.exceptions import ClientError

def send_email_notification():
    ses_client = boto3.client('ses', region_name='eu-west-1')
    subject = "NMA Graph Job Completed Successfully"
    body = "The NMA explaination for the model <model_name> with <Graph-type> is ready!."
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    try:
        response = ses_client.send_email(
            Source="<BETTER>@gmail.com",
            Destination={"ToAddresses": ["<example>@gmail.com"]},
            Message=message
        )
        print("Email sent! Message ID:", response['MessageId'])
    except ClientError as e:
        print("Error sending email:", e.response['Error']['Message'])

if __name__ == "__main__":
    send_email_notification()
# This script sends an email notification using AWS SES when executed.