import setuptools


PACKAGE_NAME = "cosyvoice_ttsfrd"

# Include package data in `setup.cfg` or `setup.py`
# setuptools will automatically handle configurations in pyproject.toml, but we need to ensure files are included
setuptools.setup(
    # Ensure specific files in the bundled_files directory are included, but exclude resource.zip
    package_data={
        f'{PACKAGE_NAME}': [
            'bundled_files/*.whl',
            # 'bundled_files/resource.zip' is excluded, will be downloaded from the network
        ],
    }
)
