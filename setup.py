from setuptools import find_packages, setup

setup(
    name = 'ML',
    version='0.0.1',
    author='Saurabh',
    author_email='sorabh.tanwar17@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'seaborn']
)