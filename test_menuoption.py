# test_menuoption.py
"""
Tests for MenuOption module.
"""

import unittest
from menuoption import MenuOption

class TestMenuOption(unittest.TestCase):
    """Test cases for MenuOption class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MenuOption()
        self.assertIsInstance(instance, MenuOption)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MenuOption()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
