from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.strategy import FSMStrategy
from redis.asyncio.client import Redis

from aiogram_starter_kit.handlers import routers
from aiogram_starter_kit.middlewares import DatabaseMiddleware


def get_redis_storage(redis: Redis) -> RedisStorage:
    """
    Create and return a Redis storage for Aiogram FSM.

    Args:
        redis (Redis): The Redis client instance.

    Returns:
        RedisStorage: The Redis storage instance for FSM data.
    """
    return RedisStorage(redis=redis)


def get_dispatcher(
    storage: BaseStorage = MemoryStorage(),
    fsm_strategy: FSMStrategy | None = FSMStrategy.CHAT,
    event_isolation: BaseEventIsolation | None = None,
) -> Dispatcher:
    """
    Create and configure an Aiogram Dispatcher.

    Args:
        storage (BaseStorage): The storage for dispatcher data (default is MemoryStorage).
        fsm_strategy (FSMStrategy | None): The FSM strategy to use (default is FSMStrategy.CHAT).
        event_isolation (BaseEventIsolation | None): The event isolation strategy (default is None).

    Returns:
        Dispatcher: The configured Aiogram Dispatcher instance.
    """
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
