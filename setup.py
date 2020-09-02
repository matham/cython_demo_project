from setuptools import setup, Extension, find_packages
from io import open
from os.path import dirname, join
from os import path
from Cython.Distutils import build_ext
from cython_demo_project import __version__

URL = 'https://github.com/matham/cython_demo_project'

src_path = build_path = dirname(__file__)

with open(path.join(src_path, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

cmdclass = {'build_ext': build_ext}

ext_modules = [Extension(
    'cython_demo_project.numeric',
    sources=[join(src_path, 'cython_demo_project', 'numeric.pyx')])
]

for e in ext_modules:
    e.cython_directives = {"embedsignature": True, 'language_level': 3}

setup(
    name='cython_demo_project',
    version=__version__,
    description='A simple Cython demo project with GitHub CI.',
    long_description=long_description,
    url=URL,
    author='Matthew Einhorn',
    author_email='moiein2000@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    setup_requires=['cython'],
    install_requires=[],
    extras_require={
        'dev': ['pytest>=3.6', 'wheel', 'sphinx-rtd-theme', 'sphinx'],
    },
    package_data={'cython_demo_project': ['*.pxd']},
    data_files=[],
    entry_points={},
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    project_urls={
        'Bug Reports': URL + '/issues',
        'Source': URL,
    },
)
