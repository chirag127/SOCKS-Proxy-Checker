---
name: 🐛 Bug Report
about: Report an unexpected behavior or flaw in the SOCKS Validator.
title: "[BUG] Concise summary of the issue (e.g., Multithreading hangs on specific timeout)"
labels: ["bug", "triage/priority-high"]
assignees: ""
--- 

## 🚨 Environment & Context

This section is crucial for immediate triage. Please provide as much detail as possible.

### 1. Repository Version / Commit

If possible, please provide the exact version or Git commit hash where the bug was observed. (If using `main`, specify the date).

*   **Version/Commit:** 

### 2. Operational Context

Describe how you executed the command that caused the failure.

*   **Operating System (Host):** (e.g., Ubuntu 22.04, Windows 11 WSL2, macOS Sonoma)
*   **Python Version:** (e.g., `python --version`)
*   **Input Proxy List Size:** (e.g., 100,000 entries)
*   **SOCKS Type Tested:** (SOCKS4, SOCKS5, or Both)

bash
# Paste the EXACT command executed here
proxy-pulse --input proxies.txt --output results.txt --threads 50


## 🛑 Steps to Reproduce

List the steps required to reproduce the behavior. Be precise.

1.  
2.  
3.  

## ❌ Expected Behavior

What did you expect the Validator to do according to the documentation or logical operation?

## 🎯 Actual Behavior

What actually happened? (e.g., Process terminated unexpectedly, Incorrect output file, Thread count discrepancy).

## 💻 Logs & Output (If Applicable)

Paste any relevant traceback or terminal output. If the issue involves concurrency or hangs, please describe the last few lines visible before the failure/freeze.

text
# Paste Output/Traceback Here


## ✨ Potential Fix / Insight (Optional)

If you have any thoughts on where the issue might lie (e.g., socket timeout logic, thread join issue), please share your insights. This helps speed up resolution.

---

*Adhering to the Apex Standard ensures rapid, zero-defect resolution. Thank you for contributing to `ProxyPulse-High-Performance-SOCKS-Validator-CLI`.*