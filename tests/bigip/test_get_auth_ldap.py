# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_auth_ldap
from genie.libs.parser.bigip.get_auth_ldap import AuthLdap

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/auth/ldap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:auth:ldap:ldapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/auth/ldap?ver=14.1.2.1",
            "items": [],
        }


class test_get_auth_ldap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [],
        "kind": "tm:auth:ldap:ldapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/auth/ldap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AuthLdap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AuthLdap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
