class Logger:
    def __init__(self):
        print("Object is created.")

    def __del__(self):
        print("Object is destroyed.")


log = Logger()
del log