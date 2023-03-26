import unittest

from netjsonconfig import OpenWrt
from netjsonconfig.utils import _TabsMixin


class TestZerotier(unittest.TestCase, _TabsMixin):
    maxDiff = None
    _TEST_CONFIG = {
        "zerotier": [
            {
                "name": "zerotier-network-1",
                "enableBroadcast": False,
                "id": "79vgjhks7ae448c5",
            },
            {
                "name": "zerotier-network-2",
                "enableBroadcast": True,
                "id": "yt6c2e21c0fhhtyu",
            },
        ]
    }

    def test_render_zerotier(self):
        o = OpenWrt(self._TEST_CONFIG)
        expected = self._tabs(
            """package zerotier

config zerotier 'zerotier_network_1'
    option enabled '0'
    list join '79vgjhks7ae448c5'

config zerotier 'zerotier_network_2'
    option enabled '1'
    list join 'yt6c2e21c0fhhtyu'
"""
        )
        self.assertEqual(o.render(), expected)

    def test_parse_zerotier(self):
        native = self._tabs(
            """package zerotier

config zerotier 'zerotier_network_1'
    option enabled '0'
    list join '79vgjhks7ae448c5'

config zerotier 'zerotier_network_2'
    option enabled '1'
    list join 'yt6c2e21c0fhhtyu'
"""
        )
        expected = {
            "zerotier": [
                {
                    "name": "zerotier-network-1",
                    "enableBroadcast": False,
                    "id": "79vgjhks7ae448c5",
                },
                {
                    "name": "zerotier-network-2",
                    "enableBroadcast": True,
                    "id": "yt6c2e21c0fhhtyu",
                },
            ]
        }

        o = OpenWrt(native=native)
        self.assertEqual(o.config, expected)
