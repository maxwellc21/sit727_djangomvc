# 🚀 SIT727 Cloud Automation Technology  
### *Cloud-Native Apps with Django, Docker & Kubernetes*  

![Banner](https://via.placeholder.com/1200x400/326CE5/FFFFFF?text=Docker+K8s+Django+Automation)  

---

## 🌟 **Welcome**  
A full-stack cloud automation demo using **Python (Django), Node.js, HTML, Docker, and Kubernetes**. Deploy locally (Minikube) or on any cloud provider!  

---

## 🛠️ **Tech Stack**  
| **Role**            | **Tools**                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Backend              | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-339933?logo=node.js&logoColor=white) |
| Frontend             | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) |
| Infrastructure       | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white) |

---

## 🚀 **Quick Start**  

### **Prerequisites**  
- Docker ([Install](https://docs.docker.com/get-docker/))  
- Kubernetes/Minikube ([Install](https://minikube.sigs.k8s.io/docs/start/))  
- Python 3.8+ & Node.js  

---

## 🐋 **1. Docker Setup**  

### **Build Docker Image**  
```bash
docker build -t djangomvc-app:latest .
```
##🐋 **2. Push to DockerHub**  
```bash
docker tag djangomvc-app:latest yourusername/djangomvc-app:latest  
docker push yourusername/djangomvc-app:latest
```
## ☸️ **3. Kubernetes Deployment
###  **Deploy to Minikube/Cloud**
```bash
kubectl create deployment djangomvc --image=djangomvc-app:latest
````
###  **Expose the Service**
#### **For Cloud (LoadBalancer**
```bash
kubectl expose deployment djangomvc --type=LoadBalancer --port=8000
````
#### **For For Minikube (NodePort)r**
```bash
kubectl expose deployment djangomvc --type=NodePort --port=8000
````
###  **Access the Application**
#### **For Cloud (LoadBalancer**
```bash
kubectl get services  # Use the EXTERNAL-IP
````
#### **For For Minikube (NodePort)r**
```bash
minikube service djangomvc
````
###  **Deploy to Minikube/Cloud**
```bash
kubectl create deployment djangomvc --image=djangomvc-app:latest
````
## 🔍 **4. Verify Deployment**
```bash
kubectl get pods
kubectl get services
```
