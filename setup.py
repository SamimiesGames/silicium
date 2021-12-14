from setuptools import find_packages, setup

VERISON = '0.1.0'

# import pypandoc

# long_description = pypandoc.convert_file('./README.md', 'rst')

setup(
    name='silicium',
    version=VERISON,
    description='Ahead-of-time interpreted all-language compiler in Python3',
    # long_description=long_description,
    author='Samimies',
    url='https://github.com/SamimiesGames/silicium',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    # packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3 :: Only'
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9'
    ],
    package_dir={
        '': 'src'
    },
    package_data={
        'silicium': ['*.typed']
    },
    zip_safe=False,
)

