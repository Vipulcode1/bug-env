\# AI Bug Fixing Environment



\## Problem

This environment simulates real-world debugging tasks where an AI agent fixes buggy Python code.



\## Tasks

\- Easy: Syntax errors

\- Medium: Logic bugs

\- Hard: Multi-case function bugs



\## Actions

\- edit\_code



\## Reward

\- Full fix: +1.0

\- Improvement: +0.5

\- Worse: -0.5

\- No change: -0.1



\## How to Run

1\. Start server:

&#x20;  uvicorn server.app:app --reload



2\. Run agent:

&#x20;  python inference.py

