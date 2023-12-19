+++
slug = 'homelab'
title = 'Homelab'
date = 2016-12-19T00:00:00-00:00
draft = false
type = 'post'
tags = ['SysAdmin']
+++

<p>So where do I start on this topic? I guess I'll start with why I'm going to talk about it. I was asked a few days ago (more like weeks, but whatever) why I have servers and such a "complicated" setup. First, before I do end up spilling the beans on my setup I'll give a small background on myself.</p>
<p>tl;dr</p>
<p>I hate networking and everything about it. (although, I'm starting to enjoy it somewhat)</p>
<p>Now that's out of the way, time to talk about my home lab.</p>
<p>So now to spill the beans. I offset compile times etc by using some Xeon power among other things as I list them below. I often use the servers for research/experiments and just plain things like a Teamspeak 3 server.</p>
<h3>Server Specs</h3>
<p>I currently have 3 Supermicro 1U servers with the specs of:</p>
<ul>
<li>Motherboard: <a href="http://www.supermicro.com/products/motherboard/QPI/5500/X8DTU-F.cfm" target="_blank" rel="noopener">X8DTU-F</a></li>
<li>CPU: 2x <a href="http://ark.intel.com/products/37109/Intel-Xeon-Processor-X5560-8M-Cache-2_80-GHz-6_40-GTs-Intel-QPI" target="_blank" rel="noopener">Intel Xeon x5560</a></li>
<li>Memory: 1 server has 96GB ECC the other 2 have 48GB ECC</li>
<li>Storage: 1 server has 3x <a href="http://www.ebay.com/itm/161690640516" target="_blank" rel="noopener">3TB</a> and 1x 250GB the other 2 have 2x 250GB and 1x 1TB</li>
<li>PSU: 560w</li>
<li>96GB is DEV1</li>
<li>48GB is PROD1 and DEV2</li>
<li>All run <a href="http://www.vmware.com/products/esxi-and-esx.html" target="_blank" rel="noopener">ESXi</a></li>
</ul>
<p>I also have a <a href="http://www.dell.com/us/business/p/networking-2800-series/pd" target="_blank" rel="noopener">Dell PowerConnect 2816</a> switch, 2x firewalls, and a wireless router. I have some other things in my network to provide more security which I don't tell anyone. (the fewer people know the better)</p>
<p>I use the 96GB server for Windows 10 (dev), various Linux distros (dev), GitLab, NextCloud, and Plex. I keep one of the 48GB servers offline as I don't need it and the other is used for pfSense, Minecraft server, Pi-Hole, and Teamspeak 3.</p>
<h3>Network map</h3>
<p>My network looks somewhat like this: (I'm not going to show you the security of my network as I said above)</p>
<p><img class="alignnone size-full wp-image-71" src="https://files.trdwll.net/2016/12/netmap.png" alt="netmap" width="663" height="393" /></p>
<p>&nbsp;</p>
<p>Since this post is about finished, I'll go ahead and say I'm going to be picking up an HP ProLiant DL360 G7 with 128GB ECC to replace my DEV1 server. When I get around to doing that I'll be colocating the old DEV1 server to a dc to be an offsite backup, GitLab, Plex, and a machine I can give friends a VPS' on to host whatever.</p>
<p>until next time</p>