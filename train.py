import os
import mlflow
from mlflow import log_metric, log_param, log_artifact

os.environ["AWS_ACCESS_KEY_ID"] = "admin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "adminadmin"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://192.168.1.111:9000"

if __name__ == '__main__':
    mlflow.set_experiment("Default")
    mlflow.set_tracking_uri('http://192.168.1.111:5000')

    log_param('param1', 15)
    log_param('param2', 25)
    log_param('param3', 35)
    log_param('param4', 5)
    log_param('param5', 55)


    log_metric('foo', 1)
    log_metric('foo', 2)
    log_metric('foo', 4)
    log_metric('foo', 6)
    log_metric('foo', 8)

    with open('wine.mdl', 'w') as f:
        f.write('hello, mlops.')
    log_artifact('wine.mdl')
