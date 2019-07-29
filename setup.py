from setuptools import setup
setup(
    name = 'Python-Bankstmt-CLI',
    version = '0.1.0',
    packages = ['Bankstmt'],
    entry_points = {
        'console_scripts': [
            'Bankstmt = Bankstmt.__main__:main'
        ]
    })