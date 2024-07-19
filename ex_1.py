# Write a code to generate 1000 random numbers using threading

from typing import List, Optional
from threading import Thread
import random


def generate_random_nos(count: int,
                        result: List[Optional[List[int]]],
                        index: int) -> int:
    """ Method which generates random numbers. """
    sub_result = list()
    for i in range(count):
        sub_result.append(str(random.randint(0, count)))

    result[index] = sub_result


def thread_manager() -> List[int]:
    """ Method that manages/handles threads. """

    total_nos = 1000
    num_threads = 10
    nos_per_thread = total_nos // num_threads
    result = [None] * num_threads
    thread_list = list()

    # Creating num_thread * threads
    # which will handle creation of random numbes of
    # 100 parallely.
    # Keeping a tab of all the Threads created in a thread_list.
    for i in range(num_threads):
        thread = Thread(target=generate_random_nos,
                        args=(nos_per_thread,result, i))
        thread_list.append(thread)
        thread.start()

    # Closing the execution of thread
    for thread in thread_list:
        thread.join()

    return ','.join([num for sublist in result
                for num in sublist])


if __name__ == '__main__':
    data = thread_manager()
    print(data)
