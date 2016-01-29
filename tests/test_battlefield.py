"""These are tests of the battlefield."""
import unittest

from pygametest import BattlefieldPanel
from pygametest import InvalidBattlefieldPanelOwner
from pygametest import InvalidBattlefieldPanelState

####################
# BattlefiledPanel #
####################

class TestBattlefieldPanel(unittest.TestCase):
    """
    A class which defines the various tests of the BattlefieldPanel class.
    """

    def test_valid_owners(self):
        """
        A test which makes sure that panels can only be made with valid owners.
        """

        # Check all valid owners
        valid_owners = [
            "Player",
            "Enemy",
        ]
        for owner in valid_owners:
            panel = BattlefieldPanel(owner, "Normal")
            self.assertEqual(panel.owner, owner, msg="A panel with the valid owner " + owner + " was unable to be created.")

        # Check several invalid owners
        invalid_owners = [
            "Sally",
            "Bob",
            1,
            0.5,
        ]
        for owner in invalid_owners:
            success = False
            try:
                panel = BattlefieldPanel(owner, "Normal")
            except InvalidBattlefieldPanelOwner:
                success = True
            self.assertTrue(success, msg="A panel was able to be created with the invalid owner " + str(owner) + ".")

    def test_valid_states(self):
        """
        A test which makes sure that panels can only be created with valid
        states.
        """

        # Check all valid states
        valid_states = [
            "Normal",
            "Fire",
            "Water",
            "Grass",
            "Hole",
        ]
        for state in valid_states:
            panel = BattlefieldPanel("Player", state)
            self.assertEqual(panel.state, state, msg="A panel was unable to be created with the valid state " + state + ".")

        # Check several invalid states
        invalid_states = [
            "Unicorn",
            55,
            26.5,
            0,
        ]
        for state in invalid_states:
            success = False
            try:
                panel = BattlefieldPanel("Player", state)
            except InvalidBattlefieldPanelState:
                success = True
            self.assertTrue(success, msg="A panel was able to be created with the invalid state " + str(state) + ".")
