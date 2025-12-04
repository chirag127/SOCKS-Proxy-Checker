# 🤝 Contribution Guidelines for ProxyPulse-High-Performance-SOCKS-Validator-CLI

This project adheres to the standards set by the **Apex Technical Authority**. Contributions are welcomed from engineers dedicated to **Zero-Defect, High-Velocity, Future-Proof** development.

## 1. The Apex Philosophy

We operate under the principle of **"Managing the Unmanageable."** Contributions must align with high-performance standards, prioritizing efficiency, security, and maintainability. Every Pull Request will be scrutinized for adherence to SOLID principles, DRY coding, and comprehensive testing.

## 2. Supported Stack & Requirements

This repository is built using the **Python 3.10+ Apex Toolchain**.

*   **Language:** Python
*   **Dependency Management:** `uv` (Must manage dependencies via `pyproject.toml`)
*   **Linting/Formatting:** `Ruff` (Mandatory pre-commit hook)
*   **Testing:** `Pytest` (Minimum 90% coverage required for feature branches)
*   **Architecture:** Modular Monolith pattern.

## 3. Contribution Workflow

Follow these steps for submitting meaningful contributions:

### Step 1: Setup & Environment Synchronization

1.  **Fork** this repository to your personal account.
2.  **Clone** your fork locally:
    bash
    git clone https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI.git
    cd ProxyPulse-High-Performance-SOCKS-Validator-CLI
    
3.  **Install Dependencies** using the standard Apex Python manager (`uv`):
    bash
    uv sync  # Installs dependencies listed in pyproject.toml
    
4.  **Install Pre-commit Hooks:** Ensure local validation against Apex standards is enforced:
    bash
    pip install pre-commit
    pre-commit install
    

### Step 2: Feature Development & Isolation

1.  Create a new, descriptive branch. Follow the naming convention: `feat/short-description` or `fix/bug-id`.
    bash
    git checkout -b feat/fast-udp-check
    
2.  Develop your changes, ensuring **100% alignment** with the existing architectural patterns.
3.  **Testing is Mandatory:** Write new unit or integration tests (`Pytest`) covering **all** new logic paths. Run tests locally before committing:
    bash
    pytest
    
4.  **Linting:** Ensure all code passes `Ruff` checks:
    bash
    pre-commit run --all-files
    

### Step 3: Pull Request Submission

1.  **Commit** your changes using Conventional Commits format (e.g., `feat: Add new SOCKS5 handshake enhancement`).
2.  **Push** your branch to your fork.
3.  Open a **Pull Request** against `chirag127:main`.

## 4. Pull Request Requirements

Every PR **MUST** satisfy these criteria before merging:

*   **Template Usage:** Fill out the entire `.github/PULL_REQUEST_TEMPLATE.md`.
*   **Atomic Changes:** Each PR should address one logical concern. Do not mix feature work with documentation updates or unrelated fixes.
*   **Test Coverage:** Evidence of new or updated tests that increase or maintain high coverage.
*   **Code Review:** Pass all automated checks enforced by `.github/workflows/ci.yml`.
*   **Documentation:** Update relevant sections of `README.md` if the change affects usage or installation.

## 5. Reporting Issues & Security

*   **Bugs:** Report all bugs using the dedicated template: `.github/ISSUE_TEMPLATE/bug_report.md`.
*   **Security Vulnerabilities:** For security-sensitive issues, **DO NOT** open a public issue. Follow the guidelines in `.github/SECURITY.md` for responsible disclosure.

## 6. Code of Conduct

We expect all contributors to adhere to a professional, technical, and respectful dialogue. Disagreements must be framed around technical merit, not personal critique. Review the detailed expectations in `.github/CODE_OF_CONDUCT.md` (Assumed existence based on best practices).

--- 
*Thank you for elevating the standard of this repository.*