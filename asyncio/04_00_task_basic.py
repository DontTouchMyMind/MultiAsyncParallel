import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')
    return 'tick-tock'


async def main():
    t1 = asyncio.create_task(tick(), name='tick1')
    t2 = asyncio.ensure_future(tick())  # Аналогично t1.

    # await t1
    # await t2

    # Когда мы работаем с набором тасков, то есть для этого api.

    results = await asyncio.gather(t1, t2)

    print(f'{t1.get_name()}. Done= {t1.done()}')
    print(f'{t2.get_name()}. Done= {t2.done()}')

    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
