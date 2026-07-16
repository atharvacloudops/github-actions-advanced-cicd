# ⚡ GitHub Actions Advanced CI/CD.

A complete CI/CD automation project covering reusable workflows, matrix builds,
OIDC keyless AWS authentication, deployment environments with approval gates,
and release automation pipeline.

---

## 📁 Project Structure

```text
github-actions-advanced-cicd/
├── app/
│   ├── main.py                     # FastAPI application
│   ├── requirements.txt            # Python dependencies
│   └── test_main.py                # Pytest test suite
│
├── .github/
│   ├── actions/
│   │   └── setup-python-app/
│   │       └── action.yml          # Composite reusable action
│   │
│   └── workflows/
│       ├── matrix-test.yml         # Matrix builds across OS & Python versions
│       ├── reusable-deploy.yml     # Reusable deployment workflow
│       ├── oidc-aws.yml            # OIDC keyless AWS authentication
│       └── release.yml             # Automated release pipeline
│
├── Dockerfile                      # Multi-stage production image
├── .dockerignore                   # Build context exclusions
└── README.md                       # Project documentation
```

---

## 🔄 Workflows Overview

| Workflow | Trigger | Purpose |
|---|---|---|
| matrix-test.yml | Push to main | Tests on 2 OS × 2 Python = 4 parallel jobs |
| oidc-aws.yml | Push to main | Keyless AWS auth via OIDC |
| reusable-deploy.yml | Called by other workflows | Reusable deploy logic |
| release.yml | Push tag v*.*.* | Full release pipeline |

---

## ✨ Key Features

### 🔁 Reusable Workflows & Composite Actions
- Composite action bundles Python setup + pip cache + install into one reusable step
- Reusable deploy workflow called from release pipeline for staging and production
- No duplicated workflow code across jobs

### 🧪 Matrix Builds
- Tests run in parallel across ubuntu-22.04 and ubuntu-24.04
- Tests run across Python 3.11 and 3.12
- fail-fast: false ensures all matrix legs complete even if one fails
- Total: 4 parallel jobs running simultaneously

### 🔐 OIDC Keyless AWS Authentication
- No AWS access keys stored in GitHub Secrets
- GitHub requests JWT from OIDC provider
- JWT exchanged with AWS STS for temporary credentials
- Credentials auto-expire after job completes

### 🌍 Deployment Environments
- Staging environment — auto deploys on tag push
- Production environment — requires manual approval from reviewer
- Full deployment history tracked per environment on GitHub

### 🚀 Release Automation Pipeline
- Triggered by pushing a version tag (v1.0.1)
- Builds multi-arch Docker image (amd64 + arm64)
- Runs full test suite before any deployment
- Deploys to staging then waits for production approval

---

## 🚀 How to Trigger

### Run Tests
```bash
git push origin main
# Matrix Test workflow triggers automatically
```

### Create a Release
```bash
git tag v1.0.2
git push origin v1.0.2
# Release pipeline triggers automatically
# Approve production deployment in GitHub Actions
```

---

## 🛠️ Tech Stack

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazonaws&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
