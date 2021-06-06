class NullLock():
    """
    This class implements the interface of `threading.Lock` as a Null Object.
    """
    
    def acquire(self):
        pass

    def release(self):
        pass

    def locked(self):
        pass
