import multiprocessing as mp
from jitcache import KVStore
import time
import json

store = KVStore()


def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2


kwarg_dict = {"input_1": 10, "input_2": 4}

# Make a unique identifier for this object
key = json.dumps(kwarg_dict, sort_keys=True)

n_processes = 10

process_list = []

# Create a set of processes who will request the same value
for i in range(n_processes):
    p = mp.Process(target=store.get_value, args=(key, slow_fn, kwarg_dict))
    process_list.append(p)

# Start each process
for p in process_list:
    p.start()

# Wait for completion
for p in process_list:
    p.join()

# Print the value that they tried to compute
print(store.get_value(key))
