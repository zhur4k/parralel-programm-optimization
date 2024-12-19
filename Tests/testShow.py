import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from model.logic import Logic
from ui.show import Tkinter, graph_show

class TestGraphShow(unittest.TestCase):

    @patch('tkinter.Tk')
    def test_init_ui(self, mock_tk):
        """Тест на инициализацию UI"""
        app = Tkinter()
        self.assertIsNotNone(app.root)

if __name__ == '__main__':
    unittest.main()