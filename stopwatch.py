import time 

get_secs = int(input("Enter seconds : "))
def timer(secs):
    while secs >= 0:
        get_mins =  int(secs / 60)
        get_full_secs = int(secs % 60)
        stopwatch = f'{get_mins} : {get_full_secs}'
    
        print(stopwatch, end = "\r")
        secs -= 1
        time.sleep(1)
    print("Time's up")
            
timer(get_secs)


