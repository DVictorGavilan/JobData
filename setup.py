from setuptools import setup, find_packages

setup(
    name='job_data',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'job_data=job_data.main:main',
        ],
    },
    author='VTech Solutions',
    author_email='contacto@vtech.com',
    description='Una breve descripción de tu proyecto',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DVictorGavilan/JobData'
)