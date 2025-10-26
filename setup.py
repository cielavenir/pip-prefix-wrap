
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pip-prefix-wrap',
    version="1.0.0",
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    description='patch pip scheme to posix_prefix',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cielavenir/pip-prefix-wrap',
    keywords='pip',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.11",  # only applies to something with PEP 668
    install_requires=[
        # 'setuptools',
    ],
)
