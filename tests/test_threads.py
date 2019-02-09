from jitcache import KVStore
from concurrent.futures import ThreadPoolExecutor
import json
import time


def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2


def test_threads_results():

    store = KVStore()

    n_threads = 10

    executor = ThreadPoolExecutor(max_workers=n_threads)

    future_list = []
    result_list = []
    expected_result_list = []

    n_requests = 5

    # Set up n requests for an object
    for i in range(n_requests):
        kwarg_dict = {"input_1": 10, "input_2": 4}

        key = json.dumps(kwarg_dict, sort_keys=True)
        f = executor.submit(store.get_value, key, slow_fn, kwarg_dict)

        future_list.append(f)
        expected_result_list.append(slow_fn(**kwarg_dict))

    # Set up n requests for an object
    for i in range(n_requests):
        kwarg_dict = {"input_1": 20, "input_2": 6}

        key = json.dumps(kwarg_dict, sort_keys=True)
        f = executor.submit(store.get_value, key, slow_fn, kwarg_dict)

        future_list.append(f)
        expected_result_list.append(slow_fn(**kwarg_dict))

    # Collect the results
    # Notice that slow_fn is only called once for each key
    for f in future_list:
        result_list.append(f.result())

    assert result_list == expected_result_list


def test_threads_store():
    store = KVStore()

    n_threads = 10

    executor = ThreadPoolExecutor(max_workers=n_threads)

    future_list = []

    n_requests = 5

    kwarg_dict_1 = {"input_1": 10, "input_2": 4}

    kwarg_dict_2 = {"input_1": 20, "input_2": 6}

    # Set up n requests for an object
    for i in range(n_requests):

        key = json.dumps(kwarg_dict_1, sort_keys=True)
        f = executor.submit(store.get_value, key, slow_fn, kwarg_dict_1)

        future_list.append(f)

    # Set up n requests for an object
    for i in range(n_requests):

        key = json.dumps(kwarg_dict_2, sort_keys=True)
        f = executor.submit(store.get_value, key, slow_fn, kwarg_dict_2)

        future_list.append(f)

    # Collect the results
    # Notice that slow_fn is only called once for each key
    for f in future_list:
        f.result()

    assert store.get_value(
        json.dumps(kwarg_dict_1, sort_keys=True)
    ) == slow_fn(**kwarg_dict_1)

    assert store.get_value(
        json.dumps(kwarg_dict_2, sort_keys=True)
    ) == slow_fn(**kwarg_dict_2)
