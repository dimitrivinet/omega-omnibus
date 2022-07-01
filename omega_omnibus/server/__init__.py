from omega_omnibus.config import cfg

from . import app

# setup files that aren't necessarily imported by app
from .global_instances import games_store

__all__ = ["app", "games_store", "cfg"]
