---
name: Bug Report
about: Report a bug or issue in the ProxyPulse project
title: "Bug: [Concise description of the bug]"
labels: "bug"
assignees: "chirag127"

body:
  - type: markdown
    attributes:
      value: | 
        **Important:** Please ensure you have reviewed the project's [Contributing Guidelines](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/blob/main/.github/CONTRIBUTING.md) and [Security Policy](https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI/blob/main/.github/SECURITY.md) before submitting a bug report.

        **Please note:** This repository adheres to the Apex Technical Authority's 'Zero-Defect' principle. All issues should be reproducible and clearly documented.

        **Repository URL:** `https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI`

---

### 🐛 Bug Description

Describe the bug clearly and concisely. What is the unexpected behavior?

### 📍 Steps to Reproduce

Provide a step-by-step guide to reproduce the behavior. Be as detailed as possible.

1.  Go to '...' (e.g., `git clone https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI.git`)
2.  Checkout the specific commit/version (if applicable): `git checkout <commit_hash_or_tag>`
3.  Install dependencies: `uv pip install -r requirements.txt` (or appropriate command)
4.  Run the command with specific arguments:
    bash
    python -m proxypulse --proxy-list <path_to_input_file> --output <path_to_output_file> [other_options]
    
    *(Replace `<path_to_input_file>`, `<path_to_output_file>`, and `[other_options]` with actual values used when the bug occurred.)*
5.  Observe the error/unexpected behavior...

### 📄 Expected vs. Actual Behavior

**Expected:**

(Describe what you expected to happen)

**Actual:**

(Describe what actually happened)

### 🛠️ Environment

*   **ProxyPulse Version:** (e.g., `v1.0.0` or `main` branch commit hash)
*   **Python Version:** (e.g., `Python 3.10.9`)
*   **Operating System:** (e.g., `Linux 6.5.0-14-generic`, `macOS 13.6`, `Windows 11 Pro`)
*   **Proxy Type(s) Tested:** (e.g., `SOCKS4`, `SOCKS5`, `Both`)
*   **Proxy List Source (if applicable):** (e.g., `Custom list`, `Online source URL`)

### 📈 Potential Cause (Optional)

If you have any ideas about the cause of the bug, please share them here.

### 📸 Screenshots or Logs (Optional)

If applicable, add screenshots to help explain your problem. You can also paste relevant log snippets here.

log
Paste your log output here


### 💡 Additional Context (Optional)

Add any other context about the problem here. This might include specific network conditions, proxy configurations, or anything else that might be relevant.

---

**Note:** This issue template is generated according to the Apex Technical Authority's 'Zero-Defect, High-Velocity, Future-Proof' philosophy. Please provide comprehensive details to facilitate rapid resolution.
