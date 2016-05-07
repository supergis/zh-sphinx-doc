# -*- coding: utf-8 -*-



import sys, os
project = u'Sphinx 使用手册'
copyright = u''
version = u''
release = u''

source_suffix = '.rst'
master_doc = 'contents'
language = 'en_US'
exclude_patterns = ['_build']
extensions = ['sphinx.ext.pngmath']
pygments_style = 'sphinx'

html_title = u'Sphinx 使用手册'

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    try:
        import sphinx_rtd_theme
    except ImportError:
        html_theme = 'default'
        html_theme_path = []
    else:
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

#html_theme = 'haiku'
#html_theme = 'sphinx_rtd_theme'

        
html_theme_path = ['../../../templates/sphinx', ]
htmlhelp_basename = 'sphinx'
html_add_permalinks = None

file_insertion_enabled = False
latex_documents = [
  ('index', 'sphinx.tex', u'Sphinx 使用手册',
   u'', 'manual'),
]

exclude_patterns = ['README.rst']

#Add sponsorship and project information to the template context.
context = {
    'MEDIA_URL': "/media/",
    'slug': 'sphinx',
    'name': u'sphinx使用手册',
    'analytics_code': 'None',
}

html_context = context

