import aioredis
from app.config import settings

class RedisConn:
    __slots__ = ('redis',)

    async def start_connection(self):
        try:
            self.redis = await aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
            pong = await self.redis.ping()
            if pong:
                print("Успешно подключено к Redis!")
        except Exception as e:
            print(f"Ошибка подключения к Redis: {e}")

    async def close_connection(self):

        await self.redis.close()
        print("Успешно отключение Redis!")

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, key, value):
        await self.redis.set(key, value)


redis = RedisConn()
