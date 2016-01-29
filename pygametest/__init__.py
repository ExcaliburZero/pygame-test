"""The init file for the pygametest package."""
from .battlefield import Battlefield
from .battlefield import BattlefieldPanel
from .battlefield import InvalidBattlefieldPanelOwner
from .battlefield import InvalidBattlefieldPanelState

__author__ = 'Christopher Randall Wells'
__copyright__ = 'Copyright 2016 Christopher Randall Wells'
__license__ = 'MIT'
__title__ = 'pygametest'
__version__ = '0.1'

__all__ = (
    # Classes
    'Battlefield',
    'BattlefieldPanel',

    # Exceptions
    'InvalidBattlefieldOwner',
    'InvalidBattlefieldState',
)
