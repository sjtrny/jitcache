from multiprocessing import Manager

class KVStore():
    """
    """

    def __init__(self, manager = None, initial_dict = None):
        """
        Create a new key-value store with an option intial_dict, which requires an external multiprocessing.Manager()

        Args:
            manager (multiprocessing.Manager): an external multiprocessing.Manager that was used to create ``initial_dict``
            initial_dict (multiprocessing.Manager.dict): a multiprocessing.Manager.dict
        """

        if initial_dict is not None and manager is None:
            raise Exception("You must pass an accompanying Manager with your initial dictionary")

        if manager is None:
            self.__manager = Manager()
        else:
            self.__manager = manager

        self.__lock_access_lock = self.__manager.Lock()

        self.__locks = self.__manager.dict()

        if initial_dict is not None:
            self.__items = initial_dict
        else:
            self.__items = self.__manager.dict()

        # For some reason, if we initialise the locks dictionary here, our code will fail later
        # So we don't bother creating locks for objects that already exist

    def get_value(self, key, producer_fn=None, fn_kwargs=None):
        """
        Request a value from the store and generate the object via producer_fn if it does not exist.

        Args:
            key (hashable): the unique identifier of the object in the store
            producer_fn: a function to generate the value if it does not exist
            fn_kwargs (dict): arguments to pass to producer_fn
        """

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
                if producer_fn is None:
                    raise Exception("No function defined to generate value")
                self.__items[key] = producer_fn(**fn_kwargs)
            self.__locks[key].release()

        return self.__items[key]

    def set_value(self, key, value):
        """
        Set a value in the store if you have already computed it before hand

        Args:
            key (hashable): the unique identifier of the object in the store
            value: any object
        """
        self.get_value(key, lambda: value, {})