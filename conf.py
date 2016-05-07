# -*- coding: utf-8 -*-



import sys, os
project = u'Sphinx 使用手册'
copyright = u''
version = u''
release = u''

source_suffix = '.rst'

master_doc = 'contents'

#language = 'en_US'
language = 'zh_CN'

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

# Follow added by supergis,to support PDF output and chinese character.
# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',

#\\usepackage[english]{babel}
'preamble': '''
\\hypersetup{unicode=true}
#\\usepackage{CJKutf8}
\\AtBeginDocument{\\begin{CJK}{UTF8}{gbsn}}
\\AtEndDocument{\\end{CJK}}
'''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'sphinx.tex', 'sphinx Documentation',
     'openthings', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sphinx', 'sphinx Documentation',
     'supergis', 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'sphinx', 'sphinx Documentation',
     'supergis', 'sphinx', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for PDF output --------------------------------------------------
 
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.
 
pdf_documents = [
    ('index', u'HanLP Handbook', u'HanLP Handbook', u'hankcs'),
]
 
# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['a3','zh_CN']
 
# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
#pdf_compressed = False
 
# A colon-separated list of folders to search for fonts. Example:
#pdf_font_path = ['C:\\Windows\\Fonts']
 
# Language to be used for hyphenation support
pdf_language = "zh_CN"
 
# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
pdf_fit_mode = "shrink"
 
# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
#pdf_break_level = 0
 
# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'
 
# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True
 
# verbosity level. 0 1 or 2
#pdf_verbosity = 0
 
# If false, no index is generated.
#pdf_use_index = True
 
# If false, no modindex is generated.
#pdf_use_modindex = True
 
# If false, no coverpage is generated.
#pdf_use_coverpage = True
 
# Documents to append as an appendix to all manuals.
#pdf_appendices = []
 
# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False
 
# Set the default DPI for images
#pdf_default_dpi = 72
 
# Enable rst2pdf extension modules (default is only vectorpdf)
# you need vectorpdf if you want to use sphinx's graphviz support
#pdf_extensions = ['vectorpdf']
 
# Page template name for "regular" pages
#pdf_page_template = 'cutePage'
 
# Show Table Of Contents at the beginning?
# pdf_use_toc = False
 
# How many levels deep should the table of contents be?
pdf_toc_depth = 2
 
# Add section number to section references
pdf_use_numbered_links = False
 
# Background images fitting mode
pdf_fit_background_mode = 'scale'

