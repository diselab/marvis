from os.path import join as path_join, dirname
from setuptools import setup, find_packages

version = '0.1.0'
README = path_join(dirname(__file__), 'README.md')
long_description = open(README).read()
setup(
    name='marvis',
    version=version,
    description=('co-simulation hybrid testbed for distributed systems'),
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
    ],
    author='marvis team',
    author_email='all@diselab.berlin',
    url='https://github.com/diselab/marvis',
    download_url='https://codeload.github.com/diselab/marvis/tar.gz/master',
    packages=find_packages(),
    install_requires=[
        'pyroute2',
        'nsenter',
        'paramiko',
        (
            'activeexpressions @ '
            'git+https://github.com/active-expressions/'
            'active-expressions-static-python'
        ),

        # Those should be ``extras_require``, no?
        'pylxd',
        'docker',
    ],
    extras_require={
        'ns-3': [
            (
                'ns @ '
                'https://github.com/osmhpi/python-wheels/releases'
                '/latest/download/ns-3.33-py3-none-linux_x86_64.whl',
            ),
        ],
        'dev': [
            'pylint',
        ],
    },
)
