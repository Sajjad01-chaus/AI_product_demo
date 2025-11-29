# AI Platform Demo – Training → Storage → Inference on Kubernetes

This repository demonstrates a simplified end-to-end workflow for an AI workload:
**training a model → saving artifacts → deploying an inference API on Kubernetes.**

It is designed for AI/ML engineers and AI PMs who want to understand the practical
steps involved without setting up a full production Kubernetes environment.

---

## 🚀 Architecture Overview

**High-level flow:**

1. **Training Stage**
   - A simple HuggingFace model is saved locally using `train.py`.
   - A Kubernetes `Job` is provided (`training-job.yaml`).

2. **Storage Stage**
   - The model is stored inside the container image or uploaded manually to object storage (S3/MinIO).  
   - This simulates storing trained model artifacts.

3. **Inference Stage**
   - A FastAPI-based inference server loads a HuggingFace pipeline.
   - A Kubernetes `Deployment` + `Service` exposes the API.

---

## 📁 Repository Structure

training/
├── train.py
└── training-job.yaml
inference/
├── inference_server.py
├── requirements.txt
├── Dockerfile
└── deployment.yaml
architecture-diagram.png


---

## 🛠 Tech Used

- Python 3.10  
- FastAPI  
- HuggingFace Transformers  
- Docker  
- Kubernetes (Deployment + Service + Job)  

This mirrors **real-world AI workflows** in a simplified, beginner-friendly way.

---

##  How to Run Locally
```
### Training


cd training
python train.py


### Build Inference Image


cd inference
docker build -t simple-inference.


### Run Inference API Locally


uvicorn inference_server:app --host 0.0.0.0 --port 8000


### Deploy to Kubernetes


kubectl apply -f inference/deployment.yaml

```
---

## 📌 Why This Repo 

```
This repo is created as an **AI Product Manager ** to show:

- Understanding of model lifecycle  
- Ability to reason about K8s workloads  
- Practical AI engineering skills  
- Clean documentation and infra awareness  

---
