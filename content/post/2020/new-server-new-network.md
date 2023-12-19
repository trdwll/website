
+++
title = "New Server and New Network"
description = "I built a new server and bought a new router..."
date = 2020-10-28T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p><strong>UPDATE 12/26/2020: I've changed the drives in the server to be 2x 3TB (raid 1) and 2x 1TB (raid 1).</strong></p>
<p>I recently set up CI (Jenkins) for Shifted and I thought why not have a machine that I can use as a server for various things such as Jenkins? A few years ago I had a full-fledged homelab that contained 6 1U servers (3 Supermicro and 3 Dell). I used only 1-2 of these servers and the rest - well, collected dust. I ran ESXi, pfsense, and a ton of other random things. I got into network security and let's skip a year. I didn't use them that much so I started shutting them down. I moved to more consumer-grade networking gear and again lets fast forward to the present time.</p>
<p>While I don't <strong>need</strong> a server, it'll certainly help when I want to do some things, not on either one of my main machines. I ended up going with 2x E5 2660v2, 512GB ECC ram, Supermicro X9DRL-iF, LSI SAS 9220-8i raid card, and a Cooler Master N400 (already had from a previous project). The drives that I have in it are 2x 500GB SSD (raid 0), 3x 3TB (raid 0), and 2x 1TB (raid 0).</p>
<p>But Russ, why did you go with 512GB of ram? Calm down pal, I did it for the lulz. I mainly plan to run some local services like Jenkins, JIRA, Invoice Ninja, Plex, among some other services.</p>
<p><a href="https://files.trdwll.net/2020/10/22/20201022_004749.jpg" target="_blank" rel="noopener"><img style="height: 384px; width: 512px;" src="https://files.trdwll.net/2020/10/22/20201022_004749_thumb.jpg" /></a></p>
<p>&nbsp;</p>
<p>I also bought a new router and 2 APs. The old router that I had used for 3-4 years was dropping packets like crazy and the wifi would just drop also. I ended up going with the <a href="https://mikrotik.com/" target="_blank" rel="noopener">MikroTik</a>&nbsp; <a href="https://mikrotik.com/product/rb4011igs_rm" target="_blank" rel="noopener">RB4011iGS+RM</a> and 2 of MikroTik's cheaper <a href="https://mikrotik.com/product/RB941-2nD-TC" target="_blank" rel="noopener">hAP lite TC</a>. MikroTik is very cheap, but very reliable. If you're looking into redoing your network then take a look at stuff that MikroTik offers.</p>
<p>&nbsp;</p>
<p>until next time</p>
    