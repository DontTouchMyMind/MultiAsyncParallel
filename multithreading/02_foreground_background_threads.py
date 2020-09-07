# 1 Что бы решить проблему в '01_problem_demo.py', необходимо read_ints запустить в новом потоке.
import threading
import time

from multithreading.count_three_sum import count_three_sum, read_ints

if __name__ == '__main__':
    print('Started main.')

    ints = read_ints('../data/1Kints.txt')
    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)  # 1 Создадим объект потока
    t1.start()
    time.sleep(3)  # Поиск троек будет осуществяться только в это время, если daemon=True!

    # t1 = threading.Thread(target=count_three_sum, args=(ints,))  # 1 Создадим объект потока
    # t1.start()

    # Таким образом основной поток нее будет заблокирован,
    # Функции print (ниже) выполнятся, а поиск троек будет продолжаться.
    print('What are we waiting for?')
    t1.join()  # Основной поток будет заблокирован пока не выполнится t1
    print('Ended main.')
