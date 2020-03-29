import boto3
import sys
sm = boto3.client("sagemaker")
cf = boto3.client("cloudformation")

trainingJobName = sys.argv[1]
env_name = sys.argv[2]

job = sm.describe_training_job(TrainingJobName=trainingJobName)
trainingImage = job['AlgorithmSpecification']['TrainingImage']
modelDataUrl = job['ModelArtifacts']['S3ModelArtifacts']
roleArn = job['RoleArn']
stack_name = env_name + "-inference"

print('Job name: ' + trainingJobName)
print('trainingImage: ' + trainingImage)
print('modelDataUrl: ' + modelDataUrl)
print('roleArn: ' + roleArn)
print('stack_name: ' + stack_name)

with open("inference.yml", "r") as f:
    stack = cf.create_stack(StackName=stack_name,
                            TemplateBody=f.read(),
                            Parameters=[
                                {"ParameterKey": "EnvName",
                                    "ParameterValue": env_name},
                                {"ParameterKey": "ModelName",
                                    "ParameterValue": trainingJobName},
                                {"ParameterKey": "TrainingImage",
                                    "ParameterValue": trainingImage},
                                {"ParameterKey": "ModelDataUrl",
                                    "ParameterValue": modelDataUrl},
                                {"ParameterKey": "RoleArn",       "ParameterValue": roleArn}])
print(stack)
