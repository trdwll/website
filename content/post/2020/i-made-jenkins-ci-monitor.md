
+++
title = "I made a Jenkins CI monitor"
description = 'Using a RPi 3B and a 5" screen I made a Jenkins CI monitor.'
date = 2020-10-29T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>Now that we have Jenkins running for Shifted I wanted to have the stats displayed easily. I set up a <a href="https://grafana.com/get" target="_blank">grafana</a> dashboard in a vm on my <a href="https://trdwll.com/blog/new-server-new-network/">server</a> and hooked up Jenkins to it.</p>



<p>I got this idea from the Sea of Thieves talk (Automated Testing at Scale in Sea of Thieves) by <a href="https://jessicabaker.co.uk/" target="_blank">Jessica Baker</a>. (specifically the <a href="https://youtu.be/KmaGxprTUfI?t=1504" target="_blank">timestamp</a> (1504)).</p>



<p><iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube-nocookie.com/embed/KmaGxprTUfI" width="560"></iframe></p>



<p>&nbsp;</p>



<p>This probably isn&#39;t the most ideal way to do this, but it works.&nbsp; For this build, I just used one of my old Raspberry Pi&#39;s (the 3B) and I picked up a 5&quot; screen from <a href="https://www.amazon.com/gp/product/B08343QX67/" target="_blank">ELECROW</a>. I installed Raspbian, connected to Wifi, and then opened the grafana dashboard via Chromium. (then full-screened and used Kiosk mode in grafana)</p>



<p>Honestly, I wish I would&#39;ve gone with the 7&quot; screen so I could display more information.</p>



<p>The photo is a bit blurry because I zoomed in on the rpi so I wouldn&#39;t be in the reflection</p>



<p><a href="https://files.trdwll.net/2020/10/24/20201024_150526_2GjJUZ8.png" target="_blank"><img src="https://files.trdwll.net/2020/10/24/20201024_150526_2GjJUZ8.png" style="height:800px; width:600px" /></a></p>



<p>&nbsp;</p>



<p>until next time</p>
    