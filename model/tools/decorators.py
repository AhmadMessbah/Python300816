def exception_handling(function):
    def inner(*args, **kwargs):
        try:
            output = getattr(function.__qualname__, *args[1:])
            return output
        except Exception as e:
            return False, str(e)

    return inner