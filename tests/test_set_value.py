from jitcache import KVStore
import json


def slow_fn(input_1, input_2):
    return input_1 * input_2


def test_set_value():

    store = KVStore()

    kwarg_dict = {"input_1": 10, "input_2": 4}

    # Make a unique identifier for this object
    key = json.dumps(kwarg_dict, sort_keys=True)

    # Insert a value with corresponding key
    print("Start")
    store.set_value(key, slow_fn(**kwarg_dict))
    print("Value inserted")

    # Print the value that they tried to compute
    computed_value = store.get_value(key)

    actual_value = slow_fn(**kwarg_dict)

    assert computed_value == actual_value
