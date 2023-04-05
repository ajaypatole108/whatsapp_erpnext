from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in whatsapp/__init__.py
from whatsapp import __version__ as version

setup(
	name="whatsapp",
	version=version,
	description="whatsapp + interakt",
	author="Ajay Patole",
	author_email="ajaypatole@dhuparbrothers.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
