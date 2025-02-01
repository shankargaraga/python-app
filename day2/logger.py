def logger(func):
    def wrapper():
        print(f"someone called {func.__name__}")
        func()
        print(f"{func.__name__} exit")
    return wrapper


@logger
def processData():
    print("connecting to database")
    print("data processed")

processData()