from setuptools import setup, find_packages

setup(
  name='gram-scanner',
  version='1.0.0',
  description="A command line interface of Ionian University's Gram-Web",
  author='Nick Garlis',
  author_email='nickgarlis@gmail.com',
  python_requires='>=3',
  url='https://github.com/nickgarlis/gram-scanner',
  packages=find_packages(exclude=('bin')),
  scripts=['bin/gram-scanner'],
  install_requires=[
    'click',
    'bs4',
    'halo',
    'colorama',
    'requests'
  ],
  include_package_data=True,
  license='MIT',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.6',
  ],
  keywords=['Ionian University', 'Gram-Web' 'gram-scanner']
)