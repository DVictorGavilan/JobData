from setuptools import setup, find_packages

setup(
    name='job_data',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'beautifulsoup4'
        "essentialkit"
    ],
    entry_points={
        'console_scripts': [
            'job_data=job_data.main:main',
        ],
    },
    author='VTech Solutions',
    author_email='contacto@vtech.com',
    description='Job Data analysis from TecnoEmpleo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DVictorGavilan/JobData'
)
