from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

setup(
    name="queens",
    version="1.0.0",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    install_requires=parse_requirements("requirements.txt"),
)
