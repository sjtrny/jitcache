from jitcache import Cache
import time


cache = Cache()


@cache.memoize
def slow_fn(input_1, input_2, input_3=10):
    print("Slow Function Called")
    time.sleep(1)
    return input_1 * input_2 * input_3


print(slow_fn(10, 2))
