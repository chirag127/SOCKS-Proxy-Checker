# ProxyPulse-High-Performance-SOCKS-Validator-CLI

![ProxyPulse Hero Banner](https://raw.githubusercontent.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/main/assets/banner.png)

| Status | Metrics | Standards | Tech Stack |
| :---: | :---: | :---: | :---: |
| [![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/ci.yml?branch=main&style=flat-square&label=CI%20Build)](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/actions/workflows/ci.yml) | [![Code Coverage](https://codecov.io/gh/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/branch/main/graph/badge.svg?style=flat-square)](https://codecov.io/gh/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI) | [![Linting: Ruff](https://img.shields.io/badge/Linting-Ruff-6E40C9?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff) | [![Python 3.10+](https://img.shields.io/badge/Python-3.10+%7C%203.11%20%7C%203.12-blue?style=flat-square&logo=python)](https://www.python.org/)
| [![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg?style=flat-square)](LICENSE) | [![GitHub Stars](https://img.shields.io/github/stars/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI?style=flat-square)](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/stargazers) | [![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](.github/CONTRIBUTING.md) | [![Dependencies: uv](https://img.shields.io/badge/Dependencies-uv-2B88DD?style=flat-square&logo=git%20lfs)](https://github.com/astral-sh/uv)

> ⭐ **Star this repository** to support the development of high-performance networking tools.

## 🚀 BLUF (Bottom Line Up Front)

**ProxyPulse** is a lightning-fast, highly concurrent Python CLI engineered for the immediate validation of large lists of SOCKS4 and SOCKS5 proxies. Utilizing native, non-blocking socket programming, it maximizes throughput, delivering verified, clean proxy lists with superior performance and zero reliance on external proxy testing APIs.

## 📋 Table of Contents

- [Architecture & Design](#-architecture--design)
- [Installation](#-installation)
- [Usage & Commands](#-usage--commands)
- [Development Standards](#-development-standards)
- [🤖 AI Agent Directives (Technical Spec)](#-ai-agent-directives-technical-spec)

## 🏗️ Architecture & Design

ProxyPulse is built upon a **Modular Monolith** pattern, separating the concerns of I/O handling, the core concurrent validation engine, and the CLI interface. This ensures the core networking logic remains highly optimized and independent of the user interface layer.

mermaid
graph TD
    A[ProxyPulse CLI (Click)] --> B{Input Handler (File/Stdin)};
    B --> C[Core Validation Engine];
    C -- Concurrency Pool --> D(Concurrent Socket Tester);
    D --> E[SOCKS4/SOCKS5 Protocol Adapter];
    E --> F((External Proxy IP:Port));
    F -- Success/Failure --> D;
    D -- Working Proxies --> G[Output Handler (Stdout/File)];
    G --> H[Validated Proxy List];
    
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px


## 📦 Installation

We utilize `uv` for robust, rapid dependency management and environment isolation.

### Prerequisites

Ensure you have Python 3.10+ installed and the `uv` package manager (recommended for speed).

bash
# 1. Install uv (if not present)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone the repository
git clone https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI
cd ProxyPulse-High-Performance-SOCKS-Validator-CLI

# 3. Create virtual environment and install dependencies using uv
uv venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
uv sync

# 4. Install the CLI executable
uv pip install -e .


## ⚙️ Usage & Commands

The main command is `proxypulse`.

### Validating a Proxy List

Validate a file of proxies (`ip:port` per line) with a 5-second timeout, outputting the results to a new file.

bash
proxypulse validate proxies.txt \
    --timeout 5 \
    --threads 200 \
    -o validated_socks.txt


| Option | Description | Default |
| :--- | :--- | :--- |
| `-i`, `--input <path>` | Path to the input file containing proxies (IP:PORT). | Required |
| `-o`, `--output <path>` | Path to save the list of working proxies. | stdout |
| `-t`, `--timeout <seconds>` | Connection timeout limit in seconds. | 10 |
| `-h`, `--threads <count>` | Maximum number of concurrent validation threads. | 100 |
| `--socks4` | Only check for SOCKS4 proxies. | False |
| `--socks5` | Only check for SOCKS5 proxies. | True (Default checks both) |

## 📐 Development Standards

### Core Principles

This project adheres strictly to the **SOLID** principles of software design and focuses on achieving maximum performance through native Python concurrency primitives, avoiding unnecessary external libraries.

*   **DRY (Don't Repeat Yourself):** Logic for socket connection and protocol negotiation is centralized.
*   **YAGNI (You Ain't Gonna Need It):** Features are minimal, focused solely on high-speed SOCKS validation.

### Available Scripts

| Script | Command | Description |
| :--- | :--- | :--- |
| `setup` | `uv sync` | Installs all required development and runtime dependencies. |
| `lint` | `ruff check .` | Runs the ultra-fast Ruff linter against all source code. |
| `format` | `ruff format .` | Auto-formats code using Ruff standards. |
| `test` | `pytest -v` | Executes all unit and integration tests defined in the `tests/` directory. |
| `ci` | `uv sync && ruff check . && pytest --cov=proxypulse` | Full continuous integration pipeline check. |


<details>
<summary><h2>🤖 AI Agent Directives (Technical Spec)</h2></summary>

# SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

## 1. IDENTITY & PRIME DIRECTIVE

**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter. You operate with absolute precision, enforcing FAANG-level standards.
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.

---

## 2. PROJECT-SPECIFIC STACK & ARCHITECTURE

This repository, `ProxyPulse-High-Performance-SOCKS-Validator-CLI`, is a core Python networking utility focused on maximum concurrent I/O performance.

### Primary Tech Stack

*   **Language:** Python 3.10+ (Prioritize features from 3.11/3.12 for performance).
*   **Package Manager:** `uv` (Used exclusively for fast dependency resolution and environment management).
*   **Linting/Formatting:** `Ruff` (Mandatory for ultra-fast, zero-config code quality enforcement).
*   **Testing Framework:** `Pytest` (Required for unit and integration testing of socket handling).
*   **CLI Framework:** `Click` (Used for defining the primary user interface commands).

### Architectural Pattern: Modular Monolith

The codebase is structured to ensure separation of networking logic from CLI parsing:

1.  **`proxypulse.core`:** Contains the high-performance concurrent socket and proxy protocol negotiation logic (SOCKS4/SOCKS5). This module must be dependency-free.
2.  **`proxypulse.cli`:** Handles command parsing, I/O file operations, and thread management.
3.  **Error Handling:** Use custom exceptions for network failures, timeouts, and protocol errors, ensuring graceful shutdowns.

### Performance Mandate

**Mandate:** Validation must leverage Python's native concurrency model (e.g., `ThreadPoolExecutor` or `asyncio` for non-blocking I/O) to handle thousands of concurrent connections. Do not rely on sequential processing.

---

## 3. DEVELOPMENT & VERIFICATION PROTOCOL

### Quality Assurance Gates

| Gate | Command | Pass Condition |
| :--- | :--- | :--- |
| **Dependencies** | `uv sync` | All packages resolved and environment set up. |
| **Code Quality** | `ruff check .` | Zero `E` or `W` errors. |
| **Format Standard** | `ruff format --check .` | Zero formatting differences found. |
| **Unit Testing** | `pytest` | 100% test pass rate. Focus on edge cases like malformed proxies and connection resets. |

### Core Engineering Principles

*   **SOLID:** Specifically, adhere to the Single Responsibility Principle (SRP): the socket handler should only handle the socket, and the parser should only parse.
*   **Agnosticism:** The core validation engine must remain protocol-agnostic (easily extendable to HTTP proxies if needed).
*   **Zero-Dependency Core:** The `core` module must not introduce heavy external dependencies, relying on Python's standard library (`socket`, `threading`, `concurrent`).

</details>
