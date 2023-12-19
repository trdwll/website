+++
title = 'Hidden Backup Server'
date = 2017-07-19T00:00:00-00:00
draft = false
type = 'post'
tags = ['Guide', 'Technical', 'Privacy']
old_content_duration = 0
+++

<p>Been a while, eh?</p>
<p>I&rsquo;ve been needing an offsite backup solution and recently I found a VPS provider that had an amazing deal on storage that I couldn&rsquo;t pass up. Prior to renting this new VPS I just pulled certain files every month or whatever, but I had a cron running every 6 hours backing up everything. This wasn&rsquo;t the best idea, but it worked.</p>
<p>Now that I have a dedicated vps for backups I can actually do proper backups of imglnx, my other projects, and personal data.</p>
<p>Instead of using <a href="http://duplicity.nongnu.org/" target="_blank" rel="noopener">duplicity</a> for backups, I decided to do it my own way via <a href="http://www-hep2.fzu.cz/computing/adm/sftp.html" target="_blank" rel="noopener">sftp</a>, <a href="https://www.gnupg.org/" target="_blank" rel="noopener">gpg</a>, and <a href="https://torproject.org" target="_blank" rel="noopener">tor</a>. So let's get into this!</p>
<p>Backup server:</p>
<pre class="language-no-highlighting"><code>root@yolotrain:~# sudo apt-get install tor 
root@yolotrain:~# vi /etc/tor/torrc 
HiddenServiceDir /var/lib/tor/hiddenservicename/ 
HiddenServicePort 22 127.0.0.1:22 
HiddenServiceAuthorizeClient stealth name1 
root@yolotrain:~# systemctl enable tor 
root@yolotrain:~# systemctl start tor 
root@yolotrain:~# cat /var/lib/tor/hiddenservicename/hostname 
myonionnamegoeshere.onion randomstringhere # client: name1</code></pre>
<p>Host/Server you want to backup:</p>
<pre class="language-no-highlighting"><code>root@awesomecrack:~# sudo apt-get install tor 
root@awesomecrack:~# vi /etc/tor/torrc 
HidServAuth myonionnamegoeshere.onion randomstringhere # client: name1 
root@awesomecrack:~# systemctl enable tor 
root@awesomecrack:~# systemctl start tor 
root@awesomecrack:~# vi .ssh/config 
host hidden 
hostname myonionnamegoeshere.onion 
proxycommand ncat --proxy 127.0.0.1:9050 --proxy-type socks5 %h %p</code></pre>
<p>Then you can just do &ldquo;ssh hidden&rdquo; on your host server.</p>
<p>I also have a bash script to go zip directories, gpg encrypt them, then <code>scp -i keyfile.key file.gpg username@hidden:backup-dir</code>. The gpg key I&rsquo;m using was generated on my desktop and all I did was import the public key on the server I want to backup, so I can encrypt the backup before sending it off to the backup server.</p>
<p>NOTE: If I did something incorrectly or insecure here please notify me about it. (Still a bit new to messing with hidden services.)</p>
<p>&nbsp;</p>
<p>until next time</p>