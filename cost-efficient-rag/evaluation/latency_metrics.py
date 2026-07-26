import time

def measure_latency(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    latency = round(time.time() - start, 3)

    return result, latency