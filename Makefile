IMAGE_NAME=carmelar15/calculadora
TAG=latest

build:
	docker build -f Dockerfile.run -t $(IMAGE_NAME):$(TAG) .

run:
	docker run -it --rm -v "$(PWD)/logs:/app/logs" $(IMAGE_NAME):$(TAG)

test:
	docker build -f Dockerfile -t $(IMAGE_NAME)-test .
	docker run --rm $(IMAGE_NAME)-test

login:
	@export $$(grep -v '^#' .env | xargs) && echo $$DOCKER_TOKEN | docker login -u carmelar15 --password-stdin



push:
	docker push $(IMAGE_NAME):$(TAG)

deploy:
	make build
	make login
	make push

release:
	@if [ -z "$(v)" ]; then \
		echo "❌ Debes pasar una versión con: make release v=1.0"; \
		exit 1; \
	fi
	@echo "🚀 Construyendo y etiquetando versión $(v)..."
	docker build -f Dockerfile.run -t $(IMAGE_NAME):$(v) -t $(IMAGE_NAME):latest .
	@export $$(grep -v '^#' .env | xargs) && echo $$DOCKER_TOKEN | docker login -u carmelar15 --password-stdin
	docker push $(IMAGE_NAME):$(v)
	docker push $(IMAGE_NAME):latest
	@echo "✅ Imagen subida como $(IMAGE_NAME):$(v) y latest"

