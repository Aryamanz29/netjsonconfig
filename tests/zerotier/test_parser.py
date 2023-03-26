import unittest
from unittest.mock import patch

from netjsonconfig.backends.zerotier.parser import ZerotierParser


class TestBaseParser(unittest.TestCase):
    """
    Tests for netjsonconfig.backends.zerotier.parser.BaseParser
    """

    def test_parse_text(self):
        # Creating an instance of Zerotier Parser will raise
        # NotImplementedError since it will requires "parse_text"
        with self.assertRaises(NotImplementedError):
            ZerotierParser(config="")

    @patch.object(ZerotierParser, 'parse_text', return_value=None)
    def test_parse_tar(self, mocked):
        parser = ZerotierParser(config="")
        with self.assertRaises(NotImplementedError):
            parser.parse_tar(tar=None)

    @patch.object(ZerotierParser, 'parse_text', return_value=None)
    def test_get_vpns(self, mocked):
        parser = ZerotierParser(config="")
        with self.assertRaises(NotImplementedError):
            parser._get_vpns(text=None)

    @patch.object(ZerotierParser, 'parse_text', return_value=None)
    def test_get_config(self, mocked):
        parser = ZerotierParser(config="")
        with self.assertRaises(NotImplementedError):
            parser._get_config(contents=None)
