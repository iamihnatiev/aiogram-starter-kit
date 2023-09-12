from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.strategy import FSMStrategy
from redis.asyncio.client import Redis

from aiogram_starter_kit.handlers import routers
from aiogram_starter_kit.middlewares import DatabaseMiddleware


def get_redis_storage(redis: Redis) -> RedisStorage:
    return RedisStorage(redis=redis)


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
