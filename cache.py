from multiprocessing import Manager

class ThingStoreJIT():

    def __init__(self):

        self.__manager = Manager()
        self.__thing_list = self.__manager.list()
        self.__lock = self.__manager.Lock()

    def get_value(self, producer_fn = None, fn_kwargs = None):

        self.__lock.acquire()

        if len(self.__thing_list) == 0:
            if producer_fn is None:
                raise Exception("No function defined to generate value")

            self.__thing_list.append(producer_fn(**fn_kwargs))

        self.__lock.release()

        return self.__thing_list[0]

class KVStoreJIT():

    def __init__(self, manager = None, initial_dict = None):

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
        self.get_value(key, lambda: value, {})