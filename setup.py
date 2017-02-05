from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup(
    name='pacman3d',
    version='0.0.1',
    author='Fritz Heiden, Kilian Wutzke',
    author_email='..., s0545665@htw-berlin.de',
    description='Pacman in 3d with pygame',
    license='MIT',
    packages=['pacman3d'],
    data_files=[('', ['data/maze.txt'])],
    long_description=('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games'
    ]
)
