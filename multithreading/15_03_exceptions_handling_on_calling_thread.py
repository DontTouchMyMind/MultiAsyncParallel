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
    print('Started main')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res_list = executor.map(div, (3, 5), (15, 25))
        while res_list:
            try:
                cur_res = next(res_list)
            except StopIteration:
                print('stop iteration')
                break
            except Exception as ex:
                print(repr(ex))

    print('main ended')
