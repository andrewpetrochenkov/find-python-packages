import setuptools

setuptools.setup(
    name='find-python-packages',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/find-python-packages']
)
