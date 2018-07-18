# module metadata
__description__ = "A Python Client for Gluu oxd Server"
__version__ = "3.1.2-alpha"
__author__ = "Gluu"

# setup logging system
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

# expose Client
from . client import Client

