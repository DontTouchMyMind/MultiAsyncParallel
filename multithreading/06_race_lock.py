import concurrent.futures
import threading
import time


class BankAccount:
    def __init__(self):
        self.balance = 100  # shared data/resource.
        self.lock_obj = threading.Lock()    # Объявление спецальной абстракции, кот. ограничит доступ к ресурсам.

    def update(self, transaction, amount):
        print(f'{transaction} started')
        # В часть кода который уже захвачен, может войти только один поток!
        with self.lock_obj:     # acquire вызывается внутри try, а release - в finally.
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)  # Вызывает context switch.

            self.balance = tmp_amount

        print(f'{transaction} ended.')


if __name__ == '__main__':
    # lock_obj = threading.Lock()
    # print(lock_obj.locked())
    #
    # lock_obj.acquire()  # Захватить объект (овладеть)
    # print(lock_obj.locked())
    #
    # lock_obj.release()  # Освободить
    # print(lock_obj.locked())
    acc = BankAccount()
    print(f'Main started. acc.balance={acc.balance}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f'END of main. Balance={acc.balance}')
