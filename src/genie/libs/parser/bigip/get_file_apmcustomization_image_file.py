# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/policy/customization-image-file' resources
# =============================================


class FileApmCustomizationimagefileSchema(MetaParser):

    schema = {}


class FileApmCustomizationimagefile(FileApmCustomizationimagefileSchema):
    """ To F5 resource for /mgmt/tm/file/apm/policy/customization-image-file
    """

    cli_command = "/mgmt/tm/file/apm/policy/customization-image-file"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
