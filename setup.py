from setuptools import find_packages, setup

NAME = "silicium"
VERSION = "0.1.4"
URL = "https://github.com/SamimiesGames/silicium"

AUTHOR = "Samimies"
DESCRIPTION = "Silicium is an ahead-of-time interpreted all-language compiler in Python."


setup(
    name=NAME,
    version=VERSION,
    url=URL,
    author=AUTHOR,
    license="MIT",
    description=DESCRIPTION,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"], where="src"),
    package_dir={"": "src"}
)

