import io
from os import path
from setuptools import setup, find_packages

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='xspamguard',
    version=__import__('xspamguard').__version__,
    description='X-SpamGuard is a command-line utility tool designed for mass muting/blocking engagement spammers on X(twitter).',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='rohsec',
    license='GNU Affero General Public License v3.0',
    url='https://github.com/rohsec/X-SpamGuard',
    download_url='https://github.com/rohsec/X-SpamGuard/archive/v%s.zip' % __import__(
        'xspamguard').__version__,
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Topic :: Security',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'xspamguard = xspamguard.xspamguard:main'
        ]
    },
    keywords=['twitter', 'block', 'blocker', 'twitter mute', 'X blocker', 'user block', 'Twitter']
)