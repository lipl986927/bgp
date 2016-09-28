from setuptools import find_packages, setup

VERSION = 0.1

scapy_package = 'scapy-python3' if sys.version_info.major==3 else 'scapy'

setup(name="Bgp",
      version=VERSION,
      description="A python stack to test bgp",
      author="Sudarshana K S",
      author_email='sudarshana.ks@gmail.com',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="BSD",
      url="http://github.com/sudks/bgp",
      packages=find_packages(),
      install_requires=[scapy_package],
      download_url='https://github.com/sudks/bgp/tarball/' + VERSION,
      keywords=['tcp','bgp', 'scapy', 'network', 'dissect', 'packets']
      )
