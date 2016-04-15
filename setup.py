import os
import subprocess
from setuptools import setup, find_packages


class NoGitVersionFound(Exception):
    pass

#requirements.txt
with open('requirements.txt') as f:
  required = f.read().splitlines()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
    git_version = subprocess.check_output(['git','describe']).rstrip()
    if not git_version:
        raise NoGitVersionFound("No git tag found")
    return git_version

__author__ = 'Josue Kouka'
__email__ = 'josuebrunel@gmail.com'
__version__ = get_version()

setup(
  name = "logged_requests",
  version = __version__,
  description = "Simple wrapper around the requets library",
  long_description = read("README.rst"),
  author = __author__,
  author_email = __email__,
  url = "https://github.com/josuebrunel/logged-requests",
  download_url = "https://github.com/josuebrunel/logged-requests/archive/{0}.tar.gz".format(__version__),
  keywords = ['requests', 'logging', 'log', 'logger', 'logged requests'],
  packages = find_packages(),
  classifiers = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License'
  ],
  platforms=['Any'],
  license='MIT',
  install_requires = required
)
