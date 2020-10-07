import concurrent.futures
import time
from concurrent.futures._base import CancelledError


def div(divisor, limit):
    print(f'started div = {divisor}')

    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            print(f'{divisor=}, {x=}')
        time.sleep(0.2)
    print('raise exception')
    raise Exception('bad things happen!')


if __name__ == '__main__':
    print('started main')
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(div, 3, 15)
        time.sleep(5)
        print('Nothing happens until ...')
        # Реализация исключения на вызывающей стороне.
        try:
            res = future.result()  # .result прокинет исключение если оно произошло в потоке.
        except Exception as ex:
            print(repr(ex))
        # Нужно упомянуть специальные типы исключений, о которых стоит позаботиться.
        except CancelledError as ex:  # Если задача была отменена во время возбуждения исключения.
            print(repr(ex))
        except TimeoutError as ex:  # Если назначался таймаут, то может возникнить это исключение.
            print(repr(ex))

    print('main ended')
