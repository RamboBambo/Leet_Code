import functools
import inspect

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_names = inspect.getfullargspec(func)[0]
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        zip_args = zip(args_names, args_repr + kwargs_repr)
        final_args = map(lambda x: f'{x[0]}={x[1]}', zip_args)
        signature = ", ".join(final_args)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
