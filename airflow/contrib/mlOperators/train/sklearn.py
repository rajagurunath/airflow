"""
Train Base class inherits airflow baseoperator to display the task in 
airflow UI

- Train Operator should log the metrics in mlflow UI
- Saves the model in reproducible manner
- Trains the model with different hyperparamaters and display the same in Mlflow ui
- Share implementation with nni (for automl)

"""

from airflow.operators.base_opertor import BaseOperator
from airflow.utils.decorators import apply_defaults

#from skearn.linear_model import LogisticRegression


class MLTrainBaseOperator(BaseOperator):
    """
    Base class for all ml training operators
    This class expected to implement following things

    Integeration with mlflow or nnictl (Depending up on the user config)
    Integeration with Message queues or using any persistant DBs  to get the 
        training data
    Implement one operator for one algorithm or framework (yet to be decided)
    """
    @apply_defaults
    def __init__(self,config,mlflowClient):
        self.mlflowClient=mlflowClient
        self.config=config

    def execute(self):
        pass
    def log_model(self):
        pass

    def nnictl(self):
        pass
    








