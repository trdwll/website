
+++
title = "Weekly Update 22 - GameMode Redesign for VAIL, Jenkins CI, and Website Redesign"
description = "I talk about my week."
date = 2020-11-06T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>So it's been a long time since I wrote a weekly update. I apologize for that, but I've had some shit going on ok.</p>
<p>So what have I been busy with? Fuck dude chill out for a second. Let's take a quick breath and relax.</p>
<p>&nbsp;</p>
<p>For the past couple of weeks, I've been hard at work on Shifted. You know the game that I talk about every single time I write one of these? Cool so starting last week I completely ripped out, redesigned, and rewrote the entire GameMode system. The system we had before well... we'll just say it wasn't ideal. Anyway so now that this major task is out of the way we're able to manage the codebase and implement new gamemodes more easily. Another big thing for this is it's all entirely in C++. Sure we lose the prototyping of gamemodes in BP, but at the end of the day, we can always create a gamemode in BP to prototype with.</p>
<p>I'd say you can already tell that I even redesigned this website. It now uses <a href="https://tailwindcss.com" target="_blank" rel="noopener">Tailwindcss</a> instead of <a href="https://getbootstrap.com" target="_blank" rel="noopener">Bootstrap</a>. Eventually I'm going to strip out some of the css that the site doesn't use to help improve loading times, but I think it's fine for now. I even removed a ton of additional queries when visiting the homepage. I'm very happy with the way the site turned out. I push updates here and there to fix and add things that I come up with so keep an eye out for those changes. 😉</p>
<p>Last Sunday I worked on this site some and removed ckeditor (the WYSIWYG editor for doing posts like this) and replaced it with <a href="https://www.tiny.cloud/features" target="_blank" rel="noopener">TinyMCE</a>. I can say that I wish I would've done it sooner. Ckeditor is good, but I ran into too many issues with it. (the editor would go readonly sometimes or my plugins would be broken after an update)</p>
<p>I also set up Jenkins and a CI pipeline for Shifted. Which I've already written about at this point so no clue why I'm writing it here... I even started working on <a href="https://www.trdwll.com/experiments/steambridge/" target="_blank" rel="noopener">SteamBridge</a> again, but this time it's a clean slate.</p>
<p>&nbsp;</p>
<p>Anyway I know I say this quite often, but I do plan to start writing weekly. I've just been very busy so I haven't had the time.</p>
<p>&nbsp;</p>
<p>until next time</p>
    