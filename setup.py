from distutils.core import setup
setup(
  name = 'Marina-decide',
  packages = ['Marina-decide'], # this must be the same as the name above
  version = '0.10',
  description = 'Decision making tool',
  author = 'Stefan Nožinić',
  author_email = 'stefan@lugons.org',
  url = 'https://github.com/fantastic001/Marina', # use the URL to the github repo
  download_url = 'https://github.com/fantastic001/Marina/tarball/0.10', 
  keywords = ['decision-making', 'scoring', 'organization', 'lifehack'], # arbitrary keywords
  classifiers = [],
  scripts = ["Marina-decide/marina-build", "Marina-decide/marina-decide"],
  install_requires=[] # dependencies listed here 
)