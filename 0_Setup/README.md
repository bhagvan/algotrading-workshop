# Set up your development environment

**Time to complete:** 5-10 minutes.

## What are we building?

We are going to use [AWS SageMaker](https://aws.amazon.com/sagemaker/) as our exploration and backtest environment. It will get you bootstrapped with a Jupyter Notebook that is able to run the notebooks for this workshop.

_If you already have running Jupyter Notebook, feel free to use that. Make sure you clone the git repository and you grant the SageMakerExecutionRole access to ECS._

### Step 1: Create a S3 Bucket for SageMaker

1. Navigate to Amazon S3 [in the console](https://console.aws.amazon.com/s3).
1. Choose Create Bucket.
1. Provide a globally unique name for your bucket such as ‘algoworkshop-firstname-lastname’.
1. Select the Region you’ve chosen to use for this workshop from the dropdown.

Keep in mind that your bucket’s name must be globally unique across all regions and customers. We recommend using a name like 'algoworkshop-firstname-lastname'. If you get an error that your bucket name already exists, try adding additional numbers or characters until you find an unused name.

### Step 2: Create Git Repository for Notebook Instance

1. Navigate to Amazon SageMaker [in the console](https://console.aws.amazon.com/sagemaker) and Select Notebook / Git Repository and Click **Add repository**
1. Select GitHuv/Other Git-based repo and create a new repository.
1. Set 'Amazon SageMaker repository name' to algotrading-workshop, Set 'Git Repository URL' to https://github.com/osteffmann/algotrading-workshop
1. Select to use No Secret
1. Click **Add repository**

### Step 3: Create Git Repository for Notebook Instance

1. Navigate to Amazon SageMaker [in the console](https://console.aws.amazon.com/sagemaker) and Select Notebook / Git Repository and Click **Add repository**
1. Select GitHuv/Other Git-based repo and create a new repository.
1. Set 'Amazon SageMaker repository name' to algotrading-workshop, Set 'Git Repository URL' to https://github.com/osteffmann/algotrading-workshop
1. Select to use No Secret
1. Click **Add repository**
