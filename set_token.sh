#!/bin/sh

aws ssm put-parameter --name "/slack-bot-anonymous-demo/slack_bot_user_access_token" --value $SLACK_BOT_USER_ACCESS_TOKEN --type SecureStrin
aws ssm put-parameter --name "/slack-bot-anonymous-demo/slack_app_auth_token" --value $SLACK_APP_AUTH_TOKEN --type SecureStrin