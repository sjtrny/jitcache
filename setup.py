# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

# Get the long description from the README file
with open(path.join(path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name = "jitcache",
    version = "0.1",
    description = "jitcache is a just-in-time key-value cache that is thread/process safe",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/sjtrny/jitcache',
    author = 'Stephen Tierney',
    author_email = 'sjtrny@gmail.com',
    keywords = 'cache jit key value dictionary thread process',
    py_modules=['jitcache'],
    install_requires=[],
    python_requires='>=3',
    classifiers = [
        'License :: OSI Approved :: MIT License',
      ]
)