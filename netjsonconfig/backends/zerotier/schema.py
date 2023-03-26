"""
Zerotier specific JSON-Schema definition
"""

from copy import deepcopy

from ...schema import schema as default_schema

# The schema is taken from OpenAPI specification
# of Zerotier Controller REST API available at
# docs.zerotier.com/openapi/centralv1.json
# Note: Currently it supports only limited properties
base_zerotier_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": True,
    "properties": {
        "zerotier": {
            "type": "array",
            "title": "Zerotier",
            "uniqueItems": True,
            "additionalItems": True,
            "propertyOrder": 12,
            "items": {
                "type": "object",
                "title": "ZerotTier tunnel",
                "additionalProperties": True,
                "required": ["name", "id", "enableBroadcast"],
                "properties": {
                    "name": {
                        "title": "network name",
                        "description": "Zerotier network name",
                        "type": "string",
                    },
                    "id": {
                        "title": "network id",
                        "description": "Zerotier network ID",
                        "type": "string",
                        "minLength": 16,
                        "maxLength": 16,
                    },
                    "enableBroadcast": {
                        "title": "enable broadcast",
                        "type": "boolean",
                        "description": "Enable broadcast packets on the network",
                    },
                    "creationTime": {
                        "title": "creation time",
                        "type": "integer",
                        "description": "Creation time of the zerotier network.",
                    },
                    "private": {
                        "title": "private",
                        "type": "boolean",
                        "description": "Whether or not the zerotier network is private.  If false, members will *NOT* need to be authorized to join.",  # noqa
                    },
                },
            },
        }
    },
}

schema = deepcopy(base_zerotier_schema)
schema['required'] = ['zerotier']
schema['properties']['files'] = default_schema['properties']['files']
