import time


def div(diviser, limit):
    print(f'Started div={diviser}')

    for x in range(1, limit):
        if x % diviser == 0:
            print(f'divisor={diviser}, x={x}')
        time.sleep(0.2)
    print(f'Ended div={diviser}')