.SILENT:

SERVICE_NAME:=nangijala
IMAGE_NAME:=nangijala

help:
	@echo "Commands:               |"
	@echo "  $$ make build          | build development image"
	@echo "  $$ make dev            | run development image in container"
	@echo "  $$ make release        | build and start "

build:
	docker build -t ${IMAGE_NAME}:dev --target development .

dev:
	docker run --rm -it -p 5500:80 \
		-v ${PWD}/src:/src:cached \
		-v ${PWD}/logs:/logs \
		--name ${SERVICE_NAME} ${IMAGE_NAME}:dev

build-release:
	docker build -t ${IMAGE_NAME}:latest --target release .

release:
	build-release
	docker stop ${SERVICE_NAME} 2> /dev/null
	docker run --rm -it -p 5500:80 \
		-v ${PWD}/src:/src:cached \
		-v ${PWD}/logs:/logs \
		--name ${SERVICE_NAME} ${IMAGE_NAME}:latest
