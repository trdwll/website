
+++
title = "Using GoAccess"
description = "A fast web log analyzer and interactive viewer."
date = 2020-12-16T09:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p><strong>UPDATE: I recently changed from a crontab to using the websocket and it works great. This <a href="https://ansonvandoren.com/posts/goaccess-nginx-auth/" target="_blank" rel="noopener">post</a> was extremely useful when setting up the websocket. (also some nginx info around the web)<br /></strong></p>
<pre class="language-markup"><code>goaccess /var/log/nginx/access.log -o /var/www/report.html --log-format=COMBINED --real-time-html --ws-url=wss://domain:443/ws --port 7890 --daemon</code></pre>
<p>&nbsp;</p>
<p>This year I built a <a href="https://trdwll.com/experiments/django-analytics/" target="_blank" rel="noopener">middleware</a> for <a href="https://djangoproject.com" target="_blank" rel="noopener">Django</a> to store data on visitors to websites. It would store things like the page they view, the site that referred them, and their IP address/country. This worked fine for the longest time, but it's very redundant since I already have this information in my <a href="https://nginx.org/" target="_blank" rel="noopener">Nginx</a> (HTTP server) logs and it was stored in my database for my website. I still have one model (table) that I store just to keep a copy of it in case I delete the logs from <a href="https://nginx.org/" target="_blank" rel="noopener">Nginx</a>.</p>
<p>Before you start getting paranoid just know, an IP address isn't private and all websites that you access usually have logs enabled to help debug issues to seeing when a bad guy tries to access things. Just to put your mind at ease I don't give out any of my data and nor will I ever.</p>
<p>&nbsp;</p>
<h3>GoAccess</h3>
<p>I started building out a dashboard that was going to be like <a href="https://goaccess.io/" target="_blank" rel="noopener">GoAccess</a> - that was until I found <a href="https://goaccess.io/" target="_blank" rel="noopener">GoAccess</a>. My version was going to be such shit compared to <a href="https://goaccess.io/" target="_blank" rel="noopener">GoAccess</a>.</p>
<p>Installing GoAccess is very simple. They have <a href="https://goaccess.io/download" target="_blank" rel="noopener">packages</a> that you can fetch and their <a href="https://goaccess.io/get-started" target="_blank" rel="noopener">getting started</a> page is very simple to follow, they even have a <a href="https://goaccess.io/man" target="_blank" rel="noopener">manpage</a>.</p>
<p>The way that I'm using GoAccess is via a <a href="https://crontab.guru/" target="_blank" rel="noopener">cron</a> instead of their <a href="https://en.wikipedia.org/wiki/WebSocket" target="_blank" rel="noopener">WebSocket</a> server. This probably isn't the best way, but it's the method that works for me.</p>
<pre class="language-markup"><code>*/10 * * * * goaccess /var/log/nginx/access.log -o /var/www/report.html --log-format=COMBINED</code></pre>
<p>One thing I really can't wait for is the <a href="https://github.com/allinurl/goaccess/issues/117" target="_blank" rel="noopener">filtering</a> <a href="https://github.com/allinurl/goaccess/issues/1167" target="_blank" rel="noopener">option</a>. This feature will completely change everything.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>until next time</p>
    