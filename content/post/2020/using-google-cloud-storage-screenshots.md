
+++
title = "Using Google Cloud Storage for Screenshots"
description = "A guide on using GCP for hosting your screenshots."
date = 2020-09-22T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>For a while, I used <a href="https://vgy.me/" target="_blank" rel="noopener">vgy.me</a> for hosting my screenshots, and while I didn't have any issues with it until recently. It never really occurred to me that I should host my <a href="https://trdwll.com/blog/building-image-hosting-website/">own</a>. A few days ago I started having 404 and 500 errors with vgy.me so I said that's enough and I began research on the top cloud providers (Google, AWS, and Azure). I settled on Google Cloud Platform hence this post.</p>
<p>You don't have to use this just for screenshots, but any type of files. After all, it is a storage platform, but we're just using it for screenshots in this post.</p>
<p>&nbsp;</p>
<h3>Setting up Your Storage Bucket</h3>
<p>With GCP you pay for what you use. 1GB storage is $0.026 per GB-month etc. Read more on the pricing <a href="https://cloud.google.com/storage/pricing" target="_blank" rel="noopener">here</a>.</p>
<div class="mat-form-field-hint-spacer">&nbsp;</div>
<p>So now we begin.</p>
<ol>
<li>Head over to the <a href="https://console.cloud.google.com/storage/" target="_blank" rel="noopener">Google Console</a>.</li>
<li>Choose "Select a project"<br /><a href="https://files.trdwll.net/2020/09/14/image_RJV5CmB.png" target="_blank" rel="noopener"><img style="height: 42px; width: 350px;" src="https://files.trdwll.net/2020/09/14/image_RJV5CmB_thumb.png" /></a></li>
<li>Choose "New Project"<br /><a href="https://files.trdwll.net/2020/09/14/image_nXgjtFH.png" target="_blank" rel="noopener"><img style="height: 278px; width: 350px;" src="https://files.trdwll.net/2020/09/14/image_nXgjtFH_thumb.png" /></a></li>
<li>Name your project if you want to and press create. (if you have an organization then feel free to choose it also.<br /><a href="https://files.trdwll.net/2020/09/14/image_Z9k8ZRj.png" target="_blank" rel="noopener"><img style="height: 284px; width: 350px;" src="https://files.trdwll.net/2020/09/14/image_Z9k8ZRj_thumb.png" /></a><br /><a href="https://files.trdwll.net/2020/09/14/image_DYY4qmd.png" target="_blank" rel="noopener"><img style="height: 58px; width: 350px;" src="https://files.trdwll.net/2020/09/14/image_DYY4qmd_thumb.png" /></a></li>
<li>Scroll down on the left of the screen and look for "Storage"<br /><a href="https://files.trdwll.net/2020/09/14/image_h0ByCCO.png" target="_blank" rel="noopener"><img style="height: 303px; width: 274px;" src="https://files.trdwll.net/2020/09/14/image_h0ByCCO_thumb.png" /></a></li>
<li>Before being able to create a bucket you may need to add a billing method. I'm not going to do that in this guide as I've already done it and it literally tells you to add one if you need to so just go do that.&nbsp;<br /><a href="https://files.trdwll.net/2020/09/14/image_pqIZLG0.png" target="_blank" rel="noopener"><img style="height: 94px; width: 864px;" src="https://files.trdwll.net/2020/09/14/image_pqIZLG0.png" /></a></li>
<li>Once you have your billing setup then you can press "Create Bucket".<br /><a href="https://files.trdwll.net/2020/09/14/image_gBvHGYK.png" target="_blank" rel="noopener"><img style="height: 45px; width: 553px;" src="https://files.trdwll.net/2020/09/14/image_gBvHGYK.png" /></a></li>
<li>Name your new bucket. (this can be anything, but if you want to use your own domain then put that domain here)<br /><a href="https://files.trdwll.net/2020/09/14/image_W9gCRi0.png" target="_blank" rel="noopener"><img style="height: 219px; width: 350px;" src="https://files.trdwll.net/2020/09/14/image_W9gCRi0_thumb.png" /></a></li>
<li>Set your location and storage class.<br /><a href="https://files.trdwll.net/2020/09/14/image_hr1oB84.png" target="_blank" rel="noopener"><img style="height: 350px; width: 239px;" src="https://files.trdwll.net/2020/09/14/image_hr1oB84_thumb.png" /></a></li>
<li>Set other settings.<br /><a href="https://files.trdwll.net/2020/09/14/image_Ws0tQ19.png" target="_blank" rel="noopener"><img style="height: 350px; width: 223px;" src="https://files.trdwll.net/2020/09/14/image_Ws0tQ19_thumb.png" /></a></li>
<li>Excellent! Now press the big Create button at the bottom.</li>
</ol>
<p>&nbsp;</p>
<h3>Setting up ShareX to Upload to GCP</h3>
<ol>
<li>Open ShareX and set your destinations to Google Cloud Storage.<br /><img style="height: 133px; width: 350px;" src="https://files.trdwll.net/2020/09/14/image_f07iktl_thumb.png" /></li>
<li>Then go to Destination settings and scroll to find Google Cloud Storage.<br /><a href="https://files.trdwll.net/2020/09/14/image_QscJigz.png" target="_blank" rel="noopener"><img style="height: 257px; width: 350px;" src="https://files.trdwll.net/2020/09/14/image_QscJigz_thumb.png" /></a></li>
<li>Press Connect and sign in with the email that you created the bucket under. It'll give you a token which then you'll paste it into ShareX under "verify code" then press Complete authorization.</li>
<li>Set your bucket name to the bucket name from the bucket above. Set your custom domain if you have that setup also. (you'll have to add a CNAME record (for this guide it's files and then c.storage.googleapis.com as the value))</li>
<li>Done!</li>
</ol>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>until next time</p>
<p>&nbsp;</p>
    