import textwrap
import unittest

from netjsonconfig import OpenWrt
from netjsonconfig.utils import _TabsMixin


class TestFirewall(unittest.TestCase, _TabsMixin):
    maxDiff = None

    _rule_1_netjson = {
        "firewall": {
            "rules": [
                {
                    "name": "Allow-MLD",
                    "src": "wan",
                    "src_ip": "fe80::/10",
                    "proto": ["icmp"],
                    "icmp_type": ["130/0", "131/0", "132/0", "143/0"],
                    "target": "ACCEPT",
                    "family": "ipv6",
                }
            ]
        }
    }

    _rule_1_uci = textwrap.dedent(
        """\
        package firewall

        config defaults 'defaults'

        config rule 'rule_Allow_MLD'
            option name 'Allow-MLD'
            option src 'wan'
            option src_ip 'fe80::/10'
            option proto 'icmp'
            list icmp_type '130/0'
            list icmp_type '131/0'
            list icmp_type '132/0'
            list icmp_type '143/0'
            option target 'ACCEPT'
            option family 'ipv6'
        """
    )

    def test_render_rule_1(self):
        o = OpenWrt(self._rule_1_netjson)
        expected = self._tabs(self._rule_1_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_rule_1(self):
        o = OpenWrt(native=self._rule_1_uci)
        self.assertEqual(o.config, self._rule_1_netjson)

    _rule_2_netjson = {
        "firewall": {
            "rules": [
                {
                    "name": "Allow-DHCPv6",
                    "src": "wan",
                    "src_ip": "fc00::/6",
                    "dest_ip": "fc00::/6",
                    "dest_port": "546",
                    "proto": ["udp"],
                    "target": "ACCEPT",
                    "family": "ipv6",
                }
            ]
        }
    }

    _rule_2_uci = textwrap.dedent(
        """\
        package firewall

        config defaults 'defaults'

        config rule 'rule_Allow_DHCPv6'
            option name 'Allow-DHCPv6'
            option src 'wan'
            option src_ip 'fc00::/6'
            option dest_ip 'fc00::/6'
            option dest_port '546'
            option proto 'udp'
            option target 'ACCEPT'
            option family 'ipv6'
        """
    )

    def test_render_rule_2(self):
        o = OpenWrt(self._rule_2_netjson)
        expected = self._tabs(self._rule_2_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_rule_2(self):
        o = OpenWrt(native=self._rule_2_uci)
        self.assertEqual(o.config, self._rule_2_netjson)

    _rule_3_netjson = {
        "firewall": {
            "rules": [
                {
                    "name": "Allow-Ping",
                    "src": "wan",
                    "proto": ["icmp"],
                    "family": "ipv4",
                    "icmp_type": ["echo-request"],
                    "target": "ACCEPT",
                    "enabled": False,
                }
            ]
        }
    }

    _rule_3_uci = textwrap.dedent(
        """\
        package firewall

        config defaults 'defaults'

        config rule 'rule_Allow_Ping'
            option name 'Allow-Ping'
            option src 'wan'
            option proto 'icmp'
            option family 'ipv4'
            list icmp_type 'echo-request'
            option target 'ACCEPT'
            option enabled '0'
        """
    )

    def test_render_rule_3(self):
        o = OpenWrt(self._rule_3_netjson)
        expected = self._tabs(self._rule_3_uci)
        self.assertEqual(o.render(), expected)

    def test_parse_rule_3(self):
        o = OpenWrt(native=self._rule_3_uci)
        self.assertEqual(o.config, self._rule_3_netjson)