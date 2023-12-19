
+++
title = "Building an Image Hosting Website"
description = "An in-depth post about my time making and operating an image hosting website."
date = 2020-04-15T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<h2>Introduction</h2>

<p>I developed and operated an image hosting website called <a href="https://trdwll.com/experiments/imglnx/" target="_blank">imglnx.com</a> (image links/lynx) for just over a year (Dec 5, 2016-Mar 3, 2018).&nbsp; The domain changed ownership to a trusted friend on Nov 20, 2018, and I have no idea if that friend will recreate imglnx.</p>

<p>I created imglnx (<a href="https://web.archive.org/web/20180104183842/https://www.imglnx.com/" target="_blank">archive</a>) for a very simple reason, to create an image host that focused on free, fast, secure, and simple image hosting with a focus on privacy. Not only did I operate imglnx, but I also operated my own DNS servers. The entire service was based outside of the USA (excluding the domain - was registered at Namecheap).</p>

<p>The project originally started in Aug 2013, but quickly died and then was revived in 2016. My plan was to run imglnx for as long as I could since I was personally using the site to host my screenshots etc.</p>

<h2>Research</h2>

<p>Building an image hosting website takes a good amount of research, time, and patience. When I started looking into building the site I wanted to make sure it was fast, secure, and private as possible.</p>

<p>The market of image hosts is very saturated and I needed to be unique so I settled on security and privacy over everything. Sure the site was really fast, but the main focus was security and privacy. The original 2016 version was based in the USA and wasn&#39;t focused on security and privacy.</p>

<h2>Legal</h2>

<p>Not only do you have to worry about illegal content, but you have to worry about getting subpoenaed. This was a great worry for me since I did the site under my real name and alias. However, the images stored were in Romania, the DNS was in France and Czechia - the domain was at Namecheap (USA). There was some thought about transferring the domain to a provider like <a href="https://njal.la" target="_blank">njal.la</a>, but I never did transfer it. Even if I did have everything based out of the USA it doesn&#39;t guarantee not being subpoenaed, because <a href="https://en.wikipedia.org/wiki/Foreign_Intelligence_Surveillance_Act" target="_blank">FISA</a> is a thing.</p>

<p>My thought process for imglnx and the legal side, was if I was subpoenaed or I was emailed about a DMCA request, etc then I&#39;d comply as much as I could without identifying my users. imglnx didn&#39;t store any logs, ips, or identifiable information other than what was supplied at registration (email which didn&#39;t have to be legit). On uploads, I even stripped out <a href="https://en.wikipedia.org/wiki/Exif" target="_blank">exif data</a> to help prevent users from being identified.</p>

<h2>Development</h2>

<p>The <a href="https://github.com/trdwll/imglnx-src-1-x-x" target="_blank">initial version</a> from 2016 was written in PHP - just PHP and no frameworks so it was a pain to do things. This version didn&#39;t have login/register or any cool features, you could only upload images.</p>

<p>After running the PHP version for a few months and not adding any cool features I decided to change from <a href="https://php.net" target="_blank">PHP</a> to <a href="https://djangoproject.com" target="_blank">Django (Python)</a>. Django not only allowed me to do cooler shit like have an admin panel out of the box, but it allowed me to rapid prototype. Sure this was the first real project that I made with Django (and it certainly shows), but I pulled it off really well I think. Writing Django has truly changed the way I develop websites and I don&#39;t have to write shitty SQL statements like in PHP. 😉 I choose Django for a number of reasons, but the main one was I had been wanting to use it for a major project.</p>

<p>When I first started the Django project the layout of the project was handle uploading, login/register, and stripping exif data. I then started to focus on albums and other similar features. I also ran a tor version of the site for a short time and I even had my backups routed over tor onto another server for increased privacy.</p>

<p>The design of the website was amazing - yes I&#39;m biased, but I really do think it was great. It was a design that I made from the ground up with bootstrap only.</p>

<p><a href="https://files.trdwll.net/2020/03/26/928uo7.png" target="_blank"><img src="https://files.trdwll.net/2020/03/26/928uo7_thumb.png" style="height:338px; width:600px" /></a></p>

<p>imglnx design for the entirety of the project.</p>

<p><a href="https://files.trdwll.net/2020/03/26/image-20200326161443-1.png" target="_blank"><img src="https://files.trdwll.net/2020/03/26/image-20200326161443-1.png" style="height:143px; width:537px" /></a></p>

<p>The final message displayed on the homepage.</p>

<h2>Conclusion</h2>

<p>Working on this project was amazing and I learned a lot during its development. During the development, I had pushed numerous updated adding new features and fixing bugs. The site changed hosting providers a couple of times and still remained online for over a year.</p>

<p>Building a large-scale website was extremely fun and I&#39;d love to it again. I do wish that I had a friend or two work on it with me as we could&#39;ve added way more features than planned. During the time that the site was live, it garnered 17462 images uploaded by 158 users which is very impressive for a not known website.</p>

<p>If I were to rebuild imglnx today I&#39;d probably stick with Django for the site as Django is amazing. 😃</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>until next time</p>
    