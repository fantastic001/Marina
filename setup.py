from distutils.core import setup
setup(
  name = 'Marina-decide',
  packages = ['Marina-decide'], # this must be the same as the name above
  version = '0.12',
  description = 'Decision making tool',
  package_dir = {'Marina-decide': 'lib'},
  author = 'Stefan Nožinić',
  author_email = 'stefan@lugons.org',
  url = 'https://github.com/fantastic001/Marina', # use the URL to the github repo
  download_url = 'https://github.com/fantastic001/Marina/tarball/0.12', 
  keywords = ['decision-making', 'scoring', 'organization', 'lifehack'], # arbitrary keywords
  classifiers = [],
  scripts = ["marina-build", "marina-decide"],
)
