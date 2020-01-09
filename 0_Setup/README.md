# Set up the environment

**Time to complete:** 5-10 minutes.

## What are we building?

We are going to use [AWS SageMaker](https://aws.amazon.com/sagemaker/) as our exploration and backtest environment. It will get you bootstrapped with a Jupyter Notebook that is able to run the notebooks for this workshop.

_If you already have a running Jupyter Notebook, feel free to use that. Make sure you clone this git repository in the notebook and you attach **AmazonEC2ContainerRegistryFullAccess** to the SageMakerExecutionRole that is used in your notebook.

### Step 1: Create a S3 Bucket for SageMaker

1. Navigate to Amazon S3 [in the console](https://console.aws.amazon.com/s3).
1. Choose Create Bucket.
1. Provide a globally unique name for your bucket such as **algoworkshop-firstname-lastname**.
1. Select the Region you’ve chosen to use for this workshop from the dropdown.

Keep in mind that your bucket’s name must be globally unique across all regions and customers. We recommend using a name like **algoworkshop-firstname-lastname**. If you get an error that your bucket name already exists, try adding additional numbers or characters until you find an unused name.

### Step 2: Create Git Repository for Notebook Instance

1. Navigate to Amazon SageMaker [in the console](https://console.aws.amazon.com/sagemaker) and Select Notebook / Git Repository and Click **Add repository**.
1. Select GitHuv/Other Git-based repo and create a new repository.
1. Set 'Amazon SageMaker repository name' to **algotrading-workshop**, Set 'Git Repository URL' to https://github.com/osteffmann/algotrading-workshop.
1. Select to use No Secret.
1. Click **Add repository**.

### Step 3: Create Notebook Instance

1. Navigate to Amazon SageMaker [in the console](https://console.aws.amazon.com/sagemaker) and Select Notebook / Notebooks and Click **Create notebook instance**.
1. Set 'Notebook instance name' to **algotrading**.
1. Under Permissions and ecryption / IAM Role, select **Create a new role** if you don't have an existing AmazonSagerMaker-ExecutionRole-YYYYMMDDhhmmss. This will bring up a new screen that allows you to create a new IAM role. In this screen specify the S3 bucket that you have created in Step 2 (e.g. **algoworkshop-firstname-lastname**) and click **Create Role**.
1. Under Git Repositories, select the default repository from the dropdown list: **algotrading-workshop**. 
1. Click **Create notebook instance**.

### Step 4: Grant SageMaker access to ECS

1. Navigate to IAM [in the console](https://console.aws.amazon.com/iam) and Select Access Management / Roles and select the SageMakerExecutionRole-YYYYMMDDhhmmss that you selected in the notebook.
2. Click **Attach policies** and search for **AmazonEC2ContainerRegistryFullAccess**, select the checkbox next to it, and click **Attach policy**

## Next step:

We're ready to proceed getting the data for our trading strategies. [data](../1_Data).

