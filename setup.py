from setuptools import setup, find_packages

setup(
    name='temaMaterialLorena',
    version='1.0.0',
    packages=['temaMaterialLorena', 'temaMaterialLorena.extensions', 'temaMaterialLorena.plugins', 'temaMaterialLorena.templates'],
    include_package_data=True,
    package_data={
        'temaMaterialLorena': ['templates/*', 'templates/**/*'],
    },
    install_requires=[
        'mkdocs-material',
    ],
    entry_points={
        'mkdocs.themes': [
            'temaMaterialLorena = temaMaterialLorena.templates',
        ],
        'mkdocs.plugins': [
            'temaMaterialLorena/enviorment = temaMaterialLorena.plugins.enviorment:EnviormentPlugin',
            'temaMaterialLorena/functions = temaMaterialLorena.plugins.functions:FunctionsPlugin',
            'temaMaterialLorena/sectionicons = temaMaterialLorena.plugins.sectionicons:SectionIconsPlugin',
        ],
    },
)
