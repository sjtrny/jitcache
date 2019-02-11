from multiprocessing import Manager
from functools import wraps
import json
import inspect


class Cache:
    """
    This class is a thread and process safe cache that prevents duplicated
    computation of a function if it is not in the cache.
    """

    def __init__(self,):
        self.__manager = Manager()
        self.__lock_access_lock = self.__manager.Lock()
        self.__locks = self.__manager.dict()
        self.__items = self.__manager.dict()

    @staticmethod
    def __get_key(func, kwargs):
        func_id = id(func)
        return str(func_id) + json.dumps(kwargs, sort_keys=True)

    @staticmethod
    def __get_default_kwargs(func):
        return {
            k: v.default
            for k, v in inspect.signature(func).parameters.items()
            if v.default is not inspect.Parameter.empty
        }

    def memoize(self, func):
        """
        Decorator. Use this to cache any function.

        Args:
            func: the function to be cached
        """

        @wraps(func)
        def decorated(*args, **kwargs):

            kwargs_dict = inspect.getcallargs(func, *args, **kwargs)

            key = self.__get_key(func, kwargs_dict)

            # Check if this function is already cached
            if key not in self.__items:

                # Check if lock created for key
                # Prevent this code from being called twice
                if key not in self.__locks:
                    self.__lock_access_lock.acquire()
                    if key not in self.__locks:
                        self.__locks[key] = self.__manager.Lock()
                    self.__lock_access_lock.release()

                # Create
                self.__locks[key].acquire()
                if key not in self.__items:
                    self.__items[key] = func(*args, **kwargs)
                self.__locks[key].release()

            return self.__items[key]

        return decorated

    # TODO: Implement clear cache, must acquire global lock and all item locks
