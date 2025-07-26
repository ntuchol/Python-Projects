    import sys
    

    exit(1) 
    
    import os
        
    os._exit(0)



    def main():
        return
    
    if __name__ == "__main__":
        main()
    
        import time
    
    stop_flag = False
    
    def some_process():
        while not stop_flag:
            print("Running...")
            time.sleep(1)
    
    stop_flag = True
    


    import signal
    
    def timeout_handler(signum, frame):
        raise TimeoutError("Timed out!")
    
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5) 
    
    try:
        print("Start")
        time.sleep(10)
    except TimeoutError as e:
        print(e)
    finally:
      signal.alarm(0) 
