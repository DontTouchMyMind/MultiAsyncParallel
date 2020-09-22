import concurrent.futures
import time


def div(divider, limit):
    print(f'Started div={divider}')

    result = 0
    for x in range(1, limit):
        if x % divider == 0:
            #print(f'divider={divider}, x={x}')
            result += x
        time.sleep(0.2)
    print(f'Ended div={divider}')
    return result

if __name__ == '__main__':
    print('Starting main')
    # C использованием блока with, shutdown=True расположиться в блоке finally,
    # и print('After with block') выполнится только по окончанию блока with.
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures.append(executor.submit(div, 3, 25))
        futures.append(executor.submit(div, 5, 25))

        while futures[0].running() and futures[1].running():
            print('.', end='')
            time.sleep(0.5)

        for f in futures:
            print(f'{f.result()}')
        print('Immediately printed out after submit')

    print('After with block')

    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    # executor.submit(div, 3, 25)
    # executor.submit(div, 5, 25)
    #
    # executor.shutdown(wait=False)   # print('\nmain ended') вызовется до завершения threats
    # print('\nmain ended')

