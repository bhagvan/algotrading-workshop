# Set up your development environment

**Time to complete:** 5-10 minutes.

## What are we building?

We are going to use [AWS SageMaker](https://aws.amazon.com/sagemaker/) as our exploration and backtest environment. It will get you bootstrapped with Jupyter Notebooks that are able to run the notebooks for this workshop.

_If you already have running Jupyter Notebook, feel free to use that. Make sure you clone the git repository and you grant the SageMakerExecutionRole access to ECS._

### Step 1: Create a S3 Bucket for SageMaker

<details>
<summary><strong>Expand if you want detailed directions</strong></summary><p>

1. Navigate to Amazon S3 [in the console](https://console.aws.amazon.com/s3)
2. Choose Create Bucket
3. Provide a globally unique name for your bucket such as ‘algoworkshop-firstname-lastname’.
4. Select the Region you’ve chosen to use for this workshop from the dropdown.

Keep in mind that your bucket’s name must be globally unique across all regions and customers. We recommend using a name like 'algoworkshop-firstname-lastname'. If you get an error that your bucket name already exists, try adding additional numbers or characters until you find an unused name.

</p></details>

### Step 2: Create Notebook Instance

1. Navigate to Amazon SageMaker [in the console](https://console.aws.amazon.com/sagemaker) and Select Notebook / Notebook Instances

