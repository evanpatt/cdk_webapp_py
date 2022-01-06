from constructs import Construct
from aws_cdk import RemovalPolicy, aws_ec2 as ec2, aws_rds as rds

class Rds(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._rds = rds.DatabaseInstance(
            self,
            "RDS",
            database_name="db1",
            engine=rds.DatabaseInstanceEngine.MYSQL,
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.MICRO
            ),
            removal_policy=RemovalPolicy.DESTROY,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
            deletion_protection=False
        )

        # TODO: assign instance to private isolated subnet in VPC
        # TODO: create security groups to access DB (or in VPC?)
