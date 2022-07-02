import time
import functools
import memory_profiler as mem_profile
from django.db import reset_queries, connection


def memory_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        print(f"Memory (Before {func.__name__}): {mem_profile.memory_usage().__str__()} MB")
        result = func(*args, **kwargs)
        print(f"Memory (After {func.__name__}): {mem_profile.memory_usage().__str__()} MB")
        return result
    return inner_func


def check_performance_time(func):
    @functools.wraps(func)
    def do_wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished[{func.__name__}] in : {(end - start):.7f}s")
        return result
    return do_wrapper


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result
    return inner_func
