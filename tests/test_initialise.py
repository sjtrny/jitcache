from jitcache import KVStore
from multiprocessing import Manager
import time
import json


def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2


def test_initialise():

    manager = Manager()

    kwarg_dict = {"input_1": 10, "input_2": 4}

    # Make a unique identifier for this object
    key = json.dumps(kwarg_dict, sort_keys=True)

    initial_dict = manager.dict({key: slow_fn(**kwarg_dict)})

    # Initialise the store with some objects
    store = KVStore(manager, initial_dict)

    # Try to retrieve the object or create it if it doesn't exist
    value1 = store.get_value(key, slow_fn, kwarg_dict)

    # If you know the object exists you can just use the object id
    value2 = store.get_value(key)

    assert value1 == value2 == slow_fn(**kwarg_dict)
