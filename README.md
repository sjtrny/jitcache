[![Build Status](https://travis-ci.org/sjtrny/jitcache.svg?branch=master)](https://travis-ci.org/sjtrny/jitcache)
[![Documentation Status](https://readthedocs.org/projects/jitcache/badge/?version=latest)](https://jitcache.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/jitcache)](https://pepy.tech/project/jitcache)

# jitcache

jitcache is a just-in-time key-value cache that is thread/process safe. jitcache also prevents repeated computation
when multiple workers request the same value.

jitcache was designed to improve the performance of Plot.ly Dash apps by caching results and reducing CPU load.

Installation
-------------------

Install via pip:

    $ pip install jitcache

Documentation
-------------------

Full documentation available here [https://jitcache.readthedocs.io/](https://jitcache.readthedocs.io/en/latest/)

Example Usage
-------------------

Notice that ``slow_fn`` is only called once, despite two requests.

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

 Output:
 
    Slow Function Called
    40
    40