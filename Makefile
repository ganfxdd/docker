include .env

.DEFAULT_GOAL=build

# ENVごとにコマンドやcomposeファイル使い分けたい時に使う
#ifeq ($(FLASK_ENV), production)
#	DC = COMPOSE_FILE=docker-compose.production.yml docker-compose
#else
#    ifeq ($(PROJECT_ENV), test)
#        DC = COMPOSE_FILE=docker-compose.test.yml docker-compose
#    else
#        DC = PROJECT_ENV=docker-compose.development.yml docker-compose
#    endif
#endif
#project_env_check:
#	@$(eval PROJECT_ENV := $(shell read -p "ENV? (prd or stg): " ENV; echo $$ENV))
#	@echo "run command in $(PROJECT_ENV)"

DC = docker-compose

APP = docker-compose exec app
FLASK = $(APP) flask

CD_NGINX = cd .docker/nginx
CD_REDIS = cd .docker/redis


# コンテナ操作コマンド
.PHONY: build up build_up restart force_restart down logs clean test
build:
	$(DC) build
up:
	$(DC) up -d
build_up:
	$(DC) up -d --build
restart:
	$(DC) restart
force_restart:
	@make down
	@make build_up
down:
	$(DC) down
logs:
	$(DC) logs -f
clean:
	@docker image prune
	@docker volume prune
test:
	$(APP) pytest

# DB関連コマンド
.PHONY: db_migrate db_upgrade db_downgrade
db_migrate:
	@$(FLASK) db migrate
db_upgrade:
	@$(FLASK) db upgrade
db_downgrade:
	@$(FLASK) db downgrade
