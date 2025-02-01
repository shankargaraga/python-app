import time

def profiler(func):
    """Print the runtume of the decoreated function"""
    def wrapper_timmer(*args, **kwargs):
       start_time = time.perf_counter()
       value = func(*args, **kwargs)
       end_time = time.perf_counter()
       run_time = end_time - start_time
       print(f" Finished {func.__name__} in {run_time:.4f} secs")
       return value
    return wrapper_timmer


@profiler
def alogorithm(num_times):
   for _ in range(num_times): #throw away variables
      sum([i**2 for i in range(10000)])
    

#test code
alogorithm(1)
alogorithm(999)