
from setuptools import setup, find_packages


setup(
    name='LivePeerSDKPython',
    version='0.1',
    license='MIT',
    author="Ragavendiran Balasubramanian",
    author_email='bgragavendiran@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'LivePeerSDKPython'},
    url='https://github.com/RAGANITHI/EthernalHacks-LivePeerSDK',
    keywords='LivePeerSDKPython',
    install_requires=[
          'requests'
      ],
    python_requires='>=3'
)