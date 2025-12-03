# ProxyPulse: High-Performance SOCKS Validator CLI

<div align="center">
  <a href="https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI">
    <img src="https://raw.githubusercontent.com/chirag127/chirag127/main/assets/proxypulse_banner.png" alt="ProxyPulse Banner">
  </a>

  <p align="center">
    A high-performance, multithreaded Python CLI for rapidly validating SOCKS4/SOCKS5 proxy lists.
    <br />
    <a href="#key-features"><strong>Explore Features »</strong></a>
    <br />
    <br />
    <a href="https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/issues">Report Bug</a>
    ·
    <a href="https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/issues">Request Feature</a>
  </p>
</div>

<div align="center">

[
![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/ci.yml?branch=main&style=flat-square&logo=githubactions&logoColor=white)
](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/actions/workflows/ci.yml)
[
![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI?style=flat-square&logo=codecov&logoColor=white)
](https://codecov.io/gh/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI)
[
![Tech Stack: Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white)
](https://www.python.org/)
[
![Formatter: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square)
](https://github.com/astral-sh/ruff)
[
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square)
](https://creativecommons.org/licenses/by-nc/4.0/)
[
![GitHub Stars](https://img.shields.io/github/stars/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI?style=flat-square&logo=github&logoColor=white)
](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/stargazers)

</div>

> **Star ⭐ this Repo:** If ProxyPulse helps you streamline your workflow, please consider starring the repository. Your support helps the project grow and reach more developers!

---

## 🚀 BLUF (Bottom Line Up Front)

ProxyPulse is a high-performance, multithreaded Python CLI for rapidly validating SOCKS4/SOCKS5 proxy lists. It verifies connectivity and outputs a clean, reliable list of working proxies with zero external dependencies, optimized for speed and accuracy in cybersecurity and data scraping tasks.

---

## 📖 Table of Contents

- [🔧 Key Features](#-key-features)
- [🏗️ Project Architecture](#️-project-architecture)
- [🤖 AI Agent Directives](#-ai-agent-directives)
- [⚙️ Getting Started](#️-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Development Standards](#development-standards)
  - [Scripts](#scripts)
  - [Core Principles](#core-principles)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🔧 Key Features

- **High-Speed Validation:** Leverages multithreading to check thousands of proxies in seconds.
- **SOCKS4/SOCKS5 Support:** Comprehensive validation for both major SOCKS protocols.
- **Zero Dependencies:** A pure Python solution with no external libraries required, ensuring maximum portability.
- **Clean Output:** Generates a file containing only the working proxies for immediate use.
- **Customizable Timeout:** Set a custom timeout for proxy connections to balance speed and reliability.
- **Intuitive CLI:** Simple, clear command-line interface powered by Python's `argparse`.

---

## 🏗️ Project Architecture

The project follows a modular CLI architecture, separating concerns for clarity and maintainability. The core validation logic is decoupled from the command-line interface, allowing for easier testing and future expansion.

plaintext
.ProxyPulse-High-Performance-SOCKS-Validator-CLI/
├── src/
│   └── proxypulse/
│       ├── __init__.py
│       ├── core/           # Core validation logic, networking
│       │   └── validator.py
│       ├── utils/          # Helper functions, file I/O
│       │   └── io.py
│       └── cli.py          # Argparse-based command-line interface
│
├── tests/
│   └── test_validator.py   # Unit tests for core logic
│
├── pyproject.toml          # Project metadata and dependencies (uv)
├── .gitignore
└── README.md


---

## 🤖 AI Agent Directives

<details>
<summary><strong>click to expand:</strong> Apex Technical Authority Directives (December 2025)</summary>

### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards.
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

### 2. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
This repository, `ProxyPulse-High-Performance-SOCKS-Validator-CLI`, is a Python-based high-performance networking tool.

*   **PRIMARY SCENARIO: SYSTEMS / NETWORKING / CLI (Python)**
    *   **Stack:** This project leverages **Python 3.10+**. Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **High-Concurrency CLI Architecture**. This pattern emphasizes:
        1.  **Thread-Safe Operations:** All shared resources are managed using locks or queues to prevent race conditions.
        2.  **Efficient I/O:** Utilizes Python's `socket` and `threading` modules for non-blocking, parallel network operations.
        3.  **Separation of Concerns:** A clear division between the network I/O layer (`core`), the user interface (`cli`), and utility functions (`utils`).
    *   **CLI Framework:** Uses `argparse` for a lightweight, dependency-free, and powerful command-line interface.

### 3. MANDATORY VERIFICATION COMMANDS
Before committing, you **MUST** run these commands to ensure 100% compliance with project standards.

1.  **Format & Lint:** `uv run ruff check . --fix && uv run ruff format .`
2.  **Run Tests:** `uv run pytest`

</details>

---

## ⚙️ Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

- Python 3.10 or higher
- `uv` package manager (recommended)
  sh
  pip install uv
  

### Installation

1.  **Clone the repository:**
    sh
    git clone https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI.git
    cd ProxyPulse-High-Performance-SOCKS-Validator-CLI
    

2.  **Create a virtual environment and install dependencies:**
    sh
    # Create a virtual environment
    uv venv

    # Activate it (macOS/Linux)
    source .venv/bin/activate

    # Install dependencies
    uv pip install -r requirements.txt
    

---

## Usage

Run the validator from the command line, providing a file with a list of proxies.

sh
python -m src.proxypulse.cli -f path/to/your/proxies.txt -o working_proxies.txt -t 5 -th 100


**Arguments:**
- `-f`, `--file`: Path to the input file containing proxies (one per line, format: `ip:port`).
- `-o`, `--output`: Path to the output file for saving working proxies.
- `-t`, `--timeout`: (Optional) Connection timeout in seconds. Default is 5.
- `-th`, `--threads`: (Optional) Number of threads to use. Default is 100.

---

## Development Standards

This project adheres to modern Python development standards to ensure code quality, consistency, and maintainability.

### Scripts

Common development tasks are managed via `pyproject.toml` and run with `uv`.

| Command               | Description                                           |
| --------------------- | ----------------------------------------------------- |
| `uv run lint`         | Run Ruff linter to check for style and errors.        |
| `uv run format`       | Run Ruff formatter to automatically format the code.  |
| `uv run test`         | Execute the test suite using Pytest.                  |

### Core Principles

- **SOLID:** Design principles for creating understandable, flexible, and maintainable software.
- **DRY (Don't Repeat Yourself):** Avoid redundancy in code and logic.
- **YAGNI (You Ain't Gonna Need It):** Do not add functionality until it is deemed necessary.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please see [`CONTRIBUTING.md`](./.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

---

## 📜 License

Distributed under the Creative Commons Attribution-NonCommercial 4.0 International License. See [`LICENSE`](./LICENSE) for more information.
