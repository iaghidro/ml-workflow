# ML Workflow

## Creating a machine learning developer workflow stack

- Create a github access token if you don't have one already. [Click here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) for instructions for creating one.
- Log into the AWS console and go to cloud formation.
- Create a new stack using the `/dev-workflow.yml` file.
- During creation do the following:
  - Name the CF stack
  - provide a unique environment name
  - use your code repository username
  - use the repository access token you created earlier
  - change any of the parameters if needed
- After the CF stack reached a create complete state, go to outputs.
- Click on the NotebookJupyterLab url which will open up the notebook.
- The notebook files will be located in `/REPO_NAME/notebooks/`.
- Use the JupyterLab git client to check out the branch of your choosing.

  **NOTE**: Shut down jupyter notebook once not in use from AWS console > SageMaker > Notebooks > your notebook.

## Creating the inference stack

- From Jupyter notebook run the following commands:
  - `! cd ../ && python create-inference-stack.py TRAINING_JOB_NAME ENV_NAME`
- From terminal:
  - cd into the root directory
  - run the following command:
    - `python create-inference-stack.py TRAINING_JOB_NAME ENV_NAME`
- example command:
  `python create-inference-stack.py 'tuning16-21-13-002-b81f1153' 'sghidro'`
- The first argument is the name of a valid training job
- The second argument is any environment name of your choosing

## Using the JupyterLab IDE

- Git commands can be made by:
  - using the git client in the left hand tool bar
  - using the command line by going to: Launcher > Other > Terminal

### What does the developer stack do?

- Creates an S3 bucket used to store data for processing, and the generated models.
- Creates a code CodeRepository, which is a configuration of where the default repository is located and what secrets manager to use for git commands. Defaults are provided, but they can me modified.
- Creates a SageMaker Jupyter notebook.
- Creates an IAM role which gives the notebook access to certain AWS resources. This is defined by the following managed policies: `arn:aws:iam::aws:policy/AmazonSageMakerFullAccess`, `arn:aws:iam::aws:policy/AmazonS3FullAccess`
- Creates a secret for access to the git code repository.
- Associates the secret with the git code repository.
- Associates the provided git code repository with the notebook. This will be checked out to the root of the Jupyter notebook directory. Access is already granted through a secrets manager record, and once inside the Jupyter lab the developer can push and pull code using the built in git client.
