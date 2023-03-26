from ..base.backend import BaseVpnBackend
from . import converters
from .parser import config_suffix, vpn_pattern
from .renderer import ZerotierRenderer
from .schema import schema


class Zerotier(BaseVpnBackend):
    schema = schema
    converters = [converters.Zerotier]
    renderer = ZerotierRenderer
    # BaseVpnBackend attributes
    vpn_pattern = vpn_pattern
    config_suffix = config_suffix

    @classmethod
    def auto_client(cls, host, server, **kwargs):
        return {'zerotier': [{**server, 'host': host}]}
