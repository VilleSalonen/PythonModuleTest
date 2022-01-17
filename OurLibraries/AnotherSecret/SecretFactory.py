import random

def secret_factory_function():
    secret_int = random.randrange(10)
    return "secret factory produced %d" % (secret_int)
