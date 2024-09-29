import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/anujahlawat.ds/06-learning-mlops-mini-project.mlflow")
dagshub.init(repo_owner='anujahlawat.ds', repo_name='06-learning-mlops-mini-project', mlflow=True)


with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)