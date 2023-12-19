
+++
title = "New Site"
description = "Hugo, GitHub Pages, and some Python"
date = 2023-12-19T00:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

I did it again. I recreated my website. It's not hosted by me anymore nor do I even have a backend. It's using Hugo and GitHub Pages. 

This allows me to write stuff without worrying about security or maintenance of a system/software.

Here's the Python code I wrote to export blog posts over to the Hugo format from Django.

<pre>
import sqlite3
import os.path
import os

import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")
rows = []
with sqlite3.connect(db_path) as db:
    for row in db.execute('SELECT published_date, title, body, slug, keywords, description, is_published FROM posts'):
        data = {
            'is_published': row[6],
            'published_date': row[0],
            'title': row[1],
            'body': row[2],
            'slug': row[3],
            'keywords': row[4],
            'description': row[5],
            }
        # TODO: should check the blog_category table and extract the categories, but it's between 2 tables (thanks Django) and will be a pain to do lookups
        rows.append(data)

for row in rows:
    if not row['is_published']: # don't export hidden posts
        continue
    date = datetime.datetime.strptime(row['published_date'], '%Y-%m-%d %H:%M:%S')
    file = os.path.join(BASE_DIR, f'post/{date.year}/{row['slug']}.md') 
    tags = ['TODO']
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))

    f = open(file, "w", encoding="utf-8")
    f.write(f"""
+++
title = "{row['title']}\"
description = "{row['description']}"
date = {date.strftime('%Y-%m-%dT%H:%M:%SZ')}
draft = false
type = \'post\'
tags = {tags}
old_content_duration = 0
+++

{row['body']}
    """)
    f.close()

</pre>

<p>until next time</p>
    