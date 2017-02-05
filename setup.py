from setuptools import setup

setup(
    name='pacman3d',
    version='0.0.1',
    author='Fritz Heiden, Kilian Wutzke',
    author_email='..., s0545665@htw-berlin.de',
    description='Pacman in 3d with pygame',
    license='MIT',
    packages=['pacman3d'],
    package_data={'pacman3d': ['license.txt']},
    long_description=('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games'
    ]
)
