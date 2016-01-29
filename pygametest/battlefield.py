"""This module contains code relevent to the battlefield."""


class Battlefield(object):
    """
    A class which represents the battlefield within a battle.
    """

    def __init__(self):
        """
        The method used to construct a basic battlefield.
        """

        # The panels of the battlefield
        self.panels = None


class BattlefieldPanel(object):
    """
    A class which represents a single battlefield panel.
    """

    def __init__(self, owner, state):
        """
        The method used to create a batlefield panel and set its initial state.

        :param str owner: The initial owner of the battlefield panel.
        :param str state: The initial state of the battlefield panel.
        """

        # Make sure that the given owner is valid
        if owner != "Player" and owner != "Enemy":
            raise InvalidBattlefieldPanelOwner(owner)

        # Set the owner of the panel
        self.owner = owner

        # Make sure that the given state is valid
        valid_states = [
            "Normal",
            "Fire",
            "Water",
            "Grass",
            "Hole",
        ]
        if not state in valid_states:
            raise InvalidBattlefieldPanelState(state)

        # Set the state of the panel
        self.state = state


class InvalidBattlefieldPanelOwner(Exception):
    """
    An exception which is raised whenever a battlefield panel is attempted to
    be created with an invalid player.
    """
    pass

class InvalidBattlefieldPanelState(Exception):
    """
    An exception which is raised whenever a battlefield panel is attempted to
    be created with an invalid state.
    """
    pass
