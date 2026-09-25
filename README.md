# week61-devsecops-pipeline
Week 61 - Advanced CI/CD, DevSecOps and Release Automation
# Week 61 – Advanced CI/CD, DevSecOps & Release Automation

## Project Overview

This project demonstrates an automated CI/CD and DevSecOps workflow using
Python Flask, GitHub Actions, Docker, Trivy, and Kubernetes.

The goal is to automate software testing, code-quality validation,
container creation, security scanning, deployment preparation, health
verification, and rollback planning.

## Application

The project contains a simple Flask REST API.

Endpoints:

- `/` – Application home endpoint
- `/health` – Health-check endpoint
- `/version` – Application version endpoint

## CI/CD Pipeline

The automated workflow follows:

Code → Lint → Test → Build → Security Scan → Containerize → Deploy → Verify → Monitor

GitHub Actions automatically performs:

- Dependency installation
- Flake8 code-quality checks
- Pytest unit testing
- Docker image build
- Trivy vulnerability scanning

## Automated Testing

Pytest is used for automated unit testing.

The test suite validates:

- Home endpoint
- Health endpoint
- Version endpoint

## Containerization

The Flask application is packaged as a Docker container.

The project uses a Python slim base image to reduce unnecessary
dependencies and container size.

## Container Security

Trivy is used to scan the Docker image for known vulnerabilities.

Security practices include:

- Minimal base image
- Automated vulnerability scanning
- No secrets stored in the Docker image
- Dependency management
- `.dockerignore` configuration
- Image versioning

## Deployment Strategy

The project demonstrates a Blue-Green deployment strategy using Kubernetes.

Blue represents the current stable production version.

Green represents the new release.

The Green environment can be tested before production traffic is switched
from Blue to Green.

## Health Checks

Kubernetes readiness and liveness probes use the `/health` endpoint.

Readiness checks determine whether the application is ready to receive
traffic.

Liveness checks determine whether the application is healthy and should
continue running.

## Rollback Strategy

If the Green deployment fails, traffic can remain on Blue.

If a problem is discovered after switching traffic, the Kubernetes Service
selector can be changed from Green back to Blue.

This provides a fast recovery path with minimal downtime.

## Monitoring

Important production metrics include:

- Application availability
- HTTP error rate
- Response time
- CPU utilization
- Memory utilization
- Container restarts
- Failed health checks
- Deployment status

## Technologies

- Python
- Flask
- Pytest
- Flake8
- GitHub Actions
- Docker
- Trivy
- Kubernetes

## Repository Structure

.github/workflows/    CI/CD pipeline
tests/                Automated tests
security/             Security scan results
kubernetes/           Kubernetes deployment configuration
docs/                 Deployment and recovery documentation
app.py                Flask application
Dockerfile            Container configuration
requirements.txt      Python dependencies

## Week 61 Deliverables

- Advanced CI/CD pipeline
- Automated testing and quality checks
- Security scanning
- Container image security review
- Deployment strategy
- Blue-Green deployment configuration
- Health checks
- Rollback and recovery plan
- Updated project documentation

## Key Learning

This project demonstrates how CI/CD and DevSecOps practices combine
automated testing, security scanning, containerization, deployment
strategies, health verification, and rollback mechanisms to create a
safer and more reliable software delivery process.