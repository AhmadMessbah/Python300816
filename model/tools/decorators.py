from model.tools.logging import Logger


def exception_handling(function):
    def inner(*args, **kwargs):
        try:
            output = function(*args, **kwargs)
            Logger.info(f"Function {function.__name__} - {args[1:], kwargs} returned {output[1]}")
            return output
        except Exception as e:
            Logger.error(f"Function - {args, kwargs} Has Error {e}")
            return False, str(e)

    return inner