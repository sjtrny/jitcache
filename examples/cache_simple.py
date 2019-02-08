import multiprocessing as mp
from cache import KVStore
import time
import json

store = KVStore()

def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2

kwarg_dict = {
    'input_1': 10,
    'input_2': 4
}

# Make a unique identifier for this object
key = json.dumps(kwarg_dict, sort_keys=True)

# Insert a value with corresponding key
value1 = store.get_value(key, slow_fn, kwarg_dict)

value2 = store.get_value(key, slow_fn, kwarg_dict)

print(value1), print(value2)
