from setuptools import setup

setup(
    name='argumentum',
    version='1.0b0',
    package_dir={'': 'src'},
    packages=['argumentum'],
    include_package_date=True,
    install_requires=['Flask>=0.12.2', 'Flask-SQLAlchemy>=2.3.2', 'Flask-WTF>=0.14.2'],
    scripts=['src/run_development_server.py', 'src/application.py'],
    url='https://github.com/pjwalen/argumentum',
    license='',
    author='Patrick Walentiny',
    author_email='patrick.walentiny@walentiny.com',
    description='An application for moderating arguments.',
    zip_safe=False,
    test_suite='tests'
)
