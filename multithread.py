import threading
import time
import threading
import time

count = 0

# 这是为什么呢？因为count这个值是共享的，每个线程都可以在执行temp=count这行代码时拿到当前count的值，但是这些线程中的一些线程可能是并发或者并行执行的，这就导致不同的线...
#
# 拉勾教育版权所有：https://kaiwu.lagou.com/course/courseInfo.htm?courseId=46
class MyThread(threading.Thread):

    # Constructor
    def __init__(self, second):
        threading.Thread.__init__(self)  # self refers to the instance that calls on in this
        # case the instance is threading.Thread
        self.second = second

    def run(self):
        global count
        temp = count
        time.sleep(0.001)
        count = temp + 1


print(f'Threading {threading.current_thread().name} is running')
threads = []
for i in range(1000):
    thread = MyThread(i)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f'final count is: {count}')