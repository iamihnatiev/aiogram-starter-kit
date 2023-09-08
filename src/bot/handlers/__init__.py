from .start import start_router
from .register import register_router
from .unrecognized import unrecognized_router

routers = (
    start_router,
    register_router,

    # Positioned last to handle unrecognized messages
    unrecognized_router,
)
