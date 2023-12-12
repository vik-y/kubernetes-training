---
marp: true
---
<!-- header: Kubernetes Session -->
# Introduction 

What is Kubernetes?

--> This intro is going to be very different from any that you might have ever had 

---
# Introduction 

What is Kubernetes?

- When people start about introducing kubernetes, they say
	- It's an orchestration tool 
	- It's a cluster 
	- It's an automation tool 
	- It was made by google, 
	- etc. etc. etc. 
	- What I will start with - is a simple python application. 
---

Why Kubernetes ?
- let's start with a simple django app example 
- You run locally  : python manage.py runserver 
- Now , you want to deploy it 
	- Options
		- VM 
			- with container
			- without container 
	- You configure your webserver to route traffic 
	- and you're pretty much done 

- Now you have 100 django applications
	- Provision 100 vms
	- Manage config of those vms using a config management tool or manually 
	- Configure web server to route traffic to each of those 
	- Configure SSL for each of these 100 apps and write tooling to manage cert lifecycle 
	- Write tooling to manage operations of these applications 

- Enter Kubernetes 
	- Take 50-60 virtual machines ( why lower number? We'll see at the end) 
	- Build a kubernetes cluster on top of those 
	- Containerise each of application and push the images to a registry 
	- Write yaml definition of your application 
	- Submit the yaml to kubernetes and let it take care of everything else 
- What will K8 take care of? 
	- Deploy your application on the VMs wherever it finds capacity 
	- Auto configure web server and route the incoming traffic to the correct application based on host header or suburl 
	- Manage lifecycle of each application - like helath monitoring, auto-restarting, alerting, health probes, metrics, etc. 
	- Manage SSL configuration and lifecycle - this is not offered in core Kubernetes but community has utilities for these. 

---
