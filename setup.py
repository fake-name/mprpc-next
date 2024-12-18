# -*- coding: utf-8 -*-

from setuptools import setup, Extension

setup(
    name='mprpc',
    version='0.2.0',
    description='A fast MessagePack RPC library',
    long_description=open('README.rst').read(),
    author='Studio Ousia',
    author_email='ikuya@ousia.jp',
    url='http://github.com/studio-ousia/mprpc',
    packages=['mprpc'],
    ext_modules=[
        Extension('mprpc.client', ['mprpc/client.c']),
        Extension('mprpc.server', ['mprpc/server.c'])
    ],
    license=open('LICENSE').read(),
    include_package_data=True,
    keywords=['rpc', 'msgpack', 'messagepack', 'msgpackrpc', 'messagepackrpc',
              'messagepack rpc', 'gevent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'gsocketpool',
        'gevent',
        'msgpack-python',
    ],
    tests_require=[
        'nose',
        'mock',
    ],
    test_suite = 'nose.collector'
)
