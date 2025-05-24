import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

def send_email_notification(user_id, model_name, graph_type):
    ses_client = boto3.client('ses', region_name='eu-west-1')
    cognito_client = boto3.client('cognito-idp', region_name='eu-west-1')
    try:
        user = cognito_client.admin_get_user(
            UserPoolId=os.environ.get("USER_POOL_ID"),
            Username=user_id
        )

        email = next(attr['Value'] for attr in user['UserAttributes'] if attr['Name'] == 'email')
        print("User email fetched successfully:", email)
        
    except ClientError as e:
        print("Error fetching user email:", e.response['Error']['Message'])
        return
    
    subject = "You're All Set - Your NMA Graph is ready!"
    body_html = (
        f"<h2>Hey, Deep Thinker!</h2>"
        f"<p>Great news! The {graph_type} graph process for the model {model_name} is now complete, and you can officially log in to the system and start exploring.<br>We're excited to have you on board and expose you to BETTER model explanations.</p>"
        f"<p>Welcome aboard!</p>"
        f"<p>Best regards,<br>BETTER Team</p>"
        f"<p><strong>Note:</strong> This is an automated message. Please do not reply to this email.</p>"
    )
    
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body_html}}}
    try:
        response = ses_client.send_email(
            Source="betterxai2025@gmail.com",
            Destination={"ToAddresses": [email]},
            Message=message
        )
        print("Email sent! Message ID:", response['MessageId'])
    except ClientError as e:
        print("Error sending email:", e.response['Error']['Message'])

if __name__ == "__main__":
    user_id = os.environ.get("user_id")
    model_name = os.environ.get("model_name")
    graph_type = os.environ.get("graph_type")
    send_email_notification(user_id, model_name, graph_type)