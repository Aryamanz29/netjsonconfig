from ...zerotier.converters import Zerotier as BaseZerotier
from .base import OpenWrtConverter


class Zerotier(OpenWrtConverter, BaseZerotier):
    _uci_types = ['zerotier']

    def __intermediate_vpn(self, vpn):
        vpn = super().__intermediate_vpn(vpn, remove=[''])
        # update vpn dict with zerotier configuration
        vpn.update(
            {
                '.name': self._get_uci_name(vpn.pop('name')),
                # add zerotier type
                '.type': 'zerotier',
                # for prototype demo purpose let's enable
                # the zerotier uci configuration (default)
                'enabled': vpn.pop('enableBroadcast', '1'),
                'join': [vpn.pop('nwid')],
            }
        )
        # now remove 'private' and 'n' property
        vpn.pop('n', None)
        vpn.pop('private', None)
        return vpn
