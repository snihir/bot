from .main import main_router
from .payment import payment_router
from .info import info_router
from .navigation import navigation_router
from .statistics import statistics_router

__all__ = ["main_router", "payment_router", "info_router", "navigation_router", "statistics_router"]
