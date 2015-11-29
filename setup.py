from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: add any additional package requirements here
    'charlesbot',
]

test_requirements = [
    # TODO: add any additional package test requirements here
    'asynctest',
    'coverage',
    'flake8',
]

setup(
    name='charlesbot-jira',
    version='0.1.0',
    description="Charlesbot Jira plugin",
    long_description=readme,
    author="Marvin Pinto",
    author_email='marvin@pinto.im',
    url='https://github.com/marvinpinto/charlesbot-jira',
    packages=[
        'charlesbot_jira',
    ],
    package_dir={'charlesbot_jira':
                 'charlesbot_jira'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='slack robot chatops charlesbot charlesbot-jira',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
