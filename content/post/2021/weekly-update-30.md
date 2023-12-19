
+++
title = "Weekly Update 30 - Happy New Year and Website Optimizations"
description = "I talk about my week."
date = 2021-01-08T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>First post of the year! Happy New Year everyone, I hope the holidays were good for you.</p>
<p>This week I worked more on <a href="https://store.steampowered.com/app/1202410/Midjungard/" target="_blank" rel="noopener">Midjungard</a>. In my <a href="https://www.trdwll.com/blog/weekly-update-29/">weekly update 29</a>, I said I was pretty much finished - that turned out to be false. We ran into some issues when deploying on Linux. It had to do with Apex and from what we understand is you need a gpu for Apex on Linux. They disabled Apex and there's still some issues with running the server. The libraries aren't being linked for some reason. It turns out that it was my fault - I was uploading to /root/, chowning the files to my tmpuser, and then running the server. The binary references to /root/. This doesn't work since my tmpuser isn't root. To fix this I had to upload to /home/tmpuser/ instead. 🤦 I feel so dumb. I also had to make sure my engine install and project weren't on the same partition. <em>(damn windows) </em>✊</p>
<p>I submitted SteamBridge to the Unreal Marketplace so it should be live within a week or two. I, unfortunately, can't link GitHub in the description so I hope people end up finding it.</p>
<p>I even convinced a friend to get the new Call of Duty (Cold War). We played zombies for ~6 hours Sunday/Monday and it was so fun. Treyarch has done it again - made an amazing game. I hope they bring back some zombie maps from Black Ops 1.</p>
<p>During the past ~2 weeks I've updated the site some and it's sped up the site by ~74.2%. I'm planning to get the speed up more over time.</p>
<p>&nbsp;</p>
<p>until next time</p>
    