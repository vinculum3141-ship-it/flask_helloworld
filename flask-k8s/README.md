# Step-by-step commands (run in a terminal)

1. Start Minikube
```
minikube start
minikube status
```
This creates a local Kubernetes single-node cluster. 


2. Build the Docker image inside Minikube’s Docker (so you don’t need to push to a registry)
```
eval $(minikube -p minikube docker-env)
docker build -t hello-flask:0.1 .
# verify: docker images | grep hello-flask
```
This points your shell’s docker to Minikube’s Docker daemon so the image is directly available. 

Alternatively,
```
# from your project dir
minikube image build -t hello-flask:0.1 .
```
This option is a useful alternative that builds an image for the Minikube node. 


3. Deploy to Kubernetes
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```


4. Check status
```
kubectl get deployments
kubectl get pods
kubectl get svc
```
You should see `hello-flask` deployment with 2 replicas and Pod(s) in `Running` state.


4. Inspect logs / debug
```
kubectl get pods
kubectl logs -f <one-pod-name>
kubectl describe pod <one-pod-name>
```
If a Pod is `CrashLoopBackOff`, `kubectl describe` shows events, and `kubectl logs` shows the container output.


6. Access the service locally
A Quick method (minikube will print a URL and open browser if you want):
```
minikube service hello-flask --url
# example output: http://192.168.49.2:32000  (open in browser or curl)
```
`minikube service` is the easiest local way to reach NodePort/LoadBalancer services. 
minikube

Alternate: port-forward to local machine:
```
kubectl port-forward svc/hello-flask 5000:5000
# then visit http://localhost:5000
```

**Expected quick check:**
```
kubectl get pods
# NAME                             READY  STATUS   RESTARTS   AGE
# hello-flask-xxxxx-xxxxx         1/1    Running  0          1m
```
```
curl $(minikube service hello-flask --url)
# Hello from Flask on Kubernetes (Minikube)!
```


7. Clean up
```
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
# optionally stop minikube
minikube stop
```

# Tips & troubleshooting (common issues)

* **Pod never starts / CrashLoopBackOff**: `kubectl describe pod <pod>` → check Events; `kubectl logs <pod>` → read stdout/stderr. 
* **Image not found**: you built the image in your host Docker but Minikube is using its own Docker — run `eval $(minikube docker-env)` or `minikube image build`. See Minikube docs on pushing/building images. 
* **Service unreachable**: check `kubectl get svc` for `TYPE` and `PORT(S)`; use `minikube service <svc> --url` or `kubectl port-forward`. For `LoadBalancer` type locally, run `minikube tunnel` in a separate terminal to get an external IP. 
* **Want to inspect cluster UI**: `minikube dashboard` opens the Kubernetes dashboard.
