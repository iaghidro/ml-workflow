# ml-workflow
A blueprint for a machine learning workflow using AWS services.

## Creating a dev workflow

* Log into the AWS console and go to cloud formation
* Create a new stack using the `/dev-workflow.yml` file
* Name the CF stack, and change any of the paramters if needed
* After the CF stack reached a create complete state, go to the SageMaker service
* Go to Notebook > Notebook instances > find your notebook instance and click "Open Jupyter"
* The notebook files will be located in `/dev-workflow/notebooks/`