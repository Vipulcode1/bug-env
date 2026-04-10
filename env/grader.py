def run_tests(code, tests):
    local_env = {}

    try:
        exec(code, {}, local_env)
    except Exception:
        return 0

    passed = 0

    for test in tests:
        try:
            if eval(test, {}, local_env):
                passed += 1
        except:
            pass

    return passed