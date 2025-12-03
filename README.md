<p align="center">
  <img src="https://custom-image-placeholder-url.com/proxypulse-high-performance-validator-hero.png" alt="ProxyPulse Hero Banner: High-Performance SOCKS Validator CLI" width="100%">
</p>

# ProxyPulse-High-Performance-SOCKS-Validator-CLI

<!-- Badge Section (Visual Authority) -->
[![GitHub Actions Status](https://img.shields.io/github/actions/workflow/status/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/ci.yml?branch=main&style=flat-square&label=Build%20Status)](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/actions/workflows/ci.yml)
[![Code Coverage](https://codecov.io/gh/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/branch/main/graph/badge.svg?style=flat-square)](https://codecov.io/gh/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Linter/Formatter](https://img.shields.io/badge/Linter-Ruff-purple?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI?style=flat-square&cacheSeconds=3600)](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/stargazers)

<p align="center">
  <a href="https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI">
    <img src="https://img.shields.io/badge/Star%20This%20Repo-⭐-black?style=for-the-badge">
  </a>
</p>

---

## 🚀 Overview (BLUF - Bottom Line Up Front)

**ProxyPulse** is an elite, high-performance command-line interface (CLI) tool designed for rapid, multithreaded validation of SOCKS4 and SOCKS5 proxy lists. Utilizing Python's native concurrency capabilities, it minimizes latency and maximizes throughput, providing zero-defect filtering of operational proxies for critical networking tasks.

This tool is optimized for system administrators, security researchers, and developers who require a verified, high-quality pool of SOCKS endpoints without reliance on external or third-party validation services.

---

## 📋 Table of Contents

1.  [🚀 Overview](#-overview-bluf---bottom-line-up-front)
2.  [✨ Key Features](#-key-features)
3.  [📦 Installation & Setup](#-installation--setup)
4.  [⚙️ Usage](#️-usage)
5.  [🏛️ Architectural Structure](#️-architectural-structure)
6.  [🤖 AI Agent Directives (System Specification)](#-ai-agent-directives-system-specification)
7.  [🛠️ Development & Principles](#-development--principles)
8.  [📜 License](#-license)

---

## ✨ Key Features

*   **Multithreaded Validation:** Achieves high concurrency via `concurrent.futures`, enabling thousands of checks per minute.
*   **SOCKS Protocol Support:** Full verification for SOCKS4 and SOCKS5 standards.
*   **Zero Dependency Core:** Operates purely on Python's standard library for maximum stability and minimal footprint.
*   **Time-Capped Connectivity:** Configurable timeout threshold for aggressive validation filtering.
*   **Clean Output Generation:** Automatically saves validated, working proxies to a defined output file (`--output`).

---

## 📦 Installation & Setup

ProxyPulse requires Python 3.10+ and uses **uv** for efficient dependency management.

### Prerequisites
Ensure you have Python 3.10 or later installed.

### Step 1: Clone the Repository

bash
git clone https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI.git
cd ProxyPulse-High-Performance-SOCKS-Validator-CLI


### Step 2: Install Dependencies using uv

We recommend `uv` for lightning-fast installation and dependency resolution.

bash
# Install uv if you don't have it
pip install uv

# Create and activate virtual environment
uv venv

# Install project dependencies (including development tools like Ruff, Pytest)
uv sync


---

## ⚙️ Usage

The CLI is structured around the `proxypulse` entry point.

### Basic Validation

Validate a list of proxies from `proxies.txt` with default settings (10 second timeout, 50 threads).

bash
python proxypulse/cli/main.py --input proxies.txt
# OR
uv run proxypulse --input proxies.txt


### Advanced Usage (High Performance)

Validate the list, setting a strict 3-second timeout, using 200 threads, and saving the output to `working_socks.txt`.

bash
uv run proxypulse \
    --input large_list.txt \
    --threads 200 \
    --timeout 3 \
    --output working_socks.txt


| Argument | Description | Required | Default |
| :--- | :--- | :--- | :--- |
| `--input <path>` | Path to the input file containing IP:Port proxies (one per line). | Yes | N/A |
| `--output <path>` | Path to save the validated, working proxies. | No | `working_proxies.txt` |
| `--threads <N>` | Number of concurrent threads for validation. Maximize based on core count. | No | 50 |
| `--timeout <N>` | Connection timeout in seconds. | No | 10 |
| `--verbose` | Enable verbose logging during the validation process. | No | False |

---

## 🏛️ Architectural Structure

ProxyPulse adheres to a **Modular Monolith** structure, separating the concurrency core from the networking logic and the command-line interface, ensuring clear boundaries and testability.

text
.
├── proxypulse/
│   ├── __init__.py
│   ├── cli/
│   │   ├── __init__.py
│   │   └── main.py       # Click CLI Entry Point & Argument Parsing
│   ├── core/
│   │   ├── __init__.py
│   │   └── validator.py  # Orchestrates multithreaded proxy checking
│   └── networking/
│       ├── __init__.py
│       └── connection.py # Low-level socket handling for SOCKS connectivity tests
├── tests/
│   ├── unit_tests/
│   └── integration_tests/
├── pyproject.toml        # Project definition, dependencies (uv) & configuration (Ruff/Pytest)
└── README.md


---

## 🤖 AI Agent Directives (System Specification)

The following directives detail the mandatory architectural and toolchain standards for any future modifications or maintenance performed by automated agents or human developers.

<details>
<summary><strong>SYSTEM SPECIFICATION (APEX TECHNICAL AUTHORITY)</strong></summary>

### 1. IDENTITY & PRIME DIRECTIVE

*   **Role:** Senior Principal Software Architect, enforcing 2026 standards.
*   **Context:** Current Date is **December 2025**.
*   **Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

### 2. CORE TECHNOLOGY STACK

This repository is built upon a high-performance Python ecosystem designed for concurrency and speed.

| Component | Tool / Standard | Purpose |
| :--- | :--- | :--- |
| **Runtime** | Python 3.10+ | Mandatory minimum version for optimization benefits. |
| **Package Manager** | `uv` | Used exclusively for dependency resolution, installation, and virtual environment management. |
| **Linter/Formatter** | `Ruff` | Enforced for all source code. Configuration resides in `pyproject.toml`. |
| **Testing Framework** | `Pytest` | Standard for all unit and integration tests. Coverage must remain above 90%. |
| **Concurrency** | `concurrent.futures` | Preferred module for thread and process pooling to manage simultaneous proxy checks. |

### 3. ARCHITECTURAL PATTERNS

*   **Modular Monolith:** Strict separation of concerns between `cli` (input/output), `core` (workflow orchestration), and `networking` (low-level socket operations).
*   **Performance First:** The `networking/connection.py` layer must prioritize non-blocking I/O patterns where possible, though currently relies on synchronous socket operations managed by a high thread count via `concurrent.futures.ThreadPoolExecutor`.
*   **SOLID Principles:** All classes must adhere to Single Responsibility Principle (SRP). Avoid large, monolithic validator functions.

### 4. VERIFICATION COMMANDS

All changes MUST pass the following verification checks:

1.  **Dependency Check:** Ensure environment integrity.
    bash
    uv check
    
2.  **Linting & Formatting (Ruff):** Run fixes and dry-run check.
    bash
    uv run ruff check .
    uv run ruff format --check .
    
3.  **Test Execution & Coverage:** Full test suite execution.
    bash
    uv run pytest --cov=proxypulse --cov-report=xml
    
</details>

---

## 🛠️ Development & Principles

### Development Scripts (Defined in `pyproject.toml` or `scripts/`)

| Script | Command | Description |
| :--- | :--- | :--- |
| `lint` | `uv run ruff .` | Runs the Ruff linter and formatter checks. |
| `format` | `uv run ruff --fix .` | Applies automatic code formatting and fixes. |
| `test` | `uv run pytest` | Executes the full test suite. |
| `test-coverage` | `uv run pytest --cov=proxypulse` | Runs tests and generates a code coverage report. |
| `start` | `uv run proxypulse --help` | Executes the main CLI entry point. |

### Core Engineering Principles

All contributions must strictly adhere to these standards:

1.  **DRY (Don't Repeat Yourself):** Abstract shared networking logic.
2.  **YAGNI (You Aren't Gonna Need It):** Focus solely on robust SOCKS validation (SOCKS4/5). Resist feature creep like HTTP/HTTPS proxy support unless architecturally isolated.
3.  **Optimized Concurrency:** Ensure thread management overhead is minimized relative to connection latency. Default thread count (50) is a pragmatic balance, but large operations may require tuning.

---

## 📜 License

This project is distributed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License. See the [LICENSE](LICENSE) file for full details.