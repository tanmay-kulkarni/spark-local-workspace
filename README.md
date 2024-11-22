# Spark Local Workspace

## Overview
This project provides a containerized Apache Spark environment for local development and testing. It eliminates the need to install Spark directly on your machine while offering a seamless development experience.

## Key Features
- 🐳 Fully dockerized Spark environment
- 🔄 Hot-reload support for code changes
- 📊 Local data persistence
- 🛠️ Development-friendly setup

## Prerequisites
- Docker
- Docker Compose
- Poetry (for Python dependency management)

## Setup

### 1. Dependencies
Generate requirements.txt from poetry dependencies:
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

### 2. Launch Environment
Start the containerized Spark environment:
```bash
docker compose up --build
```

### 3. Workflow
- First time setup requires building the Docker image using `docker compose up --build`
- Subsequent runs only need `docker compose up` (no rebuild required)
- Code and data can be modified locally for fast development iteration
- Rebuilding is only necessary when:
  - Updating Spark version
  - Modifying container dependencies
  - Changing Docker configuration