from distutils.core import setup
setup(
  name = 'Marina-decide',
  packages = ['Marina_decide'], # this must be the same as the name above
  version = '0.16',
  description = 'Decision making tool',
  package_dir = {'Marina_decide': 'lib'},
  author = 'Stefan Nožinić',
  author_email = 'stefan@lugons.org',
  url = 'https://github.com/fantastic001/Marina', # use the URL to the github repo
  download_url = 'https://github.com/fantastic001/Marina/tarball/0.16', 
  keywords = ['decision-making', 'scoring', 'organization', 'lifehack'], # arbitrary keywords
  classifiers = [],
  scripts = ["marina-build", "marina-decide"],
)
