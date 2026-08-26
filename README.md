# 🛡️ DevSecOps CI/CD Pipeline Implementation

## 📖 Project Overview
This repository showcases the implementation of a complete, automated **DevSecOps CI/CD pipeline**. The goal of this project is to demonstrate how to secure a software supply chain by integrating multiple security testing tools and automated deployment strategies into a modern development workflow.

The vulnerable web application used as the target for this pipeline is the [OWASP Juice Shop](https://owasp-juice.shop).

## 🛠️ Technologies & Tools
* **CI/CD:** GitLab CI, GitLab Runner (Self-Managed)
* **Version Control:** Git & GitHub
* **Secret Scanning:** GitLeaks
* **SAST (Static Application Security Testing):** NJSScan, Semgrep
* **SCA (Software Composition Analysis):** RetireJS
* **Container Scanning:** Trivy
* **Vulnerability Management:** DefectDojo, Python (API Automation)
* **Cloud & Containerization:** Docker, AWS ECR, AWS IAM, AWS EC2

---

## 🚀 Project Implementation Phases

This project was built iteratively, focusing on Shift-Left security principles. You can review the exact code changes, scripts, and implementation details for each phase in the following Pull Requests:

1. [**Phase 1: Setup GitLab CI & Early Secret Detection**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/8)
   * Configured a pre-commit hook and GitLab CI job using **GitLeaks** to prevent secrets from being pushed to the codebase.
2. [**Phase 2: Integrate SAST**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/2)
   * Implemented **NJSScan** and **Semgrep** to automatically identify misconfigurations and insecure coding patterns.
3. [**Phase 3: Centralize Findings in DefectDojo**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/3)
   * Developed a custom **Python script** to interact with the DefectDojo API, automatically parsing and uploading reports from the CI/CD pipeline tools.
4. [**Phase 4: Remediate Vulnerabilities (Closing the Loop)**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/4)
   * Patched application code to remediate weak cryptography and SQL injection vulnerabilities flagged during the automated scans.
5. [**Phase 5: Integrate SCA**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/6)
   * Added automated Software Composition Analysis using **RetireJS** to identify vulnerabilities in third-party dependencies, feeding the results into DefectDojo.
6. [**Phase 6: Automated Delivery to AWS ECR**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/7)
   * Secured **AWS IAM** credentials within CI/CD variables and optimized the pipeline to build and push the containerized application to **AWS Elastic Container Registry**.
7. [**Phase 7: Continuous Deployment to AWS EC2**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/9)
   * Configured a GitLab CI deployment job to securely connect to an **AWS EC2** instance via SSH, pull the latest image directly from ECR, and automatically launch the updated Docker container.
8. [**Phase 8: Self-Managed GitLab Runner on AWS EC2**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/10)
   * Provisioned an **AWS EC2** instance to register a project-level **self-managed GitLab Runner** using a **Shell executor** for direct host execution and host-level build layer reuse.
9. [**Phase 9: Container Image Scanning with Trivy**](https://github.com/manuel-garcia-gomez/juice-shop-devsecops/pull/11)
   * Integrated **Trivy** into the CI/CD pipeline to scan Docker images pulled from **AWS ECR**, failing the job strictly on **HIGH** or **CRITICAL** severity vulnerabilities.

---

## ⚖️ Credits & Disclaimer

The application code in this repository belongs to the **OWASP Juice Shop** project. Juice Shop is an intentionally insecure web application created for security training and awareness. 

* **Original Project:** [OWASP Juice Shop GitHub](https://github.com/juice-shop/juice-shop)
* **License:** MIT License (Copyright © Bjoern Kimminich & the OWASP Juice Shop contributors).

> **Note:** This fork is solely intended for educational purposes to demonstrate DevSecOps practices, CI/CD automation, and vulnerability remediation.