from setuptools import setup

setup(
    name='gram-scanner',
    version='0.1.0',
    description="A command line interface of Ionian University's Gram-Web",
    author='Nick Garlis',
    author_email='nickgarlis@gmail.com',
    python_requires='>=3',
    url='https://github.com/nickgarlis/gram-scanner',
    py_modules=['gram_scanner'],
    entry_points={
        'console_scripts': ['gram-scanner=gram_scanner:main'],
    },
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
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.6',
    ],
    keywords='Ionian University Gram-Web cli'
)