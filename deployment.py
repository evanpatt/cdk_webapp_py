from constructs import Construct
from aws_cdk import Stage, Stack
from vpc.infrastructure import Vpc
from rds.infrastructure import Rds

class WebAppInfrastructure(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stateful = Stack(self, "Stateful")
        _vpc = Vpc(stateful, "Network")
        _rds = Rds(stateful, "Database", _vpc.vpc)
