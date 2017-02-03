from setuptools import setup

setup(
    name='pacman-3d',
    modules=['core'],
    install_requires=[
        'PyOpenGL',
        'pygame==1.9.2'
    ]
)
