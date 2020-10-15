import asyncio

from multithreading.decorators import measure_time, async_measure_time


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')

    # Внутри корутина можно заиметь доступ к объекту текущего event loop.
    loop = asyncio.get_running_loop()
    # И посмотреть на его состояние.
    if loop.is_running():
        print('Loop is still running')


@async_measure_time
async def main():
    # Методом gather возвращается awaitable объект.
    # await asyncio.gather(tick(), tick(), tick())
    # Аналогично...
    awaitable_object = asyncio.gather(tick(), tick(), tick())
    # Можно посмотреть какие корутины были отправленны в event loop на исполнение.
    for task in asyncio.all_tasks():
        print(task, end='\n')
    await awaitable_object


if __name__ == '__main__':
    # coroutine = main()
    # print(type(coroutine))

    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    try:
        # loop.run_until_complete(main())
        # Можно воспользоватся други API.
        loop.create_task(main())
        loop.run_forever()
        print('Coroutines have finished')
    except KeyboardInterrupt:
        print('Manually closed application')
    finally:
        loop.close()
        print('Loop is closed')
        print(f'Loop is closed = {loop.is_closed()}')
