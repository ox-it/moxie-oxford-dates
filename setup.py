from setuptools import setup, find_packages


install_requires = open('requirements.txt').readlines()

setup(name='moxie-oxford-dates',
    version='0.2',
    packages=find_packages(),
    description='Oxford dates module for Moxie',
    author='Mobile Oxford',
    author_email='mobileoxford@oucs.ox.ac.uk',
    url='https://github.com/ox-it/moxie-oxford-dates',
    include_package_data=True,
    setup_requires=["setuptools"],
    install_requires=install_requires,
    test_suite="moxie_oxford_dates.tests",
)
