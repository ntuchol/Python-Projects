    import sys
    
    # ... some code ...
    
    sys.exit(0)  # Exit with success status
    # or
    exit(1) #exit with error status
    
    import os
    
    # ... some code ...
    
    os._exit(0)



    def main():
        # ... some code ...
        return
    
    if __name__ == "__main__":
        main()
    
        import time
    
    stop_flag = False
    
    def some_process():
        while not stop_flag:
            # Do something
            print("Running...")
            time.sleep(1)
    
    # Start the process (e.g., in a separate thread)
    
    # To stop it:
    stop_flag = True
    


    import signal
    
    def timeout_handler(signum, frame):
        raise TimeoutError("Timed out!")
    
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5) # Set timeout for 5 seconds
    
    try:
        # Run code that might take too long
        print("Start")
        time.sleep(10)
    except TimeoutError as e:
        print(e)
    finally:
      signal.alarm(0) # Disable the alarm