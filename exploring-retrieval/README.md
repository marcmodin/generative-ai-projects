# Exploring RAG

This is the `exploring-rag` directory. It is for playing around with how to RAG works with Langchain.

All examples will be using AWS Bedrock as the LLM provider.

## Prerequisites

This project requires Python and Jupyter Notebook to be installed on your machine. I personally use VSCode with the Python and Jupyter Extensions. AWS Account.

## Installation

To set up a virtual environment and install the required packages, follow these steps:

1. Install the virtual environment package if you haven't already:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Then install the required packages:

    ```
    pip install -r requirements.txt
    ```

3. ### Authenticate to AWS and Langsmith

    To run this notebook with AWS Bedrock models and Langsmith, authentication is necessary. This guide outlines the steps I take to authenticate with both platforms..

#### Env File

    Start by renaming `.env.example` to `.env`. In this file, specify your AWS region, profile, or credentials, alongside the API key for Langsmith and any additional variables required for your project. This file serves as the central hub for your environment configurations, and is loaded in the next cell.

#### Langsmith Api

    For LangSmith access, an API key is essential. Include your Langsmith API key in the `.env` file to authenticate your requests. This key enables you to interact with Langsmith services directly from your application.

#### AWS

    Authentication with AWS can vary depending on your environment setup. Generally, you should ensure that your AWS credentials or SSO profile and the `AWS_REGION` are exported to your terminal session.

    - **For VSCode Users:** If you've authenticated to AWS using `aws sso login` within a VSCode terminal, accessing AWS services via boto3 should not require hardcoded access keys. This method is convenient for those who prefer not to manage credentials manually.

    - **Manual Credential Export:** In cases where boto3 does not automatically detect your credentials from an AWS SSO session, you can export them manually using the command `eval "$(aws configure export-credentials --profile default --format env)"`. This command ensures that your AWS access keys are set as environment variables, making them accessible to your application.

    > **Note:** It is advisable to perform these steps before starting your development environment.
    >
    > If changes are made to the authentication setup, restarting your project might be necessary to ensure that the new environment variables are recognized.
    >
    > There are known issues with jupyter and aws credentials not being picked up properly: <https://github.com/microsoft/vscode-jupyter/issues/9774#issuecomment-1110328329>

### Langsmith

[LangSmith](https://docs.smith.langchain.com) is a platform designed for building production-grade applications based on Large Language Models (LLMs). It provides tools for debugging, testing, evaluating, and monitoring chains and intelligent agents constructed on any LLM framework.

This platform provides very useful information about our langchain applications which can be used to improve it further.

![langsmith dashboard](langsmith.png)

### Sample Data Sources

Sample documents to use can be found in `./docs`
