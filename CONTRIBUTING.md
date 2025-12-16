# Contributing to A.N.V.I.L.

We welcome new specialized agents!

## Architecture Rules
1.  **Separation of Concerns:** Each Agent must have a single "Lens." Do not mix Psychology with Physics.
2.  **The Forge Protocol:** All agents must implement an `analyze(text)` method that returns a dictionary containing a `status` ("SAFE" or "RISK") and `details`.

## Adding a New Agent
1.  Create a prompt kernel in `anvil/prompts/`.
2.  Create the agent class in `anvil/agents/`.
3.  Register the agent in `anvil/forge.py`.
4.  
