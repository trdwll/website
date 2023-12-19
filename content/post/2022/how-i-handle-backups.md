
+++
title = "How I Handle Backups"
description = "A foolproof plan."
date = 2022-01-02T11:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>The normal rule is 3-2-1 - 3 backups, 2 onsite, 1 offsite. However I do 2 offsite only. I may do a third offsite, but not sure just yet.</p>
<p>I use <a href="https://www.scaleway.com/en/c14-cold-storage/" target="_blank" rel="noopener">Scaleway's C14 Cold Storage</a>. I used OVH Archive, but the upload speeds were super slow.</p>
<p>&nbsp;</p>
<p>In proxmox I edited the <code>/etc/vzdump.conf</code> and added <code>script: /path/to/my/perl/script.pl</code> at the bottom. When I run vzdump from the ui or proxmox kicks off a backup cron the script will get ran.</p>
<p>Originally I was using a simple python script to backup vms to the cloud, but since I changed to this perl script.</p>
<pre class="language-perl"><code>#!/usr/bin/perl -w

# from https://gitlab.com/mikeramsey/proxmox-vzdump-hook-script.pl/-/blob/master/vzdump-hook-script.pl
# example hook script for vzdump (--script option)

use strict;

print "HOOK: " . join (' ', @ARGV) . "\n";

my $phase = shift;

my $GPGKey = "REDACTED";

if ($phase eq 'job-start' || 
	$phase eq 'job-end'  || 
	$phase eq 'job-abort') { 

	my $dumpdir = $ENV{DUMPDIR};

	my $storeid = $ENV{STOREID};

	print "HOOK-ENV: dumpdir=$dumpdir;storeid=$storeid\n";
} elsif ($phase eq 'backup-start' || 
	 $phase eq 'backup-end' ||
	 $phase eq 'backup-abort' || 
	 $phase eq 'log-end' || 
	 $phase eq 'pre-stop' ||
	 $phase eq 'pre-restart' ||
	 $phase eq 'post-restart') {

	my $mode = shift; # stop/suspend/snapshot
	my $vmid = shift;
	my $vmtype = $ENV{VMTYPE}; # lxc/qemu
	my $dumpdir = $ENV{DUMPDIR};
	my $storeid = $ENV{STOREID};
	my $hostname = $ENV{HOSTNAME};
	my $target = $ENV{TARGET};
	my $logfile = $ENV{LOGFILE}; 

	print "HOOK-ENV: vmtype=$vmtype;dumpdir=$dumpdir;storeid=$storeid;hostname=$hostname;target=$target;logfile=$logfile\n";

    if ($phase eq 'backup-end') {
		
        # encrypt the backup using gpg
        print "encrypting $target";
        system ("gpg -r $GPGKey -e $target") == 0 ||
		    die "encrypting $target failed";

        # upload to c14 cold
        print "Uploading ${target}.gpg to c14-cold-fr";
        system ("rclone copy --config /root/.config/rclone/rclone.conf -P ${target}.gpg c14-cold-fr:/REDACTED/MYDIR") == 0 ||
		    die "uploading $target to c14-cold-fr failed";

         # upload to c14 cold
        print "Uploading ${target}.gpg to c14-cold-nl";
        system ("rclone copy --config /root/.config/rclone/rclone.conf -P ${target}.gpg c14-cold-nl:/REDACTED --transfers 16 --buffer-size 512") == 0 ||
		    die "uploading $target to c14-cold-nl failed";

        print "Deleting ${target}.gpg";
        system ("rm ${target}.gpg") == 0 || 
            die "deleting ${target}.gpg failed";

        # print "Deleting $target and ${target}.gpg";
        # system ("rm $target ${target}.gpg") == 0 || 
        #     die "deleting $target ${target}.gpg failed";
	}
	
} else {
	die "got unknown phase '$phase'";
}

exit (0);
</code></pre>
<p>&nbsp;</p>
<p>Here's the rclone config that I use.</p>
<pre class="language-no-highlighting"><code>[c14-cold-fr]
type = s3
provider = Other
env_auth = false
access_key_id = REDACTED
secret_access_key = REDACTED
region = fr-par
endpoint = https://s3.fr-par.scw.cloud
location_constraint = fr-par
acl = private
bucket_acl = private
chunk_size = 25M
upload_concurrency = 100
storage_class = GLACIER

[c14-cold-nl]
type = s3
provider = Other
env_auth = false
access_key_id = REDACTED
secret_access_key = REDACTED
region = nl-ams
endpoint = https://s3.nl-ams.scw.cloud
location_constraint = nl-ams
acl = private
bucket_acl = private
chunk_size = 25M
upload_concurrency = 100
storage_class = GLACIER</code></pre>
<p>&nbsp;</p>
<p>Instead of letting rclone handle the encryption (tbh I'm not familiar with it) I just run a gpg command to encrypt the backup.</p>
<p>&nbsp;</p>
<p>until next time</p>
    