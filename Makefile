.PHONY: init build push test run drun deploy redeploy

init:
	$(info Installing dependencies...)
	pip install -r requirements.txt

build:
	$(info Building Docker image...)
	docker build --rm -t hitcounter:1.0 . 

push:
	$(info Building Docker image...)
	docker tag hitcounter:1.0 localhost:32000/hitcounter:1.0
	docker push localhost:32000/hitcounter:1.0

test:
	$(info Running tests...)
	nosetests --with-spec --spec-color

run:
	$(info Starting service locally...)
	gunicorn --bind 0.0.0.0:5000 service:app

drun:
	$(info Starting service in Docker...)
	docker run --rm -p 5000:5000 --link redis -e DATABASE_URI="redis://redis:6379" hitcounter:1.0

deploy:
	$(info Deploying to Kubernetes...)
	kubectl apply -f deploy/redis.yaml
	kubectl apply -f deploy/secrets.yaml
	kubectl apply -f deploy/deployment.yaml
	kubectl apply -f deploy/service.yaml
	kubectl apply -f deploy/ingress.yaml

redeploy:
	$(info Redeploying to Kubernetes...)
	kubectl delete --ignore-not-found=true -f deploy/deployment.yaml
	kubectl create -f deploy/deployment.yaml
