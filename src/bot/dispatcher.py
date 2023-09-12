from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.strategy import FSMStrategy
from redis.asyncio.client import Redis

from src.bot.handlers import routers
from src.bot.middlewares import DatabaseMiddleware
from src.config import conf


def get_redis_storage(redis: Redis) -> RedisStorage:
    return RedisStorage(redis=redis, state_ttl=conf.redis.state_ttl, data_ttl=conf.redis.data_ttl)


def get_dispatcher(
    storage: BaseStorage = MemoryStorage(),
    fsm_strategy: FSMStrategy | None = FSMStrategy.CHAT,
    event_isolation: BaseEventIsolation | None = None,
) -> Dispatcher:
    dp = Dispatcher(
        storage=storage,
        fsm_strategy=fsm_strategy,
        events_isolation=event_isolation,
    )

    # Register routers
    for router in routers:
        dp.include_router(router)

    # Register middlewares
    dp.update.middleware(DatabaseMiddleware())

    return dp
