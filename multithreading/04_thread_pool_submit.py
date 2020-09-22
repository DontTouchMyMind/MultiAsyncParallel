import time


def div(divider, limit):
    print(f'Started div={divider}')

    for x in range(1, limit):
        if x % divider == 0:
            print(f'divider={divider}, x={x}')
        time.sleep(0.2)
    print(f'Ended div={divider}')
    