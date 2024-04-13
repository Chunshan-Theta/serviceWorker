from queueTool import RedisQueue
import time

q = RedisQueue('rq')  # 新建队列名为rq
for i in range(50):
    q.put(i)
    print(f"input.py: data {i} enqueue {time.strftime('%c')}")
    time.sleep(1)