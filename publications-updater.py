#!/usr/local/python/bin/python
# -*- coding: utf-8 -*-

# Script to automatically update:
#   the publications page of the NGTS website 
#     (http://ngtransits.org/publications.html)
# with 
#   the publications from the NGTS NASA ADS library
#     (https://ui.adsabs.harvard.edu/public-libraries/DPYuIo9uQN6-4suzkS0Xug)

import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import subprocess

import os
import ads
ads.config.token = 'secret token'


# Change to the correct directory
os.chdir('/Users/sam/Software/NGTS.github.io/pages/tabs')

# Generate a new publications list
fields = ["author", "first_author", "bibcode", "id", "year", "title", "pub", "volume", "page", "bibcode"]
papers = ads.SearchQuery(q="docs(library/DPYuIo9uQN6-4suzkS0Xug)", sort="date desc", rows=2000, fl=fields)

newpubs = '\n'
for paper in papers:
    newpubs += '    <li style="margin-bottom:8px">\n'
    newpubs += '        <a href="https://ui.adsabs.harvard.edu/abs/{}/abstract">{} et al.</a>,\n'.format(paper.bibcode, paper.first_author)
    if paper.volume and paper.page:
       newpubs += '        {}, {}, {}, {}<br>\n'.format(paper.year, paper.pub, paper.volume, paper.page[0])
    elif paper.volume:
       newpubs += '        {}, {}, {}<br>\n'.format(paper.year, paper.pub, paper.volume)
    elif paper.page:
       newpubs += '        {}, {}, {}<br>\n'.format(paper.year, paper.pub, paper.page[0])
    else:
       newpubs += '        {}, {}<br>\n'.format(paper.year, paper.pub)
    newpubs += '        <i>{}</i>\n'.format(paper.title[0])
    newpubs += '    </li>\n\n'

oldpubs_filename = 'publications-old.txt'
newpubs_filename = 'publications-new.txt'
with open(newpubs_filename, "w") as newpubs_:
    newpubs_.write(newpubs)


# If an update is required then do it
# Check for sensible length of newpubs
if len(newpubs) > 5000:
    ## print('newpubs is long enough: {}'.format(len(newpubs)))
    # If the ADS library has been updated (or oldpubs_filename does not exist) then update the publications webpage
    diff = 1
    if os.path.exists(oldpubs_filename):
        ## print('{} exists'.format(oldpubs_filename))
        diff = subprocess.check_output("diff {} {} | wc -l".format(oldpubs_filename, newpubs_filename), shell=True)
        ## print('Difference: {}'.format(diff))
    if diff:
        ## print('There has been an update.')
        os.system("grep -B 10000 '<!-- Start of publications -->' publications_content.html > publications_content-new.html")
        os.system("cat publications-new.txt >> publications_content-new.html")
        os.system("grep -A 10000 '<!-- End of publications -->' publications_content.html >> publications_content-new.html")
        os.system("mv publications_content-new.html publications_content.html")
        os.system("mv publications-new.txt publications-old.txt")
        os.system("git add publications_content.html")
        os.system("git commit -m 'Updated publications_content.html.'")
        os.system("git push")
