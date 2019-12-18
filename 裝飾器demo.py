class UseLogging(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif self.level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper


@UseLogging("info")
def test(name):
    print("test %s %s" % (name, test.__name__))
