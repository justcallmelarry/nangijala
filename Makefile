.SILENT:

SERVICE_NAME := nangijala
IMAGE_NAME := nangijala
CONFIG_DATA := $(shell cat config.toml 2>/dev/null || cat config.example.toml 2>/dev/null)

help:
	@echo "Commands:               |"
	@echo "  $$ make build          | build development image"
	@echo "  $$ make dev            | run development image in container"
	@echo "  $$ make release        | build and start"

image:
	[ "$$(docker images ${IMAGE_NAME}:dev -q)" ] || ${MAKE} build

build:
	docker build -t ${IMAGE_NAME}:dev --target development .

dev: image
	docker run --rm -it -p 5500:80 \
		-v ${PWD}/src:/src:cached \
		-v ${PWD}/logs:/logs \
		-e NANGIJALA_CONFIG='$(call quotestr,$(CONFIG_DATA))' \
		--name ${SERVICE_NAME} ${IMAGE_NAME}:dev

build-release:
	docker build -t ${IMAGE_NAME}:latest --target release .

release:
	build-release
	docker stop ${SERVICE_NAME} 2> /dev/null
	docker run --rm -it -p 5500:80 \
		-v ${PWD}/src:/src:cached \
		-v ${PWD}/logs:/logs \
		-e NANGIJALA_CONFIG='$(call quotestr,$(CONFIG_DATA))' \
		--name ${SERVICE_NAME} ${IMAGE_NAME}:latest
