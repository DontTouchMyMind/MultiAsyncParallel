import asyncio


async def fetch_doc(doc):
    await asyncio.sleep(1)  # Emulating doc downloading.
    return doc


async def get_pages(docs):
    for cur_doc in docs:
        doc = await fetch_doc(cur_doc)
        for page in doc:
            await asyncio.sleep(1)
            yield page


# По асинхронному генератору мы не можем пройтись обычным for, только async for!
async def main():
    # Результаты через async for мы будем получать как только они приходят!
    async for page in get_pages(['doc1', 'doc2']):
        print(f'Finally {page}')


if __name__ == '__main__':
    asyncio.run(main())
