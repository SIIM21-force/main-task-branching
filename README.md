# 🚀 Containerized DevOps Status Microservice

![CI Pipeline](https://github.com/SIIM21-force/main-task-branching/actions/workflows/ci.yml/badge.svg)
![Release](https://img.shields.io/badge/release-v1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-brightgreen.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)

This repository demonstrates enterprise **Git version control workflows**, branching strategies, automated CI/CD with GitHub Actions, and containerization.

---

## 📌 Project Overview
A containerized Python Flask REST API featuring system health monitoring, automated unit testing, container build verification, and continuous integration.

### API Endpoints
| Endpoint | Method | Description | Sample Response |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | Service & environment information | `{"service": "DevOps Health & Monitoring API", "version": "1.0.0", "status": "operational"}` |
| `/health` | `GET` | Health check probe for uptime monitoring | `{"status": "healthy", "uptime": "active"}` |
| `/system` | `GET` | Host OS and runtime platform metadata | `{"operating_system": "Linux", "python_version": "3.11.x"}` |

---

## 🌿 Git Branching Strategy & Workflow

We adopted the **Feature Branch Workflow** integrated with automated CI quality gates:

```
[main] (Production - Tagged v1.0.0)
  ▲
  └── PR #4: Merge dev into main (Release v1.0.0)
        ▲
      [dev] (Staging / Integration)
        ▲
        ├── PR #1: feature/api-service (Flask API + unit tests)
        ├── PR #2: feature/docker-setup (Dockerfile + .dockerignore)
        └── PR #3: feature/ci-pipeline (GitHub Actions CI workflow)
```

### Branch Roles
1. **`main`**: Production-ready, stable code. Commits arrive exclusively through reviewed Pull Requests from `dev` and are marked with release tags (`v1.0.0`).
2. **`dev`**: Integration branch for ongoing development. All feature branches merge here first and run automated CI checks before promotion to `main`.
3. **`feature/*`**: Short-lived branches dedicated to individual tasks (`feature/api-service`, `feature/docker-setup`, `feature/ci-pipeline`).

---

## 📋 Task Execution & Workflow Documentation

This section documents the step-by-step completion of all requirements:

### 1. Initialize repo and push to GitHub
1. Initialized the local Git repository:
   ```powershell
   git init
   ```
2. Connected the remote GitHub repository:
   ```powershell
   git remote add origin https://github.com/SIIM21-force/main-task-branching.git
   ```
3. Created initial commit on `main` and pushed upstream:
   ```powershell
   git branch -M main
   git add .gitignore README.md
   git commit -m "chore: initial repo setup"
   git push -u origin main
   ```

### 2.  Create `dev`, `feature`, and `main` branches
1. Created and published the `dev` integration branch:
   ```powershell
   git checkout -b dev
   git push -u origin dev
   ```
2. Created isolated feature branches off `dev`:
   - `git checkout -b feature/api-service` (Core Flask API & unit tests)
   - `git checkout -b feature/docker-setup` (Dockerfile and container configuration)
   - `git checkout -b feature/ci-pipeline` (GitHub Actions automated testing)

### 3. Use Pull Requests to merge
Direct pushes to `dev` and `main` were restricted; all merges were executed via GitHub Pull Requests:
- **PR #1 (`feature/api-service` $\rightarrow$ `dev`)**: Added Flask REST API, requirements, and unit test suite.
- **PR #2 (`feature/docker-setup` $\rightarrow$ `dev`)**: Added multi-stage `Dockerfile` and `.dockerignore`.
- **PR #3 (`feature/ci-pipeline` $\rightarrow$ `dev`)**: Added GitHub Actions workflow (`ci.yml`) to automatically test PRs.
- **PR #4 (`dev` $\rightarrow$ `main`)**: Release v1.0.0 promoting tested code into production.

### 4. Add a proper `README.md`
Created this comprehensive `README.md` covering architecture, branch workflow diagrams, execution instructions, task tracking, and interview questions.

### 5. Use `.gitignore` and tags
1. **`.gitignore`**: Configured to exclude Python bytecache (`__pycache__/`, `*.pyc`), virtual environments (`venv/`), secrets (`.env`), package directories (`node_modules/`), and reference assignment PDFs.
2. **Git Tags**: Created and pushed an annotated semantic tag on `main` for release `v1.0.0`:
   ```powershell
   git checkout main
   git pull origin main
   git tag -a v1.0.0 -m "Release v1.0.0: Containerized health check API with CI pipeline"
   git push origin v1.0.0
   ```

---

## 📊 Git Commit Graph Verification

Output of `git log --all --graph --oneline --decorate` verifying the completed branch lifecycle:

```text
*   4fe1db7 (HEAD -> main, tag: v1.0.0, origin/main, origin/HEAD) Merge pull request #4 from SIIM21-force/dev
|\  
| *   afef541 (origin/dev) Merge pull request #3 from SIIM21-force/feature/ci-pipeline
| |\  
| | * 67f3597 (origin/feature/ci-pipeline, feature/ci-pipeline) ci: add GitHub Actions workflow for automated testing
| |/  
| *   88820a2 (dev) Merge pull request #2 from SIIM21-force/feature/docker-setup
| |\  
| | * 51929c7 (origin/feature/docker-setup, feature/docker-setup) chore: add Dockerfile and .dockerignore for containerization
| |/  
| * 2141b0b Merge pull request #1 from SIIM21-force/feature/api-service
|/| 
| * 561f11b (origin/feature/api-service, feature/api-service) feat: add Flask health monitoring microservice and unit tests
|/  
* 20c19c0 chore: initial repo setup
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

The workflow file `.github/workflows/ci.yml` runs on every push and PR to `main` and `dev`:
1. Checks out repository source code via `actions/checkout@v4`.
2. Configures Python 3.11 via `actions/setup-python@v5` with pip caching.
3. Installs dependencies from `requirements.txt`.
4. Executes unit tests: `python -m unittest test_app.py`.
5. Builds container image: `docker build -t devops-flask-app:ci .` to ensure deployment readiness.

---

## 🛠️ Local Setup & Execution

### Running Locally with Python
```powershell
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run automated tests
python -m unittest test_app.py

# Start application
python app.py
```

### Running with Docker / Podman
```powershell
# Build container image
podman build -t devops-flask-app .

# Run container
podman run -d -p 5000:5000 --name flask-app devops-flask-app

# Verify health check
curl http://127.0.0.1:5000/health

# If 5000 exposed port doesn't work, choose another port, like 8090 for example below
podman run -d -p 8090:5000 --name flask-app devops-flask-app
```

---
