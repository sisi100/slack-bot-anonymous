import boto3

CLIENT = boto3.client("ssm")
SSM_PREFIX = "/slack-bot-anonymous-demo"

SSM_PARAMETERS = ["slack_bot_user_access_token", "slack_app_auth_token"]


resources_key = [f"{SSM_PREFIX}/{i}" for i in SSM_PARAMETERS]

response = CLIENT.get_parameters(Names=resources_key, WithDecryption=True)

resources_parameter = {}
for i, value in enumerate(SSM_PARAMETERS):
    resources_parameter[value] = response["Parameters"][i]["Value"]


USER_ACCESS_TOKEN = resources_parameter["slack_bot_user_access_token"]
APP_AUTH_TOKEN = resources_parameter["slack_app_auth_token"]
