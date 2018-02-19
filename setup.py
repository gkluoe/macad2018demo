from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='macad2018demo',
    version=__version__,
    description='A python tool to do some Mac admin tasks',
    long_description=long_description,
    url='https://github.com/gkluoe/macad2018demo',
    download_url='https://github.com/gkluoe/macad2018demo/tarball/v' + __version__,
    license='Apache Software License',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2',
    ],
    keywords='mac',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Geoff Lee',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pylint'],
    author_email='g.lee@ed.ac.uk',
    entry_points={
        'console_scripts': [
           'macad2018demo = macad2018demo.__init__:main'
          ]
    },
)
