from jitcache import Cache
import time
from concurrent.futures import ThreadPoolExecutor

cache = Cache()


@cache.memoize
def slow_fn(input_1, input_2):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2


n_threads = 10

executor = ThreadPoolExecutor(max_workers=n_threads)

future_list = []
result_list = []

n_requests = 5

# Set up n requests for an object
for i in range(n_requests):
    f = executor.submit(slow_fn, 10, 4)
    future_list.append(f)

# Collect the results
for f in future_list:
    result_list.append(f.result())

print(result_list)
