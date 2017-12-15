from setuptools import setup

requires = [
    'flask',
    'flask_appbuilder',
    'marshmallow',
    'alembic',
    'marshmallow_sqlalchemy',
    'flask_migrate'
]

setup(
    name='reqsteady',
    version='0.1',
    include_package_data=True,
    packages=['reqsteady'],
    zip_safe=False,
    install_requires=requires
)
