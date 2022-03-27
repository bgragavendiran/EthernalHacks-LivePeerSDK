from setuptools import setup, find_packages

setup(
    name='LivePeerPython',
    version='0.3',
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
    long_description_content_type='text/x-rst',
    long_description='README.md',
    python_requires='>=3'
)
