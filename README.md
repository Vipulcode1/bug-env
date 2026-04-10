\# 🧠 AI Bug Fix Environment (OpenEnv Hackathon)



\## 🚀 Problem

Developers waste time fixing bugs without structured feedback.  

No automated environment to test, evaluate, and guide fixes step-by-step.



\---



\## 💡 Solution

We built an \*\*AI-powered bug fixing environment\*\* that:



\- Accepts code actions

\- Runs hidden test cases

\- Returns reward + feedback

\- Simulates reinforcement learning loop



\---



\## ⚙️ How it works



\### 1. Reset Environment

POST /reset



\### 2. Take Step

POST /step

{

&#x20; "action": "your code here"

}



\### Output

{

&#x20; "state": {...},

&#x20; "reward": 1.0,

&#x20; "done": true

}



\---



\## 🧪 Example



\### Input

def add(a,b): return a+b



\### Test

add(2,3)==5



\### Output

\- reward = 1.0 ✅

\- done = true



\---



\## 🧱 Architecture



\- FastAPI (server)

\- Custom Env (environment.py)

\- Grader (grader.py)

\- Task Engine (tasks.py)



\---



\## 🔥 Features



\- Multi-level tasks (easy → hard)

\- Dynamic test execution

\- Reward-based evaluation

\- API-based interaction



\---



\## 🚀 Future Scope



\- LLM auto-fix suggestions

\- Difficulty scaling

\- Debug explanation engine



\---



\## 👨‍💻 Team



\- Vipul

