from ..base.converter import BaseConverter
from .schema import schema


class Zerotier(BaseConverter):
    netjson_key = 'zerotier'
    intermediate_key = 'zerotier'
    _schema = schema

    def to_intermediate_loop(self, block, result, index=None):
        vpn = self.__intermediate_vpn(block)
        result.setdefault('zerotier', [])
        result['zerotier'].append(vpn)
        return result

    def to_netjson_loop(self, block, result, index=None):
        vpn = self.__netjson_vpn(block)
        result.setdefault('zerotier', [])
        result['zerotier'].append(vpn)
        return result

    def __netjson_vpn(self, vpn):
        vpn['id'] = str(vpn.pop('join')[0])
        vpn['name'] = vpn.pop('.name').replace('_', '-')
        vpn['enableBroadcast'] = vpn.pop('enabled', '0') == '1'
        del vpn['.type']
        return dict(vpn)

    def __intermediate_vpn(self, config, remove=[False, 0, '']):
        # add zerotier network id and name
        config['nwid'] = config.pop('id')
        config['n'] = config.get('name')
        return self.sorted_dict(config)
