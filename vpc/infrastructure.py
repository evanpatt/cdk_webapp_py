from constructs import Construct
from aws_cdk import aws_ec2 as ec2 

class Vpc(Construct):

    @property
    def vpc(self):
        return self._vpc

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._vpc = ec2.Vpc(self, "VPC",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(cidr_mask=24,name="Ingress",subnet_type=ec2.SubnetType.PUBLIC),
                ec2.SubnetConfiguration(cidr_mask=24,name="Application",subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT),
                ec2.SubnetConfiguration(cidr_mask=24,name="Database",subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
                ]
            )
        # TODO: add security groups for services?
