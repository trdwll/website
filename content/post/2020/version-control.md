
+++
title = "Version Control"
description = "The most important thing when working on a project."
date = 2020-02-25T11:25:06Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>I hear stories about people not using a Version Control System (&quot;VCS&quot;) and how they are having an issue with new code, lost all of their work, or just don&#39;t use one at all. I remember back in 2014 (I believe) I joined a team that was working on an FPS game. I quickly found out that they were using Google Drive as a VCS. lol wut? This happened again last year in 2019 when I joined a team that was working on a survival game - they were also using Google Drive. The team behind the survival game switched to Git after I had joined, but even Git isn&#39;t the best for a UE4 project.</p>

<p>&nbsp;</p>

<h3>What is Version Control?</h3>

<p>A version control system (VCS or SCM) is a software that permits multiple users to work on files together. Not only does a VCS maintain a history of each file that&#39;s added so that it can be reverted if necessary, but it even allows users to edit the same file simultaneously without overwriting other users work. (unless a newer commit overwrites a previous commit)</p>

<p>&nbsp;</p>

<p>There are a lot of VCS, but we&#39;re only going to talk about the popular ones.</p>

<ul>
	<li><a href="https://git-scm.com/" target="_blank">Git</a> is 100% free with the exception of self-hosting (if you rent a server that is)</li>
	<li><a href="https://www.perforce.com/" target="_blank">Perforce</a> is free for 5 users and then it costs - it&#39;s expensive after those 5 users</li>
	<li><a href="https://www.plasticscm.com/" target="_blank">PlasticSCM</a> has free and paid plans</li>
</ul>

<p>Git is a great VCS, but for only source files. A thing called Git LFS exists, but I wouldn&#39;t recommend it with a UE4 project.</p>

<p>Perforce is the industry standard for gamedev and is implemented very well with UE4.</p>

<p>PlasticSCM... I never heard about it until I read about <a href="https://twitter.com/garrynewman">Garry Newman</a> using it on his <a href="https://garry.tv">blog</a>. I started using it recently for a VR project that I got hired to work on and I can say that it&#39;s certainly not bad. I think it&#39;s on par with Perforce - it&#39;s also cheaper. I did ask in a discord full of PlasticSCM users and they all said they choose it due to the UI being nice or it being simple to use. Check out the plasticscm <a href="https://www.plasticscm.com/alternative-to-perforce" target="_blank">comparison</a> to other VCS.</p>

<p>&nbsp;</p>

<p>When it comes down to it, use whatever works for you and your team, just make sure you&#39;re using a VCS.</p>

<p>&nbsp;</p>

<p>until next time</p>
    