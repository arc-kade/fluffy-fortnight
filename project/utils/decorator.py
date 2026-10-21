"""Decorators used by the Secure Log Analyzer & Backup System."""

import time
from functools import wraps


def log_execution(func):
    """Print start/completion messages and the execution time of `func`."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Function started]   {func.__name__}")
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"[Function completed] {func.__name__} ({elapsed:.6f} s)")

    return wrapper
