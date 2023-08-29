from setuptools import setup, find_packages

setup(
    name='disposable-mail-checker',
    version='1.0.0',
    description='Check if an email address uses a disposable domain',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Codemonk',
    author_email='devansh.jha@codemonk.in',
    url='https://github.com/CodemonkHQ/disposable-mail-checker',
    packages=find_packages(),
    package_data={'disposable_mail_checker': ['disposable_domains.json']},
    install_requires=[

    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)