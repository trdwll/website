
+++
title = "How I Version Products in Unreal Engine"
description = "Yep..."
date = 2021-06-16T13:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>While waiting for <a href="https://github.com/EpicGames/UnrealEngine/pull/6619" target="_blank" rel="noopener">this</a> to be added to Unreal I came up with an <a href="https://gist.github.com/trdwll/c65fa5797f687ec9b47fa21212c0e09a" target="_blank" rel="noopener">alternative</a>. This python script will update the version in your <code>DefaultGame.ini</code>.</p>
<pre class="language-python"><code>import configparser
import sys
import argparse

def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('Workspace', help='The path to the project that you\'re wanting to use!')
  parser.add_argument('NewVersion', help='The new version to set for the project.')
  args = parser.parse_args()

  config_file = args.Workspace + '/Config/DefaultGame.ini'

  config = configparser.ConfigParser()
  config.optionxform=str
  config.read(config_file)
  config['/Script/EngineSettings.GeneralProjectSettings']['ProjectVersion'] = args.NewVersion

  with open(config_file, 'w') as configfile:
      config.write(configfile)

if __name__ == "__main__":
  main(sys.argv[1:])</code></pre>
<p>&nbsp;</p>
<p>It's not ideal as something like this should be added to UBT, but it doesn't exist (unless that PR gets merged) so this will work for now.</p>
<p>All you have to do is <code>py C:\UEVersion.py %WORKSPACE% 1.0.0.%PLASTICSCM_CHANGESET_ID%.%BUILD_NUMBER%</code> or something similar. This is from my <a href="https://trdwll.com/blog/jenkins-and-ue4/" target="_blank" rel="noopener">Jenkins</a> project so I can automate changing the version numbers.</p>
<p>&nbsp;</p>
<p>until next time</p>
    