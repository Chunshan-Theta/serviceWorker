from queueTool import RedisQueue
import time

q = RedisQueue('rq')
while 1:
    result = q.get_nowait()
    if result is None:
        print("No Task in Queue")
    else:
        print(f"output.py: data {result} out of queue {time.strftime('%c')}")
    time.sleep(2)