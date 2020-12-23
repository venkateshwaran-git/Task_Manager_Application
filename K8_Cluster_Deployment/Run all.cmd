kubectl apply -f redis-deployment.yaml
kubectl create -f redis-service.yaml

kubectl apply -f mongo-deployment.yaml
kubectl create -f mongo-service.yaml


cd Flask/k8s
kubectl apply -f Flask-Deployment.yaml
kubectl create -f Flask-Service.yaml

cd..
cd..

cd React/k8s
kubectl apply -f React-Deployment.yaml
kubectl create -f React-Service.yaml

cd..
cd..

cd Python/k8s
kubectl apply -f backend-Deployment.yaml
kubectl create -f backend-Service.yaml



PAUSE