## Get the IP and port of registry 
```
$ docker ps | grep 5000  
0bb3f7c28b42   gcr.io/k8s-minikube/kicbase:v0.0.42   "/usr/local/bin/entr…"   2 hours ago   Up 2 hours   127.0.0.1:52399->22/tcp, 127.0.0.1:52400->2376/tcp, 127.0.0.1:52402->5000/tcp, 127.0.0.1:52403->8443/tcp, 127.0.0.1:52401->32443/tcp   minikube
```
From the above output we see that 127.0.0.1:52402 is mapping to port 5000 on the minikube VM. So that's our registry address.

REGISTRY_ADDRESS=127.0.0.1:52402
docker tag vikasy/pod-checker-demo ${REGISTRY_ADDRESS}/pod-checker-demo
docker push ${REGISTRY_ADDRESS}/pod-checker-demo