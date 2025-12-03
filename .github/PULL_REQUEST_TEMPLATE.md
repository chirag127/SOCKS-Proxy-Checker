# Pull Request Template

---


**Please note:** This template is designed to ensure high-velocity, zero-defect contributions, adhering to the Apex Technical Authority's **40+ years of elite industry experience** and **Late 2025 Standards**.

---


## 1. PR Overview (BLUF)

*   **Briefly summarize the core change.** What problem does this PR solve, and what is the primary benefit?

---


## 2. Motivation & Context

*   **Why is this change necessary?** Link to relevant issues, tickets, or discussions.
*   **What is the impact of this change?** (e.g., performance improvement, bug fix, new feature, security enhancement).

---


## 3. Technical Details

*   **Describe the implementation details.** What architectural patterns were followed (e.g., SOLID, DRY)?
*   **Key changes:** List the most significant code modifications.
*   **Testing Strategy:** How was this change validated? (e.g., Unit tests, Integration tests, manual verification).
*   **Potential Risks/Considerations:** Any edge cases, dependencies, or future implications to be aware of?

---


## 4. Verification Steps

*   Provide clear, step-by-step instructions for reviewers to test this change.
*   Include any necessary setup, commands, or expected outcomes.

**Example:**

1.  `git clone https://github.com/chirag127/ProxyPulse-High-Performance-SOCKS-Validator-CLI.git`
2.  `cd ProxyPulse-High-Performance-SOCKS-Validator-CLI`
3.  `uv pip install --dev`
4.  `pytest`
5.  `python -m proxypulse --help`
6.  `python -m proxypulse --file ./tests/sample_proxies.txt --output ./working_proxies.txt`
7.  **Expected Outcome:** Verify that `./working_proxies.txt` contains only valid proxies from the sample list.

---


## 5. Impact on Apex Agents (If Applicable)

*   Does this change affect the `AGENTS.md` directives or the interpretation of the project's AI Agent instructions?
*   If yes, describe the changes and ensure `AGENTS.md` has been updated accordingly.

---


## 6. Code Quality & Standards

*   **Linting & Formatting:** Have all files been checked and formatted by Ruff?
*   **Type Safety:** Are TypeScript/Python type hints used correctly and consistently?
*   **Documentation:** Is new code adequately commented? Is the README up-to-date?
*   **Security:** Have potential security vulnerabilities been addressed (e.g., input validation, dependency scanning)?

---


## 7. Checklist

*   [ ] This pull request addresses an open issue or provides requested functionality.
*   [ ] The code has been tested locally and passes all tests.
*   [ ] Code follows the project's established style guides and best practices.
*   [ ] Documentation has been updated where necessary.
*   [ ] All AI Agent Directives in `AGENTS.md` are still accurate and relevant.
*   [ ] The new repository name (`ProxyPulse-High-Performance-SOCKS-Validator-CLI`) is used consistently in all links and references.
