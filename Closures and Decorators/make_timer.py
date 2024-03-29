import time


def make_timer():           # should really be called stopwatch...
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
        result = now - last_called
        last_called = now
        return result

    return elapsed
