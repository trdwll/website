+++
title = 'Installing Python 3 on CentOS 7'
date = 2019-10-15T00:00:00-00:00
draft = false
type = 'post'
tags = ['Guide', 'Technical']
+++

<p>CentOS 7 ships with 2.7.5 and that's not the best when you're wanting to use Python 3.x so I'm going to teach you how to install 3.x.</p>
<p>This will work for any python version so you don't have to use 3.7.5 like I did here. You can go and use the latest instead.</p>
<ol>
<li>Run <code>python -V</code> and see what it says. If it's not 3.x then continue to step 2.</li>
<li>Run <code>whereis python</code>, if you don't see any python3.x binaries then continue to step 3.</li>
<li>Run as root/sudo <code>yum groupinstall -y "Development Tools"</code> then run <code>yum install gcc openssl-devel bzip2-devel libffi-devel -y</code></li>
<li>Jump on over to the Python <a href="https://www.python.org/downloads/source/" target="_blank" rel="noopener">download page</a> and find the link for the Gzipped source tarball. For this guide we're going to be installing <a href="https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz" target="_blank" rel="noopener">3.7.5</a>.</li>
<li>Run <code>wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz</code> or upload the source to the machine.</li>
<li>Once the source is on the machine then run <code>tar -xvzf Python-3.7.5.tgz</code>.</li>
<li>Run <code>cd Python-3.7.5/</code> and then run <code>./configure --enable-optimizations</code></li>
<li>Now that you've configured the build for Python you can build and install it by doing <code>make altinstall</code>. <strong>This process will take some time so let it run. You don't want to do <code>make install</code>, because this will mess with Python 2 which is required by most of the components of CentOS 7.</strong></li>
<li>Python 3.x should be installed now so now you can do <code>python3.x -V</code> (in this guide should be <code>python3.7 -V</code>)</li>
</ol>
<p>&nbsp;</p>
<p>Upgrading from 3.7.5 to 3.7.6 or another version will be the same as above, but you'll go and delete the previous version before you start.</p>
<p>Run <code>whereis python</code> and then you'll delete the previous verison files.</p>
<pre>rm -rf /usr/local/lib/python3.7
rm -rf /usr/local/bin/python3.7m 
rm -rf /usr/local/bin/python3.7 
rm -rf /usr/local/bin/python3.7m-config</pre>
<p>&nbsp;</p>
<p>Note: If you're going to be using sqlite or any database then you need to install it also and the devel package. For example (sqlite-devel mariadb mariadb-server mariadb-devel).</p>
<p>&nbsp;</p>
<p>until next time</p>