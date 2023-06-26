# S3 File Upload/Delete Notifications via SNS

**Objective:**
This Lambda function allows you to send email notifications via Amazon SNS whenever a file is uploaded or deleted in an S3 bucket. The email notification includes custom information such as the name of the object and bucket.

**Step 1:Prerequisites:**
An AWS account with appropriate permissions to create and configure Lambda functions, S3 buckets, and SNS topics.

**Step 2: Configuring Amazon SNS**
1. Create an SNS Topic
2. Create a Subscription --> protocol as "Email

**Step 3: Clone or Download the Repository**
Clone or download the repository containing the Lambda function code to your local machine.

**Step 4: Update Lambda Function Code**
Open the lambda_function.py file and update the following placeholders with your own values:
TOPIC_ARN: Replace with the ARN of your SNS topic.

**Step 5: Save Changes**
Save the changes to the lambda_function.py file.

**Step 6: IAM Roles**
To grant the necessary permissions for your Lambda function to send email notifications using Amazon SNS when a file is uploaded or deleted in an S3 bucket, you should provide the function with the following IAM permissions:
1. S3 Read-Only Access Policy:
Attach the AmazonS3ReadOnlyAccess policy to the IAM role. This policy allows your Lambda function to read events from the S3 bucket when files are uploaded or deleted. 
2. SNS Publish Policy:
Create a custom policy that allows your Lambda function to publish messages to an SNS topic.
![image](https://github.com/FuzailN/s3-sns-file-notifications/assets/129302212/24281936-b51b-424b-a658-c00196837a95)

This policy allows your Lambda function to publish messages to any SNS topic.

Save the policy --> Go back to the role creation wizard --> search for the custom policy you just created ("SNSPublishPolicy"). Select the policy--> Provide a name for the role (e.g., "LambdaS3SNSRole") and click on "Create role

![image](https://github.com/FuzailN/s3-sns-file-notifications/assets/129302212/ce9c0ac8-9e84-44f7-a223-07019aa335e6)


**Step 7: Create the Lambda Function**
Open a terminal or command prompt and configure your AWS credentials using the aws configure command

Use the AWS CLI to create the Lambda function by running the following command:

**aws lambda create-function --function-name s3-sns-notifications --runtime python3.10 --handler lambda_function.lambda_handler --role YOUR_LAMBDA_ROLE_ARN --zip-file fileb://lambda_function.zip**

**Step 7: Configure S3 Trigger (or) Add Trigger in Lambda Function**

Create an S3 bucket and specifying the Event trigger from the Properties. Allowing object creation and object removal.

![image](https://github.com/FuzailN/s3-sns-file-notifications/assets/129302212/ce545008-45b0-46c4-b8db-a6b97aadbb42)

![image](https://github.com/FuzailN/s3-sns-file-notifications/assets/129302212/61bcc0f2-d25f-488f-bdd3-cc3d4710bb80)

In the lambda function console, we can see that the S3 trigger is added

**Step 8: Verifying the Event Notification**
On uploading/deleting an object in the S3 bucket, we get an email notification as shown in the figure below.

![image](https://github.com/FuzailN/s3-sns-file-notifications/assets/129302212/d8c42ef6-59c9-45cb-93f5-54cf92aadaa6)

![image](https://github.com/FuzailN/s3-sns-file-notifications/assets/129302212/db2eedd9-f3ef-4452-9de0-fce6169968a5)

![image](https://github.com/FuzailN/s3-sns-file-notifications/assets/129302212/02df463a-5d32-418f-8e3f-87fff30903b1)




