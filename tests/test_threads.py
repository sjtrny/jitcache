from jitcache import Cache
from concurrent.futures import ThreadPoolExecutor
import time

cache = Cache()


@cache.memoize
def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2


def test_threads_results():

    n_threads = 10

    executor = ThreadPoolExecutor(max_workers=n_threads)

    future_list = []
    result_list = []
    expected_result_list = []

    n_requests = 5

    # Set up n requests for an object
    for i in range(n_requests):
        kwarg_dict = {"input_1": 10, "input_2": 4}

        f = executor.submit(slow_fn, **kwarg_dict)

        future_list.append(f)
        expected_result_list.append(slow_fn(**kwarg_dict))

    # Set up n requests for an object
    for i in range(n_requests):
        kwarg_dict = {"input_1": 20, "input_2": 6}

        f = executor.submit(slow_fn, **kwarg_dict)

        future_list.append(f)
        expected_result_list.append(slow_fn(**kwarg_dict))

    # Collect the results
    # Notice that slow_fn is only called once for each key
    for f in future_list:
        result_list.append(f.result())

    assert result_list == expected_result_list
