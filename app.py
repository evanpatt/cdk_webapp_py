#!/usr/bin/env python3
import os

from aws_cdk import App

import constants

from deployment import WebAppInfrastructure


app = App()

WebAppInfrastructure(
    app,
    f"{constants.CDK_APP_NAME}-Dev",
    env=constants.DEV_ENV,
)

# TODO: create a Pipeline for deployment?

app.synth()
