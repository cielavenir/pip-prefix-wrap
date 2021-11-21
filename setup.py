
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='enum34',
    version="2.0.0",
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    description='fake enum34 redirecting to aenum',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cielavenir/enum34-aenum-proxy',
    keywords='enum enum34 aenum',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    packages=setuptools.find_packages(),
    python_requires=">=2.7, <3.4",
    install_requires=[
        'aenum',
    ],
)
