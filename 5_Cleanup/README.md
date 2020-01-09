# Cleanup

**Time to complete:** 5 minutes.

To avoid charges for resources you no longer need when you’re done with this workshop, you can delete them or, in the case of your notebook instance, stop them. Here are the resources you should consider:

### Step 1: Notebook instances

You have two options if you do not want to keep the notebook instance running. If you would like to save it for later, you can stop rather than deleting it.

1. To stop a notebook instance: click the Notebook instances link in the left pane of the SageMaker console home page. Next, click the Stop link under the ‘Actions’ column to the left of your notebook instance’s name. After the notebook instance is stopped, you can start it again by clicking the Start link. Keep in mind that if you stop rather than delete it, you will be charged for the storage associated with it.
1. To delete a notebook instance: first stop it per the instruction above. Next, click the radio button next to your notebook instance, then select Delete from the Actions drop down menu.

### Step 2: S3 Bucket

If you retain the S3 bucket created for this workshop, you will be charged for storage. To avoid these charges if you no longer wish to use the bucket, you may delete it. To delete the bucket, go to the S3 service console, and locate your bucket’s name in the bucket table. Next, click in the bucket table row for your bucket to highlight the table row. At the top of the table, the Delete Bucket button should now be enabled, so click it and then click the Confirm button in the resulting pop-up to complete the deletion.

### Step 3: Elastic Container Registry (ECR)

if you retain containers in ECR you created for this workshop, you could be charged for storage. To avoid these charges if you no longer wish to use these containers, you may delete it. To delete containers, go to the ECR service console.
