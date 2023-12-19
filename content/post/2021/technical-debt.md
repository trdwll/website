
+++
title = "Enter Technical Debt"
description = "I briefly talk about the technical debt of video games."
date = 2021-04-13T13:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>I'll be talking about technical debt in general, what to look out for before you fall into tech debt, and my experience with it.</p>
<p>&nbsp;</p>
<h3>What is technical debt?</h3>
<p>So tech debt's definition on Google is "Technical debt is a concept in software development that reflects the implied cost of additional rework caused by choosing an easy solution now instead of using a better approach that would take longer." That sums it up lol.</p>
<p>&nbsp;</p>
<h3>What am I looking for?</h3>
<p>Here's a list of some things to look out for.</p>
<ul>
<li>A new team member to the team wants to rebuild a system from the ground up</li>
<li>A team member wants to optimize something without profiling data</li>
<li>A system is a nightmare to maintain</li>
<li>A ton of other things like projects lack of time, a team members incompetence, etc</li>
</ul>
<p>&nbsp;</p>
<h3>My experience</h3>
<p>I can't go into great detail, but I can say that when I joined a team I ended up rewriting a major system that had been implemented 3 times previously and each implementation was causing more and more issues. I caused more tech debt here, but I also eliminated future tech debt due to a better implementation. The funny thing is that this system was implemented via UE4 classes, a Marketplace asset, a new team member, and then finally me using UE4 classes and I was a new team member. lol</p>
<p>That project also suffered from pre-optimizations without profiling data.</p>
<p>After that experience, I've learned to profile, profile, and profile before refactoring or optimizing.</p>
<p>&nbsp;</p>
<p>until next time</p>
    