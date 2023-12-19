+++
title = 'Adding a Day/Night Cycle in UE4 in C++'
date = 2020-01-27T00:00:00-00:00
draft = false
type = 'post'
tags = ['Guide', 'Unreal Engine', 'C++']
+++

<p><strong>UPDATE: This method shouldn't be used anymore. Epic released an atmosphere plugin that replaces the skybox that was used in this guide. To get it working with that it just requires some small changes and I'll eventually update the post.</strong></p>
<p>&nbsp;</p>
<p>This code was apart of an old project of mine that never went anywhere so I figured I'd add it to an example project and release for free. Everyone could use a day/night cycle that's networked right?</p>
<p>This code also isn't that good, but it does work just fine. I never got around to cleaning it up so do what you want with it. The original codebase was from <a href="https://github.com/tomlooman/EpicSurvivalGameSeries">EpicSurvivalGameSeries</a>.</p>
<p><strong>This works for dedicated server and listen server. </strong></p>
<ol>
<li>First off make sure that your Skylight and Light Source are both set to movable in your scene.<br /><img style="height: 35px; width: 353px;" src="https://files.trdwll.net/2020/01/27/image-20200127004550-1.png" /></li>
<li>If you don't have a GameMode and a GameState class then go ahead and make those. Remember, they have to match (GameModeBase/GameStateBase and GameMode/GameState).</li>
<li>To avoid the blog post being <strong>VERY</strong> long (since I'd have to embed the code from the files) just download the header and source files <a href="https://files.trdwll.net/2020/01/27/daynightgamestatebase.h" target="_blank" rel="noopener">DayNightGameStateBase.h</a>, <a href="https://files.trdwll.net/2020/01/27/daynightgamestatebase.cpp" target="_blank" rel="noopener">DayNightGameStateBase.cpp</a>, <a href="https://files.trdwll.net/2020/01/27/daynightgamemode.h" target="_blank" rel="noopener">DayNightGameMode.h</a>, <a href="https://files.trdwll.net/2020/01/27/daynightgamemode.cpp" target="_blank" rel="noopener">DayNightGameMode.cpp</a>, <a href="https://files.trdwll.net/2020/01/27/timeofdaymanager.h" target="_blank" rel="noopener">TimeofDayManager.h</a>, and <a href="https://files.trdwll.net/2020/01/27/timeofdaymanager.cpp" target="_blank" rel="noopener">TimeofDayManager.cpp</a>. <em>Or just download the source package <a href="https://files.trdwll.net/2020/01/27/daynightsource.7z" target="_blank" rel="noopener">DayNightSource.7z</a> to avoid downloading all of them separately.</em></li>
<li>Copy over the contents (make sure to edit to be your class names etc) of the above files to your files.</li>
<li>Now go into your editor and make a BP of TimeofDayManager (BP_TimeofDayManager) and drop that into your level.</li>
<li>Open up the BP_TimeofDayManager and on Tick do the following.<br /><img style="height: 272px; width: 696px;" src="https://files.trdwll.net/2020/01/27/image-20200127003622-1.png" /></li>
</ol>
<p>If you're too lazy to do all of this yourself then just download the project (<a href="https://files.trdwll.net/2020/01/27/daynight.7z" target="_blank" rel="noopener">daynight.7z</a>).</p>
<p>&nbsp;</p>
<p>until next time</p>