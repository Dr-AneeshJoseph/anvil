# 🔨 A.N.V.I.L. (Automated Network & Vulnerability Identification Logic)

> **The Multi-Agent Safety Engineering Framework.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


---

## ⚠️ The Problem
Safety is not one-dimensional. A system can be:
* **Mechanically Safe** (The brakes work).
* **Psychologically Unsafe** (The operator is disgruntled and has an override key).
* **Physically Impossible** (The plan relies on perpetual motion).

Standard LLMs blur these lines, giving you a "blended" average that misses critical specific risks.

## 🛡️ The Solution
**A.N.V.I.L.** is a multi-agent orchestration framework that subjects a system design to three distinct, adversarial audits:
1.  **The Engineer (STPA):** Looks for missing control loops and unsafe actions.
2.  **The Psychologist (CPIR):** Looks for human stressors and insider threats.
3.  **The Physicist (T1):** Validates the fundamental physical constraints.

The **Forge** (Orchestrator) synthesizes these reports. If *any* agent flags a Critical Risk, the system is rejected.

## 🚀 Quick Start
```bash
pip install -r requirements.txt
