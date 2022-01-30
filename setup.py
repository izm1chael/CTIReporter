from setuptools import setup, find_packages


print(find_packages())

setup(
    name='CTIReporter',
    version='1.0',
    description='A simple report manager for cyber threat intellegence',
    author='Mike Johnson',
    url='https://github.com/izm1chael/CTIReporter',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>3.7',
    install_requires=[
        'Flask>=0.9',
        'Click>=6,<7',
        'Flask-Login>=0.4',
        'Flask-WTF>=0.8',
        'Markdown>=2.2.0',
        'Pygments>=1.5',
        'WTForms>=1.0.2',
        'Werkzeug>=0.8.3',
        'python-markdown-math'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock'],
    entry_points={
        'console_scripts': [
            'wiki=wiki.cli:main'
        ]
    }
)
