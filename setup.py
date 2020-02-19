from setuptools import setup

setup(
	name='OWL_Stats',
	version='0.0',
	description='Package for parsing, filtering, and displaying stats for Overwatch League.',
	author="squidonthebass",
	author_email="squidonthebass@protonmail.com",
	packages='OWL_Stats',
	license='gpl-3.0',
	install_requires=['csv','matplotlib']
)