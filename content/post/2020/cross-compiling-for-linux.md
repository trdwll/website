+++
title = 'Cross-Compiling for Linux on Windows for UE4'
date = 2020-01-15T00:00:00-00:00
draft = false
type = 'post'
tags = ['Guide', 'Unreal Engine']
+++

<p>There's really not much information on this so I figured I'd write about it to help other people and help myself if I forget how. lol</p>
<p><strong>This guide is written for 4.24, but should work for other versions. Or at the very least will be very similar for other versions.</strong></p>
<ol>
<li>Download and install the <a href="https://docs.unrealengine.com/en-US/Platforms/Linux/GettingStarted/index.html">clang toolchain</a>.<br /><img style="height: 290px; width: 422px;" src="https://files.trdwll.net/2020/01/20/yf4mvb.png" alt="" /></li>
<li>Add the settings to your <strong>DefaultEngine.ini</strong>.
<pre><code>[/Script/LinuxTargetPlatform.LinuxTargetSettings]
TargetArchitecture=X86_64UnknownLinuxGnu</code></pre>
There are 3 options for this. X86_64UnknownLinuxGnu, ArmUnknownLinuxGnueabihf, or AArch64UnknownLinuxGnueabi</li>
<li>Go into the launcher and download the Linux platform. (if you have source build then ignore this step)<br /><img style="height: 161px; width: 252px;" src="https://files.trdwll.net/2020/01/20/oii7jo.png" alt="" /><br />Click the down arrow on the right then make sure Linux is selected.<br /><img style="height: 48px; width: 599px;" src="https://files.trdwll.net/2020/01/20/5rabcv.png" alt="" /></li>
<li>Package your project however you do whether it be via Editor (<strong>File -&gt; Package Project</strong>) or <a href="https://trdwll.com/blog/using-unreal-frontend-package-your-project/">Unreal Frontend</a>.</li>
</ol>
<p>&nbsp;</p>
<p>until next time</p>