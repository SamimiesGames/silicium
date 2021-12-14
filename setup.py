from setuptools import find_packages, setup

VERISON = '0.1.0'

# import pypandoc

# long_description = pypandoc.convert_file('./README.md', 'rst')


if __name__ == '__main__':
    setup(name='silicium',
    version=VERISON,
    description='Ahead-of-time interpreted all-language compiler in Python3',
    # long_description=long_description,
    author='Samimies',
    url='https://github.com/SamimiesGames/silicium',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    include_package_data=True,
    zip_safe=False
    )

