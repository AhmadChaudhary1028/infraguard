# 🛡️ InfraGuard — DevSecOps Platform

A production-grade DevSecOps platform built with modern DevOps tools.

## 🏗️ Architecture

- **Flask API** — REST application with health & metrics endpoints
- **Docker** — Multi-stage containerization
- **GitHub Actions** — CI/CD pipeline with Trivy security scanning
- **Kubernetes** — 3-environment deployment (dev/staging/prod)
- **Nginx Ingress** — Traffic routing across environments
- **Prometheus + Grafana** — Full observability stack
- **Terraform** — Infrastructure as Code

## 🚀 Tech Stack

| Tool | Purpose |
|------|---------|
| Python/Flask | Application |
| Docker | Containerization |
| GitHub Actions | CI/CD Pipeline |
| Trivy | Security Scanning |
| Kubernetes | Orchestration |
| Helm | Package Management |
| Prometheus | Metrics Collection |
| Grafana | Monitoring Dashboard |
| Terraform | Infrastructure as Code |

## 📦 Project Structure
## 🔐 CI/CD Pipeline

Every push to main triggers:
1. Docker image build
2. Trivy security scan (CRITICAL/HIGH vulnerabilities)
3. Push to DockerHub
4. Deploy to Kubernetes

## 📊 Monitoring

- Prometheus scrapes metrics from all pods
- Grafana dashboard shows real-time cluster health
- Endpoints: `/health`, `/ready`, `/metrics`

## 👤 Author

Ahmad Chaudhary — DevOps Engineer
