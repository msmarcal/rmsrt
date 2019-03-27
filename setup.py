from pathlib import Path
from setuptools import setup

README = Path('README.md').open('r').read()
REQUIREMENTS = Path('requirements.txt').open('rt').read().strip().split('\n')
VERSION = open(Path('VERSION.txt')).read().strip()

setup(
    name='rmsrt',
    version=VERSION,
    description='Remove orphan srt subtitle files from a given directory ',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Marcelo Subtil Marcal',
    author_email='marcelo@smarcal.com',
    url='https://github.com/msmarcal/rmsrt',
    license='MIT',
    py_modules=['rmsrt'],
    packages=['rmsrt'],
    keywords='srt,subtitle',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=REQUIREMENTS,
    python_requires='~=3.6',
    entry_points='''
      [console_scripts]
      rmsrt=rmsrt:cli
      ''',
)
