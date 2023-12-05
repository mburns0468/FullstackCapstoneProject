# FullstackCapstoneProject
Fullstack Academy Capstone Project Files
Cocktail Search Engine

Overview
The Cocktail Search Engine is a web application that allows users to search for cocktail recipes. The application is powered by a serverless backend implemented using AWS Lambda, API Gateway, and other AWS services.

Usage
Web Application

    Open the index.html file in a web browser to access the Cocktail Search Engine.

    Enter the name of a cocktail in the search bar and click the "Drink Up" button to retrieve information about the cocktail.

AWS Lambda and API Gateway

The backend of the Cocktail Search Engine is implemented using AWS Lambda and API Gateway. These services handle the processing of user requests and communication with external APIs.
Lambda Function (lambda_function.py)

This Lambda function receives user input, queries an external cocktail database API, and returns formatted cocktail information.
API Gateway

The API Gateway serves as the entry point for HTTP requests and directs them to the Lambda function. It also manages authentication and authorization if needed.
Deployment

To deploy the Cocktail Search Engine backend on AWS:

    Create an AWS account if you don't have one.

    Install and configure the AWS CLI with the necessary credentials.

    Deploy the AWS CloudFormation stack using the provided CloudFormation template (cloudformation_template.yaml). This template creates the required AWS resources, including the Lambda function, API Gateway, VPC, subnets, security groups, and more.

    Once the stack is created, check the AWS CloudFormation console for the stack's outputs. Retrieve the API Gateway endpoint.

    Update the apiGatewayEndpoint variable in the index.html file with the API Gateway endpoint.

    Open the index.html file in a web browser and start searching for cocktails!

Technologies Used

    HTML, CSS, and JavaScript for the frontend
    AWS Lambda for serverless function execution
    AWS API Gateway for creating and managing APIs
    AWS CloudFormation for infrastructure as code

Contributors
Matthew Burns, Aaron McIntire, Cody Stocker, Blanche Ranguma
