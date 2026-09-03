# DevOps Version-Controlled Project with Git

This repository demonstrates enterprise Git version control workflows, branching strategies, and automated CI/CD practices as part of the DevOps Internship (Task 4).

## 📌 Project Overview
A containerized Python Flask REST API featuring system health monitoring, unit tests, multi-stage Docker containerization, and automated GitHub Actions CI.

## 🌿 Branching Strategy
We follow the **Feature Branch Workflow**:
- **`main`**: Production-ready code. Commits arrive strictly via PR from `dev` and are tagged with releases (e.g. `v1.0.0`).
- **`dev`**: Active integration branch. All features are merged here and tested before release.
- **`feature/*`**: Dedicated branches for specific features and fixes (e.g. `feature/api-service`, `feature/docker-setup`).

---
*More documentation will be added as features are developed through pull requests.*
