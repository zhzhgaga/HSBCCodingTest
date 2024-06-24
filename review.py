# Review 1
def add_to_list(value, my_list=None):
    # default args are evaluated once when the function is defined not each time function id called.
    # mutable instance like list, dict.
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# Review 2
def format_greeting(name, age):
    # F-string
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3
class Counter:
    # class attr
    __count = 0

    def __init__(self):
        Counter.__count += 1

    @staticmethod
    def get_count():
        return Counter.__count

    def __del__(self):
        Counter.__count -= 1


# Review 4
import threading


class SafeCounter:
    counter_lock = threading.Lock()

    def __init__(self):
        self.count = 0

    def increment(self):
        self.counter_lock.acquire()
        self.count += 1
        self.counter_lock.release()


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            count = counts[item] + 1
            counts[item] = count
        else:
            counts[item] = 1
    return counts
