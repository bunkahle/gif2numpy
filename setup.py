#!/usr/bin/env python
from distutils.core import setup

setup(
    name='gif2numpy',
    version='1.3',
    author='Andreas Bunkahle',
    author_email='abunkahle@t-online.de',
    description='Convert single and multiple frame gif images to numpy images or to OpenCV without PIL or pillow',
    license='MIT',
    py_modules=['gif2numpy'],
    python_requires='>=2.7',
    url='https://github.com/bunkahle/gif2numpy',
    long_description=open('README.md').read(),
    platforms=['any'],
    install_requires=['numpy', 'kaitaistruct'],
    keywords = 'GIF Converter Numpy',
    classifiers=[    
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
