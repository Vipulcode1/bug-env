from env.tasks import TASKS
from env.grader import run_tests

class BugEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_task = 0
        self.code = ""
        return self._get_state()

    def step(self, action):
        self.code = action
        task = TASKS[self.current_task]
        tests = task["tests"]

        passed = run_tests(self.code, tests)

        if passed == len(tests):
            reward = 1.0
            done = True
        else:
            reward = -0.1
            done = False

        return {
            "state": self._get_state(),
            "reward": reward,
            "done": done
        }

    def _get_state(self):
        task = TASKS[self.current_task]
        return {
            "code": self.code,
            "tests": task["tests"]
        }