from setuptools import setup, find_packages

with open("README.md","r") as fh:
  long_description =fh.read()

setup(
  name = 'subhashree',
  packages = find_packages(),
  version = '0.0.1',
  description = 'Only for testing purpose',
  author = 'Subhashree Tripathy',
  author_email="subhashree.tripathy@reverieinc.com",
  url="https://github.com/Subhashree-Tripathy/testM",
  classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
  ],
  python_requires='>=3.5'
)
