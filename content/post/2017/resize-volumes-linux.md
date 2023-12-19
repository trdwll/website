+++
title = 'Resize Volumes in Linux'
date = 2017-01-11T00:00:00-00:00
draft = false
type = 'post'
tags = ['Guide']
+++

<p>I&rsquo;m going to start writing up small howtos so I don&rsquo;t have to search for something 1 million times.</p>
<p>This howto is about resizing volumes in Linux.</p>
<p>You&rsquo;re going to want to log out of all users except root and stop the services that show up from <strong>fuser -m /home</strong>. Now that you&rsquo;re done that you can proceed to unmout /home by issuing <strong>umount /home </strong>in terminal. Run <strong>fsck -f /dev/mapper/(whatever)_home</strong> to verify the volume is ok. You can now begin to resize /home&nbsp;volume by running <strong>lvresize -r -L(whatever)G /dev/mapper/(whatever)_home</strong> in terminal. So you&rsquo;ve resized the /home volume and you have some free space. Proceed to resize whatever volume (for example root /) as follows <strong>lvresize -r -L+(whatever)G /dev/mapper/(whatever)_root</strong>. That&rsquo;s all, just run <strong>mount /home</strong> in terminal and you&rsquo;re all good.</p>
<p>&nbsp;</p>
<p>until next time</p>