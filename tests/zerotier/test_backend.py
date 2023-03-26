import tarfile
import unittest

from netjsonconfig import Zerotier
from netjsonconfig.exceptions import ValidationError


class TestBackend(unittest.TestCase):
    """
    tests for Zerotier backend
    """

    maxDiff = None
    _TEST_CONFIG = {
        "zerotier": [
            {
                "name": "network-network-1",
                "enableBroadcast": False,
                "id": "79vgjhks7ae448c5",
                "private": True,
            },
            {
                "name": "zerotier-network-2",
                "enableBroadcast": True,
                "id": "yt6c2e21c0fhhtyu",
                "private": False,
            },
        ]
    }

    def test_test_schema(self):
        with self.assertRaises(ValidationError) as context_manager:
            Zerotier({}).validate()
        self.assertIn(
            "'zerotier' is a required property", str(context_manager.exception)
        )

    def test_confs(self):
        c = Zerotier(self._TEST_CONFIG)
        expected = """# zerotier config: 79vgjhks7ae448c5

enableBroadcast=False
n=network-network-1
nwid=79vgjhks7ae448c5
private=True

# zerotier config: yt6c2e21c0fhhtyu

enableBroadcast=True
n=zerotier-network-2
nwid=yt6c2e21c0fhhtyu
private=False
"""
        self.assertEqual(c.render(), expected)

    def test_generate(self):
        c = Zerotier(self._TEST_CONFIG)
        tar = tarfile.open(fileobj=c.generate(), mode='r')
        # tar object should contain both zerotier configuration
        self.assertEqual(len(tar.getmembers()), 2)
        vpn1 = tar.getmember('79vgjhks7ae448c5.conf')
        contents = tar.extractfile(vpn1).read().decode()
        expected = """enableBroadcast=False
n=network-network-1
nwid=79vgjhks7ae448c5
private=True
"""
        self.assertEqual(contents, expected)

    def test_auto_client(self):
        expected = """# zerotier config: 79vgjhks7ae448c5

enableBroadcast=False
host=my.zerotier.com
n=network-network-1
nwid=79vgjhks7ae448c5
private=True
"""
        auto_client = Zerotier.auto_client(
            host='my.zerotier.com', server=self._TEST_CONFIG['zerotier'][0]
        )
        self.assertEqual(Zerotier(auto_client).render(), expected)
