DOCKER=docker-compose -f docker-compose.yml
SOURCE_FILES = *.py

docker-up:
	$(DOCKER) up

init:
	cp .env.aws-credentials.sample .env.aws-credentials
	cp .env.slack_token.sample .env.slack_token
	
set_token:
	$(DOCKER) run sls sh set_token.sh

sls:
	$(DOCKER) run sls ${p}

deploy:
	$(DOCKER) run sls sls deploy

remove:
	$(DOCKER) run sls sls remove
