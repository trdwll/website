
+++
title = "How to Setup Your Own VPN"
description = "A guide on setting up your own VPN."
date = 2020-04-08T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>With security and privacy being a major thing nowadays I figured I&#39;d write up a short guide on how to set up your own VPN.</p>

<p>For this guide I used <a href="https://www.vultr.com/" target="_blank">Vultr</a> <a href="https://www.vultr.com/?ref=7156431" target="_blank">(affiliate link)</a> since I had some credit left with them and only needed a VPS for an hour max. The main thing with this is you&#39;re going to want at least a 1Gbps connection on your VPS, 1GB ram, and no less than 1 core. The VPS cost me $0.02 for the hour that I had it online.</p>

<p>This script that I&#39;m using in this guide currently only supports Debian, Ubuntu and CentOS. I choose to use CentOS 7 for this guide.</p>

<p><a href="https://github.com/Nyr/openvpn-install">https://github.com/Nyr/openvpn-install</a></p>

<p><a href="https://files.trdwll.net/2020/04/03/image-20200403173902-4.png" target="_blank"><img src="https://files.trdwll.net/2020/04/03/image-20200403173902-4.png" style="height:323px; width:919px" /></a></p>

<p><code>wget https://raw.githubusercontent.com/Nyr/openvpn-install/master/openvpn-install.sh</code></p>

<p><a href="https://files.trdwll.net/2020/04/03/image-20200403173804-3.png" target="_blank"><img src="https://files.trdwll.net/2020/04/03/image-20200403173804-3.png" style="height:267px; width:919px" /></a></p>

<p><code>chmod +x openvpn-install.sh</code></p>

<p><a href="https://files.trdwll.net/2020/04/03/image-20200403174738-5.png" target="_blank"><img src="https://files.trdwll.net/2020/04/03/image-20200403174738-5.png" style="height:657px; width:919px" /></a></p>

<p><code>./openvpn-install.sh</code></p>

<ol>
	<li>Download the .ovpn file that was generated.</li>
	<li>Head over to OpenVPN&#39;s website and <a href="https://openvpn.net/community-downloads/" target="_blank">download</a> the client. (You can use other clients, but they need to support OpenVPN - I also don&#39;t talk about those other clients in this guide.)</li>
	<li>Install the client on your machine.</li>
	<li>Copy the .ovpn file that you downloaded into your OpenVPN client folder (config). Mine is located at <strong>D:\Program Files\OpenVPN\config</strong>.<br />
	<a href="https://files.trdwll.net/2020/04/03/image-20200403175216-6.png" target="_blank"><img src="https://files.trdwll.net/2020/04/03/image-20200403175216-6.png" style="height:123px; width:583px" /></a></li>
	<li>Open the OpenVPN client (run as admin if you can&#39;t connect later). Look for the&nbsp; <img src="https://files.trdwll.net/2020/04/03/image-20200403175417-7.png" style="height:37px; width:25px" />&nbsp; icon in your task tray. (bottom right of your Windows explorer)</li>
	<li>Right click the icon and press connect.<br />
	<a href="https://files.trdwll.net/2020/04/03/image-20200403175512-8.png" target="_blank"><img src="https://files.trdwll.net/2020/04/03/image-20200403175512-8.png" style="height:234px; width:203px" /></a></li>
	<li>Bam, if everything was successful then you&#39;re successfully connected to a VPN.<br />
	<a href="https://files.trdwll.net/2020/04/03/image-20200403175656-9.png" target="_blank"><img src="https://files.trdwll.net/2020/04/03/image-20200403175656-9_thumb.png" style="height:373px; width:572px" /></a><br />
	<a href="https://files.trdwll.net/2020/04/03/image-20200403175757-10.png" target="_blank"><img src="https://files.trdwll.net/2020/04/03/image-20200403175757-10_thumb.png" style="height:216px; width:357px" /></a></li>
</ol>

<p>&nbsp;</p>

<p>Using a VPN is the first step you can do for privacy online. However, it&#39;s not a silver bullet. You still should look into dns leaks or webrtc leaks and other security things. I&#39;ll eventually write more on privacy and security so stay tuned for that.</p>

<p>&nbsp;</p>

<p>until next time</p>

<p>&nbsp;</p>
    