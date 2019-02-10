import multiprocessing as mp
from jitcache import Cache
import time


cache = Cache()


@cache.memoize
def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2


def test_process():
    kwarg_dict = {"input_1": 10, "input_2": 4}

    n_processes = 10

    process_list = []

    # Create a set of processes who will request the same value
    for i in range(n_processes):
        p = mp.Process(target=slow_fn, kwargs=kwarg_dict)
        process_list.append(p)

    # Start each process
    for p in process_list:
        p.start()

    # Wait for completion
    for p in process_list:
        p.join()

    # Print the value that they tried to compute
    assert slow_fn(**kwarg_dict) == 40
