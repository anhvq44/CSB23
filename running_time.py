import time
def running_time_calc(func):
    print("Start running-------")
    start_time = time.time()
    result = func()
    end_time = time.time()
    print("Finish--------")
    print(f"Output: {result}")
    print(f"Time: {(end_time - start_time):.6f}s")
    
