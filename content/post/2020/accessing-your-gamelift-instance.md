
+++
title = "Accessing Your GameLift Instance"
description = "A short guide on accessing your GameLift instance via RDP or ssh."
date = 2020-02-20T13:45:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>&nbsp;</p>
<h3>Prerequisites</h3>
<ul>
<li><a href="https://aws.amazon.com/cli/" target="_blank" rel="noopener">AWS CLI</a></li>
<li>A GameLift fleet already created</li>
<li>Patience</li>
</ul>
<p>&nbsp;</p>
<p><strong>This guide is assuming you're on Windows as your main OS, but if you're using Linux then the commands will be the same for AWS, but the system commands like changing the ssh key permission for Linux would be</strong> <code>chmod 400 gameliftkey.pem</code>.</p>
<p>&nbsp;</p>
<h3>Windows</h3>
<ol>
<li>Open Command Prompt (cmd) and type in <code>aws gamelift describe-instances --fleet-id &lt;your-fleet-id&gt;</code>. Replace &lt;your-fleet-id&gt; with your actual fleet id which you can find <a href="https://console.aws.amazon.com/gamelift/home" target="_blank" rel="noopener">here</a>.<br /><a href="https://files.trdwll.net/2020/02/18/image-20200218035442-1.png" target="_blank" rel="noopener"><img style="height: 251px; width: 785px;" src="https://files.trdwll.net/2020/02/18/image-20200218035442-1.png" /></a></li>
<li>Now in cmd run&nbsp;<code>aws gamelift get-instance-access --fleet-id &lt;your-fleet-id&gt; --instance-id &lt;your-instance-id&gt;</code>. Again replace the contents in &lt;test&gt; with the details from the command above. <a href="https://files.trdwll.net/2020/02/18/image-20200218035856-2.png" target="_blank" rel="noopener"><img style="height: 229px; width: 961px;" src="https://files.trdwll.net/2020/02/18/image-20200218035856-2.png" /></a></li>
<li>Excellent, now you can log into your instance. Open Remote Desktop Connection (RDP) on Windows (Windows key and type in RDP). Log in with the details from the command above.<br /><a href="https://files.trdwll.net/2020/02/18/image-20200218040112-3.png" target="_blank" rel="noopener"><img style="height: 253px; width: 407px;" src="https://files.trdwll.net/2020/02/18/image-20200218040112-3.png" /></a><br /><a href="https://files.trdwll.net/2020/02/18/image-20200218040141-4.png" target="_blank" rel="noopener"><img style="height: 368px; width: 456px;" src="https://files.trdwll.net/2020/02/18/image-20200218040141-4.png" /></a><br /><a href="https://files.trdwll.net/2020/02/18/image-20200218040230-5.png" target="_blank" rel="noopener"><img style="height: 448px; width: 800px;" src="https://files.trdwll.net/2020/02/18/image-20200218040230-5_thumb.png" /></a></li>
<li>To access your game go to <strong>C:\Game</strong>.</li>
</ol>
<p>&nbsp;</p>
<h3>Linux</h3>
<ol>
<li>Open Command Prompt (cmd) and type in <code>aws gamelift describe-instances --fleet-id &lt;your-fleet-id&gt;</code>. Replace &lt;your-fleet-id&gt; with your actual fleet id which you can find <a href="https://console.aws.amazon.com/gamelift/home" target="_blank" rel="noopener">here</a>.<br /><a href="https://files.trdwll.net/2020/02/19/image-20200219122201-2.png" target="_blank" rel="noopener"><img style="height: 252px; width: 782px;" src="https://files.trdwll.net/2020/02/19/image-20200219122201-2.png" /></a></li>
<li>Now in cmd run&nbsp;<code>aws gamelift get-instance-access --fleet-id &lt;your-fleet-id&gt; --instance-id &lt;your-instance-id&gt; --query InstanceAccess.Credentials.Secret --output text &gt; gameliftkey.pem</code>. Again replace the contents in &lt;test&gt; with the details from the command above. This will generate an ssh key for you.<br /><a href="https://files.trdwll.net/2020/02/19/image-20200219123712-5.png" target="_blank" rel="noopener"><img style="height: 45px; width: 960px;" src="https://files.trdwll.net/2020/02/19/image-20200219123712-5.png" /></a></li>
<li>Right click the gameliftkey.pem and make it readonly. (<strong>Right click -&gt; Properties -&gt; Read-only</strong>) (you might not have to do this, but do it if it complains about file permissions)<br /><img style="height: 35px; width: 151px;" src="https://files.trdwll.net/2020/02/19/image-20200219124221-6.png" /></li>
<li>Great! In cmd run <code>ssh -i gameliftkey.pem gl-user-remote@&lt;your server ip&gt;</code>. Remember to replace the &lt;your server ip&gt; with the one from step 1. If this is your first time accessing the instance it will ask you something about a fingerprint - just type yes.</li>
<li>Awesome now you should be logged in.<br /><a href="https://files.trdwll.net/2020/02/19/image-20200219125215-7.png" target="_blank" rel="noopener"><img style="height: 204px; width: 681px;" src="https://files.trdwll.net/2020/02/19/image-20200219125215-7.png" /></a></li>
<li>To access your game go to <strong>/local/game</strong>.</li>
</ol>
<p>&nbsp;</p>
<p>until next time</p>
    