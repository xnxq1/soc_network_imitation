import aioredis
from app.config import settings
class RedisConn:
    __slots__ = ('redis','redis_host', 'redis_port')

    def __init__(self, redis_host, redis_port):
        self.redis_host = redis_host
        self.redis_port = redis_port

    async def start_connection(self):
        try:
            self.redis = await aioredis.from_url(f"redis://{self.redis_host}:{self.redis_port}")
            pong = await self.redis.ping()
            if pong:
                print(f"Успешно подключено к Redis {self.redis_host}!")
        except Exception as e:
            print(f"Ошибка подключения к Redis: {e}")

    async def close_connection(self):

        await self.redis.close()
        print("Успешно отключение Redis!")

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, key, value):
        await self.redis.set(key, value)


redis_post = RedisConn(redis_host=settings.REDIS_POST_HOST, redis_port=6379)
redis_comm = RedisConn(redis_host=settings.REDIS_COMMENT_HOST, redis_port=6379)

