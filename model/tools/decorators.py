def exception_handling(function):
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            return False, str(e)

    return inner