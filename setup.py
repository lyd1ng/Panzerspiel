from distutils.core import setup

setup(
    name='Panzerspiel',
    version='0.9',
    packages=['panzerspiel', ],
    license='GNU General Public License v3.0',
    install_requires=['pygame']
    long_description=open('README.md').read(),
    include_package_data=True,
    package_data={'panzerspiel': ['res2/*.*', 'res2/music/*.mp3']},
    entry_points={
        'console_scripts': ['panzerspiel = panzerspiel.main:main']}
)
