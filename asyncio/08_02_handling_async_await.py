import asyncio
import time

import aiohttp


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.photo_id = photo_id
        self.album_id = album_id

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_title(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


# В этом случае обработки исключения на 3-ей итерации мы провалимся и перейдем к 4-ой.
async def photos_by_album(task_name, album, session):
    if not isinstance(album, int):
        raise RuntimeError('invalid album number')

    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'

    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(photo) for photo in photos_json]


async def download_albums(albums):
    async with aiohttp.ClientSession() as session:
        for album in albums:
            # Отлов исключения ближе к источнику возникновения, позволит нам продолжить выполнение основной программы.
            try:
                yield await photos_by_album(f't{album}', album, session)
            except Exception as ex:
                print(repr(ex))


async def main():
    async for photos in download_albums([1, 2, 'a', 4]):
        print_photo_title(photos)


if __name__ == '__main__':
    asyncio.run(main())

    time.sleep(3)
    print('Main ended')
