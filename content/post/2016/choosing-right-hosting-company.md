+++
slug = 'choosing-right-hosting-company'
title = 'Choosing the Right Hosting Company'
date = 2016-12-24T00:00:00-00:00
draft = false
type = 'post'
tags = ['Untitled']
+++

<p>Before we get into the post, you need to know there is no right host. Choose what's best for you and or your clients. If you need offshore - get an offshore host, etc... Always do some research and trust your gut instinct as it's rather true. Make sure to ask for support for anything you want to know. If they veer off of the path and don't answer your question - you probably shouldn't choose them as your host.</p>
<p>I tend to look for new hosts quite often as I come up with new project ideas that'll require a good amount of resources, friends need a good solution, or I'm just plain bored. With that being said, when I look for hosts I google stuff like "VPS 1Gbps" or "cheap 1Gbps VPS" etc. When I find a site that looks decent (not built on bootstrap or just some basic HTML template that shows they're not a legit company) I'll actually start looking at their plans. Once I've determined that I like the plans I see I'll start looking at reviews on <a href="http://www.webhostingtalk.com/" target="_blank" rel="noopener">WebHostingTalk</a> and elsewhere.</p>
<p>Once I have a potential host in my sight, I then proceed to look at more to determine which is the best for the price. For example, I rented a cheap vps from <a href="https://virmach.com/" target="_blank" rel="noopener">Virtual Machine Solutions LLC </a>to host my <a href="https://www.teamspeak.com" target="_blank" rel="noopener">Teamspeak 3</a> Server. For $15 /y (2TB @ 1Gbps, 2 Shared vCore, 1GB memory, 30GB HDD, and 5Gbps DDoS protection) you can't really beat that.</p>
<pre class="language-no-highlighting"><code>[root@viper ~]# ./speedtest-cli 
Retrieving speedtest.net configuration... 
Testing from ColoCrossing (&lt;REDACTED&gt;)... 
Retrieving speedtest.net server list... 
Selecting best server based on ping... 
Hosted by ColoCrossing (Buffalo, NY) [0.04 km]: 13.097 ms 
Testing download speed................................ 
Download: 808.40 Mbit/s 
Testing upload speed.................................. 
Upload: 251.97 Mbit/s</code></pre>
<p>Now, before you judge the speed test you need to know what it says in the <a href="https://github.com/sivel/speedtest-cli" target="_blank" rel="noopener">repo</a>.</p>
<blockquote>
<p>It is not a goal of this application to be a reliable latency reporting tool.</p>
</blockquote>
<p>With the speed test not exactly at 1Gbps, I'm not bothered. It's a great speed for the price and after all, it's only a <a href="https://www.teamspeak.com" target="_blank" rel="noopener">Teamspeak 3</a> server.</p>
<p>Back to the review talk. I did do some research before pulling the trigger so to speak and apparently, <a href="https://www.colocrossing.com/" target="_blank" rel="noopener">ColoCrossing</a> supports spammers etc. If that's true (I'm not sure, just going off of some people's information on some forums) then so be it. That's a crap thing to do, but I wanted a cheap server and you get what you pay for.</p>
<h3>Companies I'm with or have been with</h3>
<p>Well, this is a rather long list. I'll list the top 8 since everyone usually does the top 5 or 10, I want to be different. :) <em>(in no particular order)</em></p>
<ul>
<li><a href="https://www.hostgator.com/" target="_blank" rel="noopener">HostGator</a> [1]</li>
<li><a href="https://www.ovh.com/us/" target="_blank" rel="noopener">OVH</a> [2]</li>
<li><a href="https://www.kimsufi.com/us/" target="_blank" rel="noopener">Kimsufi</a> [3]</li>
<li><a href="https://waveride.at/" target="_blank" rel="noopener">Waveride</a> [4]</li>
<li><a href="https://www.server4you.com/" target="_blank" rel="noopener">Server4You</a> [5]</li>
<li><a href="https://www.hetzner.de/" target="_blank" rel="noopener">Hetzner</a> [6]</li>
<li><a href="https://www.limestonenetworks.com/" target="_blank" rel="noopener">Limestone Networks</a> [7]</li>
<li><a href="https://wholesaleinternet.net" target="_blank" rel="noopener">Wholesale Internet</a> [8]</li>
</ul>
<ol>
<li>I left due to them raising the price after 2 1/2 years and I wanted to do everything myself. (security, mail, etc) - They have amazing support and are great for someone wanting to start out with web stuff.</li>
<li>I'm still with them - cheap, reliable, and great</li>
<li>Haven't been with them in ~6 months - cheap and reliable</li>
<li>I've been with them for about a year now and other than the 2TB, it's a great host.</li>
<li>They are an alright host but pulled some sketchy crap with a friend of mine.</li>
<li>I used it for a client one time and they're quite decent.</li>
<li>Great pricing on the cloud servers, but their full dedicated servers are expensive. (compared to companies like OVH) - I keep funds on my account so I can spin up a server at any time to test etc.</li>
<li>Great pricing, amazing and fast support. - IPs /29 are $12 (too expensive imo)</li>
</ol>
<p>I've used other hosts, but they're mostly small sites where I've dumped <a href="https://bitcoin.org/en/" target="_blank" rel="noopener">bitcoin</a> into for a quick tmp VPS, used for misc file hosting, or just a server to host sites that didn't go anywhere. Just always remember to do research before choosing a host.</p>
<p>until next time.</p>