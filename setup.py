from setuptools import setup, find_packages

setup(
    name='foggysounds',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Django database backend driver for Mnesia (Erlang)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Eddy',
    author_email='eddyraz.fl@proton.me',
    url='https://github.com/MIRALIASOFTWARE/foggysounds',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[],
)
