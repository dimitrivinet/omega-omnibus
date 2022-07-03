# setup files that aren't necessarily imported by app
from . import app, config, global_instances

__all__ = ["app", "global_instances", "config"]
