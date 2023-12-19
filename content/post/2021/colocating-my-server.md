
+++
title = "Colocating My Server"
description = "I colocated my server!"
date = 2021-12-20T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>Colocating a server is something that I've wanted to do for a long time and I just never have until now. Over the years I've had numerous machines that I could've easily colocated (several 1U machines), but it has been too expensive. <a href="https://joesdatacenter.com" target="_blank" rel="noopener">JoesDatacenter</a> has been around for a long time - even before I started my home lab, but it was a matter of shipping the server(s) or driving to Kansas City, MO. Driving is exactly what we did. Oh yeah, I decided to take my mom with me as a 3-day vacation - since she needed time away from our city also. During the trip, I was able to stop and meet one of our staff and I even gave him 4 of my old monitors (the 6 1080p monitors) as I wasn't using them. The round trip cost me ~$700 and 3 days. I could've shipped the server for much cheaper, but I'd rather take it to the data center and have a mini-vacation - plus our staff member wouldn't have got free monitors so I'm fine with the cost. I even stopped to visit with my brother and give him my old pc case (W200) and 2 monitors.</p>
<p>Even though I colocated my server I'm still going to use a couple of VPS's and Google Cloud for file sharing.</p>
<p>&nbsp;</p>
<h3>Upgrading the Server</h3>
<p>I decided to upgrade some components of this server before colocating it so I could benefit the most from it. Before you give me shit about colocating this older machine instead of building a new one let me explain. I already had this machine from last year and spent ~$1.2k on it. So yeah for that price plus the additional ~$700 I just put into it I could've built something decent with modern hardware, but I wouldn't have had 512GB of ram or 20 cores/40 threads.</p>
<p>&nbsp;</p>
<p><a href="https://files.trdwll.net/2021/11/server1.png"><img src="https://files.trdwll.net/2021/11/server1.png" width="367" height="490" /></a>&nbsp;<a href="https://files.trdwll.net/2021/11/server2.png"><img src="https://files.trdwll.net/2021/11/server2.png" width="367" height="490" /></a>&nbsp;<a href="https://files.trdwll.net/2021/11/server3.png"><img src="https://files.trdwll.net/2021/11/server3.png" width="367" height="490" /></a>&nbsp;<a href="https://files.trdwll.net/2021/11/server4.png"><img src="https://files.trdwll.net/2021/11/server4.png" width="367" height="490" /></a></p>
<p>&nbsp;</p>
<p>Upgrades</p>
<ul>
<li>CPUs - <a href="https://ark.intel.com/content/www/us/en/ark/products/75272/intel-xeon-processor-e52660-v2-25m-cache-2-20-ghz.html" target="_blank" rel="noopener">E5-2660 V2</a> to <a href="https://ark.intel.com/content/www/us/en/ark/products/75279/intel-xeon-processor-e52690-v2-25m-cache-3-00-ghz.html" target="_blank" rel="noopener">E5-2690 V2</a>.
<ul>
<li>These CPUs are basically the exact same with the exception of the frequency - I really wish I didn't drop $150 on the 2660 V2's a year ago and would've just bought the 2690 V2's.</li>
</ul>
</li>
<li>Storage <br />
<ul>
<li>I figured since the machine is going to be colocated I might as well upgrade/replace the drives.</li>
<li>Removed 2x 1TB HDD</li>
<li>Removed 3x 3TB HDD (was in Raid 1 and Raid 0)</li>
<li>Added 2x 1TB NVMe SSD in Raid 1<br />
<ul>
<li>I plan to upgrade these to 2TB eventually, but the other $200 will have to wait as I've spent too much money already. 😅</li>
</ul>
</li>
<li>Added 1x 1TB NVMe SSD in Raid 0
<ul>
<li>Was pulled from my old i7 workstation</li>
</ul>
</li>
<li>Added 2x 250GB 2.5" SSD in Raid 1<br />
<ul>
<li>OS boot drive</li>
</ul>
</li>
<li>Added 8x 4TB HDD in Raid 6</li>
</ul>
</li>
<li>CPU Coolers
<ul>
<li>The coolers I had in the server were the <a href="https://www.newegg.com/cooler-master-hyper-212-evo-rr-212e-20pk-r2/p/N82E16835103099" target="_blank" rel="noopener">Cooler Master Hyper 212 EVO</a> and they are a pain in the ass to add/remove so I upgraded to the <a href="https://store.supermicro.com/2u-active-cpu-cooler-snk-p0048ap4.html" target="_blank" rel="noopener">Supermicro SNK-P0048AP4</a>.</li>
<li>I probably could've gone with a larger 4U cooler, but the machine is in a data center so there's enough cooling already.</li>
<li>I know these are literally for rack mount, but they work quite well so fuck it.</li>
</ul>
</li>
</ul>
<p>The NVMe drives are speed capped at 2Gb/s due to them being in PCIe 2 x4 slots - it's still faster than a standard HDD and SSD so I'll take it.</p>
<p>If you're curious about the server I posted about it <a href="https://trdwll.com/blog/new-server-new-network/">here</a>.</p>
<p>I also dusted the hell out of it before moving it to the dc. 😀I removed the front USB and audio jacks as I don't need them - and *insert paranoia* tbh I don't want someone walking by and plugging something in while they work on their server etc.</p>
<p><span style="text-decoration: underline;"><a href="https://files.trdwll.net/2021/11/20211117_200302.png"><img src="https://files.trdwll.net/2021/11/20211117_200302.png" width="367" height="490" /></a></span></p>
<p>Since these pictures were taken I replaced the 3x 3TB HDD (first 3 drives) with 4x 4TB HDD to pair with the other 4 as a raid 5 array.</p>
<p>&nbsp;</p>
<h3>Setup</h3>
<p>Now that the server has been upgraded I went ahead and started configuring my VMs and the network. I placed the order for the subnet and added the subnet to the server so when it's added to the datacenter and powered on everything will just work... right?</p>
<p>The tech that was there when I installed the server helped me for about an hour to configure my network and get it up. I had an issue establishing an uplink so I was unable to access the server remotely. I also ran into some issues internally that I won't talk about as it's regarding security, but it's all resolved now.</p>
<p>I was on a time crunch so I didn't ask if I could take some photos, but I had to take a photo of my interface's config so here's that.</p>
<p><a href="https://files.trdwll.net/2021/12/220211211_143839.jpg"><img src="https://files.trdwll.net/2021/12/220211211_143839.jpg" width="300" height="400" /></a></p>
<p>&nbsp;</p>
<p>I chose <a href="https://joesdatacenter.com" target="_blank" rel="noopener">JoesDatacenter</a> mainly due to price, but around the internet people seem to recommend them, but I haven't been able to find any colocation reviews. <em>(I'll post a review after some time has passed.)</em> I didn't need unlimited bandwidth or a ton of additional features that most colocation companies provide.</p>
<p>&nbsp;</p>
<h3>The Trip</h3>
<p>The trip was very long and if I ever go by car for 10+ hours I think I'll spread it out longer.</p>
<p>If you are ever in the St. Louis area you should stop by Gingham's Homestyle Restaurant in St. Charles. Their food was really good and reminded me of Waffle House. $51+$10 tip for 3 people so it's a bit on the high side, but it was worth it.</p>
<p>&nbsp;</p>
<p><a href="https://files.trdwll.net/2021/12/XMkqLp.jpg" target="_blank" rel="noopener"><img src="https://files.trdwll.net/2021/12/XMkqLp.jpg" width="367" height="488" />&nbsp;</a><a href="https://files.trdwll.net/2021/12/zVqx9H.jpg" target="_blank" rel="noopener"><img src="https://files.trdwll.net/2021/12/zVqx9H.jpg" width="367" height="488" /></a><a href="https://files.trdwll.net/2021/12/XMkqLp.jpg" target="_blank" rel="noopener">&nbsp;</a><a href="https://files.trdwll.net/2021/12/5AJH3P.jpg" target="_blank" rel="noopener"><img src="https://files.trdwll.net/2021/12/5AJH3P.jpg" width="367" height="488" /></a><a href="https://files.trdwll.net/2021/12/XMkqLp.jpg" target="_blank" rel="noopener">&nbsp;</a><a href="https://files.trdwll.net/2021/12/6Hoxi6.jpg" target="_blank" rel="noopener"><img src="https://files.trdwll.net/2021/12/6Hoxi6.jpg" width="367" height="488" /></a>&nbsp;<a href="https://files.trdwll.net/2021/12/zYuXtU.jpg" target="_blank" rel="noopener"><img src="https://files.trdwll.net/2021/12/zYuXtU.jpg" width="367" height="488" /></a>&nbsp;<a href="https://files.trdwll.net/2021/12/n3lWWG.jpg" target="_blank" rel="noopener"><img src="https://files.trdwll.net/2021/12/n3lWWG.jpg" width="367" height="488" /></a></p>
<p>I know it's a bit blurry, but it was an impulsive photo.</p>
<p>&nbsp;</p>
<p>until next time</p>
<div class="notranslate" style="all: initial;">&nbsp;</div>
    