from jitcache import KVStore
from multiprocessing import Manager
import time

def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2

object_id = "result_1"

manager = Manager()
initial_dict = manager.dict({object_id: slow_fn(10, 2)})

# Initialise the store with some objects
store = KVStore(manager, initial_dict)

# Try to retrieve the object or create it if it doesn't exist
value1 = store.get_value(object_id, slow_fn, {'input_1': 10, 'input_2': 4})

# If you know the object exists you can just use the object id
value2 = store.get_value(object_id)

if value1 == value2:
    print("Same object")

print(value1)
print(value2)