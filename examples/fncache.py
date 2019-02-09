from jitcache import FunctionCache
import time

cache = FunctionCache()

cache.memoize(time.time)

tx = time.time()


@cache.memoize
def slow_fn(input_1, input_2):
    print("Slow Function Called")
    # time.sleep(1)
    return input_1 * input_2


@cache.memoize
def slow_fn2(input_1, input_2, input_3=10):
    print("Slow Function2 Called")
    time.sleep(1)
    return input_1 * input_2 * input_3


t0 = time.time()
print(slow_fn(10, 2))
t1 = time.time()
print(t1 - t0)

t0 = time.time()
print(slow_fn(10, 2))
t1 = time.time()
print(t1 - t0)

t0 = time.time()
print(slow_fn(12, 2))
t1 = time.time()
print(t1 - t0)


t0 = time.time()
print(slow_fn2(10, 2))
t1 = time.time()
print(t1 - t0)

t0 = time.time()
print(slow_fn2(1, 3))
t1 = time.time()
print(t1 - t0)

t0 = time.time()
print(slow_fn2(1, 3, input_3=10))
t1 = time.time()
print(t1 - t0)
