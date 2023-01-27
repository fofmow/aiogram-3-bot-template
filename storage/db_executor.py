class DatabaseExecutor:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DatabaseExecutor, cls).__new__(cls)
        
        return cls.instance
