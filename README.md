# Intent of the Mini Task (Deploy a Simple Hello-World App to Minikube)

Deploy a simple hello-world service (Python/Flask or Node.js) to Minikube, expose it via a Service, and access it locally

The intent is hands-on learning — to make you *apply* Kubernetes and EKS concepts in a safe, local, low-cost environment.    
It turns abstract ideas (“Pods,” “Deployments,” “Services,” etc.) into concrete actions you can see working.

All files and commmands are provided in the `flask-k8s` folder to create a reachable service in minutes`


## Learning objective:


### Understand Kubernetes workflow end-to-end
By building and deploying even a tiny app (Flask/Node.js) you touch every major step in the Kubernetes lifecycle:

1. Writing an application.
2. Containerizing it (Dockerfile → image).
3. Creating Kubernetes manifests (Deployment + Service).
4. Deploying with `kubectl apply`.
5. Inspecting and debugging Pods (`kubectl get/describe/logs`).
6. Exposing the app locally (`minikube service`, `port-forward`).

This mirrors exactly what you’ll do later in real clusters (like AWS EKS), but with zero cloud cost or complexity.


### Learn the foundational Kubernetes objects
The mini task teaches how these objects interact:

- **Pod** → runs your app container.
- **Deployment** → ensures desired number of Pods are running (self-healing, rolling updates).
- **Service** → exposes Pods under a stable name/IP, handling load-balancing inside the cluster.
- **kubectl** → your main control plane interface.

After this, you’ll intuitively understand what a Pod, Deployment, and Service are—not just in theory but by seeing them live.


### Practice essential kubectl operations
You’ll use commands like:

- `kubectl get pods`
- `kubectl logs`
- `kubectl describe`

These are the **core diagnostic** tools every Kubernetes engineer uses daily.    
The mini task gives you a sandbox to safely break things and learn how to fix them.


### Bridge to AWS EKS
The goal isn’t just to run “Hello World.”    
It’s to simulate what you’ll later do on EKS, but locally:

- You build the same Docker image.
- You apply the same YAML manifests.
- You use the same `kubectl` workflow.

Then, once you move to AWS EKS, the steps are nearly identical—only the cluster creation and access differ.

The mini task provides a risk-free rehearsal for deploying apps to EKS.


### Confidence through iteration
You’ll learn by doing, observing, and debugging:

- Watch Pods spin up.
- Check logs to confirm the app is running.
- Access it via URL (`minikube service …`).

That visual, tangible feedback cements understanding far faster than reading docs alone.

