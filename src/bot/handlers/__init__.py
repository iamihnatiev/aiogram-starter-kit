from .admin import admin_router
from .register import register_router
from .start import start_router
from .unrecognized import unrecognized_router


routers = (
    start_router,
    register_router,
    admin_router,

    # Positioned last to handle unrecognized messages
    unrecognized_router,
)
