import setuptools

from intelmq_api.version import __version__

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intelmq-api",
    version=__version__,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/certtools/intelmq-api",
    packages=setuptools.find_packages(),
	install_requires=[
		"hug>=2.3.0",
        "intelmq>=2.3.0",
    ],
    python_requires='>=3.6',
	description="Intelmq-API is a REST API to manage an intelmq, a solution for IT security teams for collecting and processing security feeds",
    data_files = [('config', ['intelmq-api-config.json'])]
)