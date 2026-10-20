# QA Automation Framework v2

[![Automated Regression Suite](https://github.com/Bunchuu/QA_Automation_Framework_v2/actions/workflows/tests.yml/badge.svg)](https://github.com/Bunchuu/QA_Automation_Framework_v2/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Playwright](https://img.shields.io/badge/playwright-tested-green.svg)
![Pytest](https://img.shields.io/badge/pytest-ready-brightgreen.svg)
![Docker](https://img.shields.io/badge/docker-containerized-blue.svg)
![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

Lightweight test automation framework demonstrating REST API and Web UI test strategies using Python, Playwright, and Pytest, containerized with Docker and fully integrated into a GitHub Actions CI/CD pipeline.

## Test Scope

* **API Testing (`tests/test_api.py`):**
  * Full CRUD lifecycle coverage on REST endpoints (GET, POST, PUT, DELETE).
  * Data-driven testing with `@pytest.mark.parametrize` for single post assertions and payload generation.
  * Negative scenario handling across non-existent endpoints (404 Not Found) and response time SLAs.
* **UI Testing (`tests/test_ui.py` + `pages/`):**
  * Implemented using the **Page Object Model (POM)** pattern.
  * Parameterized authentication test cases verifying positive flows and invalid credential banners.
  * Dynamic progress bar tracking with custom polling threshold assertions.
  * Headless browser execution with centralized fixture management (`conftest.py`).
* **Code Quality & Linting:**
  * Static code analysis with **Ruff** enforcing PEP 8 standards.
* **CI/CD Pipeline (`.github/workflows/tests.yml`):**
  * Automated regression pipeline triggered on every `push` and `pull_request` to `main`.
  * Multi-step headless test execution on Ubuntu Linux runners.
  * Automated standalone HTML regression report preserved as a build artifact.

## Repository Structure

```text
QA_14_Automation_Repository_v2/
├── .dockerignore
├── .github/workflows/tests.yml
├── .gitignore
├── Dockerfile
├── conftest.py
├── pages/
├── pytest.ini
├── requirements.txt
├── tests/
└── README.md
```

## Local Setup

### 1. Start the Docker container:

```bash
docker build -t qa-tests-v2 .
docker run --rm qa-tests-v2
```

### 2. Run Tests locally:

```bash
pytest
```