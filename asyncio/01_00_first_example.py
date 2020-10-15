import asyncio
import time

from multithreading.decorators import measure_time, async_measure_time


# Обычная последовательная работа.
# def tick():
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#
#
# @measure_time     #  Скорость выполнения 3 сек.
# def main():
#     for _ in range(3):
#         tick()


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


@async_measure_time  # Скорость выполнения 1 сек.
async def main():
    await asyncio.gather(tick(), tick(), tick())  # Асинхронное ожидание завершения корутинов.


if __name__ == '__main__':
    asyncio.run(main())  # Для работы с корутинами необходимо запустить Event Loop.
