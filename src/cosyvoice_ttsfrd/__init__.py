__version__ = "0.4.2"

import pathlib

# Provide a helper function or variable to assist users in finding the decompressed resources.
# The resources are expected to be in the parent directory of this file.
PACKAGE_ROOT = pathlib.Path(__file__).parent
RESOURCE_PATH = PACKAGE_ROOT / "resource"  # Assume the decompressed directory is called resource

print(f"CosyVoice-ttsfrd initialized. Resources are expected in: {RESOURCE_PATH}")


def get_resource_path():
    """Returns the path to the unzipped resource directory."""
    return str(RESOURCE_PATH)
