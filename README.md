# Intent of the Mini Task (Deploy a Simple Hello-World App to Minikube)

The intent is hands-on learning — to make you *apply* Kubernetes and EKS concepts in a safe, local, low-cost environment.    
It turns abstract ideas (“Pods,” “Deployments,” “Services,” etc.) into concrete actions you can see working.

Let’s break it down by learning objective:


## Understand Kubernetes workflow end-to-end
By building and deploying even a tiny app (Flask/Node.js):

- You touch every major step in the Kubernetes lifecycle:
 1. Writing an application.
 2. Containerizing it (Dockerfile → image).
 3. Creating Kubernetes manifests (Deployment + Service).
 4. Deploying with `kubectl apply`.
 5. Inspecting and debugging Pods (`kubectl get/describe/logs`).
 6. Exposing the app locally (`minikube service`, `port-forward`).

This mirrors exactly what you’ll do later in real clusters (like AWS EKS), but with zero cloud cost or complexity.


## Learn the foundational Kubernetes objects

The mini task teaches how these objects interact:

Pod → runs your app container.

Deployment → ensures desired number of Pods are running (self-healing, rolling updates).

Service → exposes Pods under a stable name/IP, handling load-balancing inside the cluster.

kubectl → your main control plane interface.

After this, you’ll intuitively understand what a Pod, Deployment, and Service are—not just in theory but by seeing them live.

3. Practice essential kubectl operations

You’ll use commands like:

kubectl get pods

kubectl logs

kubectl describe
These are the core diagnostic tools every Kubernetes engineer uses daily.
The mini task gives you a sandbox to safely break things and learn how to fix them.

4. Bridge to AWS EKS

The goal isn’t just to run “Hello World.”
It’s to simulate what you’ll later do on EKS, but locally:

You build the same Docker image.

You apply the same YAML manifests.

You use the same kubectl workflow.

Then, once you move to AWS EKS, the steps are nearly identical—only the cluster creation and access differ.

So, the mini task provides a risk-free rehearsal for deploying apps to EKS.

5. Confidence through iteration

You’ll learn by doing, observing, and debugging:

Watch Pods spin up.

Check logs to confirm the app is running.

Access it via URL (minikube service …).
That visual, tangible feedback cements understanding far faster than reading docs alone.


**Edit a file, create a new file, and clone from Bitbucket in under 2 minutes**

When you're done, you can delete the content in this README and update the file with details for others getting started with your repository.

*We recommend that you open this README in another tab as you perform the tasks below. You can [watch our video](https://youtu.be/0ocf7u76WSo) for a full demo of all the steps in this tutorial. Open the video in a new tab to avoid leaving Bitbucket.*

---

## Edit a file

You’ll start by editing this README file to learn how to edit a file in Bitbucket.

1. Click **Source** on the left side.
2. Click the README.md link from the list of files.
3. Click the **Edit** button.
4. Delete the following text: *Delete this line to make a change to the README from Bitbucket.*
5. After making your change, click **Commit** and then **Commit** again in the dialog. The commit page will open and you’ll see the change you just made.
6. Go back to the **Source** page.

---

## Create a file

Next, you’ll add a new file to this repository.

1. Click the **New file** button at the top of the **Source** page.
2. Give the file a filename of **contributors.txt**.
3. Enter your name in the empty file space.
4. Click **Commit** and then **Commit** again in the dialog.
5. Go back to the **Source** page.

Before you move on, go ahead and explore the repository. You've already seen the **Source** page, but check out the **Commits**, **Branches**, and **Settings** pages.

---

## Clone a repository

Use these steps to clone from SourceTree, our client for using the repository command-line free. Cloning allows you to work on your files locally. If you don't yet have SourceTree, [download and install first](https://www.sourcetreeapp.com/). If you prefer to clone from the command line, see [Clone a repository](https://confluence.atlassian.com/x/4whODQ).

1. You’ll see the clone button under the **Source** heading. Click that button.
2. Now click **Check out in SourceTree**. You may need to create a SourceTree account or log in.
3. When you see the **Clone New** dialog in SourceTree, update the destination path and name if you’d like to and then click **Clone**.
4. Open the directory you just created to see your repository’s files.

Now that you're more familiar with your Bitbucket repository, go ahead and add a new file locally. You can [push your change back to Bitbucket with SourceTree](https://confluence.atlassian.com/x/iqyBMg), or you can [add, commit,](https://confluence.atlassian.com/x/8QhODQ) and [push from the command line](https://confluence.atlassian.com/x/NQ0zDQ).
