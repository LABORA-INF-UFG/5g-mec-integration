app_name = service-registry
tag = 1.0
build:
	docker build -t $(app_name):$(tag) .
	docker save $(app_name):$(tag) | bzip2 | ssh root@10.16.10.26 'bunzip2 | docker load'
run:
	docker run --name $(app_name):$(tag) -p 8000:8000 $(app_name)

kill:
	kubectl delete deployment $(app_name)
	docker rmi -f $(app_name):$(tag)

deploy:
	kubectl apply -f service-registry-deploy.yaml
