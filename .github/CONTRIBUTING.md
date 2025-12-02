# Contributing to ProxyPulse-High-Performance-SOCKS-Validator-CLI

Thank you for considering contributing to **ProxyPulse-High-Performance-SOCKS-Validator-CLI**! We aim to maintain a high-quality, professional, and high-velocity project, adhering to FAANG-level standards and the principles of "Managing the Unmanageable."

## 1. Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct (v2.1). Please read the full text in `CODE_OF_CONDUCT.md` to understand the behaviors that are expected of you and other contributors.

## 2. Project Philosophy & Standards

*   **Zero-Defect, High-Velocity, Future-Proof:** Every contribution should strive for perfection, enable rapid development, and be built with longevity in mind.
*   **Professional Archival Standard:** All code, documentation, and metadata are treated with the utmost importance, even for archived projects.
*   **Apex Technical Authority:** We expect contributions to align with modern best practices and the standards defined in the project's `AGENTS.md`.

## 3. Getting Started

### 3.1. Prerequisites

Ensure you have the following installed:

*   **Python:** 3.10+ (as defined in `AGENTS.md` for Python projects).
*   **uv:** For managing Python packages and virtual environments.
*   **Git:** For version control.

### 3.2. Forking and Cloning

1.  Fork the repository: `https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI`
2.  Clone your forked repository:
    bash
    git clone https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI.git
    cd ProxyPulse-High-Performance-SOCKS-Validator-CLI
    

### 3.3. Setting Up the Development Environment

It is highly recommended to use `uv` for managing dependencies and creating a virtual environment.

1.  **Create and activate a virtual environment:**
    bash
    uv venv
    # On Linux/macOS:
    source .venv/bin/activate
    # On Windows:
    .venv\Scripts\activate
    
2.  **Install development dependencies:**
    bash
    uv pip install -r requirements-dev.txt
    

## 4. Contribution Workflow

We follow a standard Git workflow for contributions:

1.  **Create a New Branch:** Always work on a separate branch for your feature or fix. Use a descriptive name (e.g., `feature/add-new-proxy-type`, `fix/improving-error-handling`).
    bash
    git checkout -b your-branch-name
    
2.  **Make Your Changes:** Implement your code, adhering to the project's coding standards and architectural guidelines (refer to `AGENTS.md`).
3.  **Run Tests:** Ensure all tests pass.
    bash
    pytest
    
4.  **Lint and Format:** Use `ruff` to ensure code quality and consistency.
    bash
    ruff check --fix .
    ruff format .
    
5.  **Commit Your Changes:** Write clear, concise commit messages.
    bash
    git add .
    git commit -m "feat: Add description of your changes"
    
6.  **Push to Your Fork:** Push your branch to your forked repository.
    bash
    git push origin your-branch-name
    
7.  **Open a Pull Request:** Create a Pull Request from your branch to the `main` branch of the `chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI` repository.

## 5. Contribution Guidelines

### 5.1. Code Quality

*   **Pythonic Code:** Adhere to PEP 8 standards, enhanced by `ruff`'s strict configuration.
*   **Modularity:** Keep code modular and well-organized. Follow the principles outlined in `AGENTS.md`.
*   **Type Hinting:** Use type hints extensively for better code clarity and maintainability.
*   **Error Handling:** Implement robust error handling and logging.
*   **Documentation:** Write clear docstrings for all functions, classes, and modules.

### 5.2. Testing

*   **Unit Tests:** Write comprehensive unit tests using `pytest` for all new functionality and bug fixes.
*   **Integration Tests:** Include integration tests where appropriate to verify interactions between different components.
*   **Test Coverage:** Aim for high test coverage. Run `pytest --cov=proxypulse` to check coverage.

### 5.3. Commit Messages

Follow the Conventional Commits specification (e.g., `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`).

### 5.4. Pull Requests

*   **Clear Description:** Provide a detailed description of your changes, including the problem solved and the approach taken.
*   **Link to Issues:** If your PR addresses an issue, reference it using keywords like `closes #issue_number`.
*   **Single Responsibility:** Aim for Pull Requests that address a single concern or feature.

## 6. Reporting Bugs

If you find a bug, please open an issue on GitHub. Use the provided `bug_report.md` template under `.github/ISSUE_TEMPLATE/` to ensure all necessary information is captured.

## 7. Suggesting Enhancements

Feature requests can also be submitted as GitHub issues, clearly outlining the proposed enhancement and its benefits.

## 8. Security

If you discover a security vulnerability, please follow the guidelines in `.github/SECURITY.md`.

## 9. Project Structure & Architecture

Refer to the `AGENTS.md` file for detailed information on the project's architecture, tech stack, and development principles. This includes adherence to Python's best practices, the use of `uv`, `ruff`, and `pytest`, and the overall modular design.

Thank you for helping to improve **ProxyPulse-High-Performance-SOCKS-Validator-CLI**!