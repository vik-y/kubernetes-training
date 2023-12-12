# Setup Environment 

Minikube should be installed on your virtual machine already. Ensure it is working. 
```
❯ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

## Install all required packages 
```
wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubens
chmod +x kubens
wget https://github.com/ahmetb/kubectx/releases/download/v0.9.5/kubectx
chmod +x kubectx 
sudo mv kubens kubectx /usr/local/bin
```



