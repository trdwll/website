
+++
title = "Jenkins and UE4"
description = "Yep. I show you how to use CI and UE4"
date = 2020-11-04T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p><strong>NOTE: This guide assumes you already have a machine with Jenkins on it.</strong></p>
<p>&nbsp;</p>
<h2>Prerequisites</h2>
<ul>
<li>Windows machine (or you can use a Windows agent)</li>
<li>UE4 and Jenkins installed</li>
<li>Patience</li>
</ul>
<p>&nbsp;</p>
<ol>
<li>Create a new job as a freestyle project.<br /><img src="https://files.trdwll.net/2020/11/01/screenshot_2020-11-01_182951.png" alt="" width="457" height="253" /></li>
<li>Choose "This project is parameterized."<br /><img src="https://files.trdwll.net/2020/11/01/bpcaag.png" alt="" width="265" height="81" /></li>
<li>Add 1 choice parameter and 2 string parameters.</li>
<li>Fill in the content as follows.<br />
<pre class="language-markdown"><code>==== Choice Parameter ====
== Name ==
BUILD_CONFIGURATION
== Choices ==
Development
Shipping
Test
DebugGame
== Description ==
Development = This configuration is equivalent to Release. Unreal Editor uses the Development configuration by default. Compiling your project using the Development configuration enables you to see code changes made to your project reflected in the editor.
Shipping =  This is the configuration for optimal performance and shipping your game. This configuration strips out console commands, stats, and profiling tools.
Test =  This configuration is the Shipping configuration, but with some console commands, stats, and profiling tools enabled.
DebugGame = This configuration builds the engine as optimized, but leaves the game code debuggable. This configuration is ideal for debugging only game modules.

==== String Parameter ====
== Name ==
ENGINE_PATH
== Default Value == 
C:\Program Files\Epic Games\UE_4.25\
== Description ==
The path for the engine install.

==== String Parameter ==
== Name == 
PROJECT_NAME
== Default Value == 
MyProject
== Description ==
This is the name of your project and the folder that it's in. (they need to match)
</code></pre>
</li>
<li>Set up your Source Control Management. We use PlasticSCM (requires you to install a plugin).</li>
<li>Check Poll SCM and put <code>@hourly</code></li>
<li>Under Build add 3 Execute Windows batch command.<br />
<pre class="language-bash"><code>FOR /d /r . %%d IN (Intermediate) DO @IF EXIST "%%d" rd /s /q "%%d"
FOR /d /r . %%d IN (Binaries) DO @IF EXIST "%%d" rd /s /q "%%d"

@RD /S /Q "Build"
@RD /S /Q "Saved"
@RD /S /Q ".vs"
del "%PROJECT_NAME%.sln" /s /f /q

===============================

"%ENGINE_PATH%Engine\Binaries\DotNET\UnrealBuildTool.exe" -projectfiles -project="%WORKSPACE%\%PROJECT_NAME%.uproject" -game -rocket -progress
"%ENGINE_PATH%Engine\Binaries\DotNET\UnrealBuildTool.exe" %PROJECT_NAME% %BUILD_CONFIGURATION% Win64 -project="%WORKSPACE%/%PROJECT_NAME%.uproject" -rocket -editorrecompile -progress -noubtmakefiles -NoHotReloadFromIDE -2019

===============================

"%ENGINE_PATH%Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project="%WORKSPACE%\%PROJECT_NAME%.uproject" -noP4 -platform=Win64 -clientconfig=%BUILD_CONFIGURATION% -cook -numcookerstospawn=8 -compressed -EncryptIniFiles -ForDistribution -allmaps -build -stage -pak -prereqs -package -archive -archivedirectory="%WORKSPACE%/Saved/Builds"
</code></pre>
</li>
<li>Done.</li>
</ol>
<p>&nbsp;</p>
<p>If you're using the source build then add <code>-client</code> before <code>-build</code> to build the Client Target otherwise it'll build as &lt;Platform&gt;NoEditor.</p>
<p>&nbsp;</p>
<p>A dedicated server build requires a source build on the Jenkins machine. NOTE: At the time of writing this I haven't got Shipping builds working with Steam and dedicated server. The Steam API doesn't initialize for some reason.</p>
<pre class="language-bash"><code>// Windows Server
"C:\UE4Source\Engine\Binaries\DotNET\UnrealBuildTool.exe" %PROJECT_NAME% %BUILD_CONFIGURATION% Win64 -projectfiles -project="%WORKSPACE%/%PROJECT_NAME%.uproject" -rocket -progress -noubtmakefiles -NoHotReloadFromIDE -2019 -TargetType=Server

"C:\UE4Source\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project="%WORKSPACE%\%PROJECT_NAME%.uproject" -noP4 -platform=Win64 -build -clientconfig=%BUILD_CONFIGURATION% -serverconfig=%BUILD_CONFIGURATION% -cook -stage -pak -generatechunks -EncryptIniFiles -server -serverplatform=Win64 -noclient -archive -archivedirectory="%WORKSPACE%/Saved/Builds"

// Linux Server
"C:\UE4Source\Engine\Binaries\DotNET\UnrealBuildTool.exe" %PROJECT_NAME% %BUILD_CONFIGURATION% Linux -projectfiles -project="%WORKSPACE%/%PROJECT_NAME%.uproject" -rocket -progress -noubtmakefiles -NoHotReloadFromIDE -2019 -TargetType=Server

"C:\UE4Source\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project="%WORKSPACE%\%PROJECT_NAME%.uproject" -noP4 -platform=Linux -build -clientconfig=%BUILD_CONFIGURATION% -serverconfig=%BUILD_CONFIGURATION% -cook -stage -pak -generatechunks -EncryptIniFiles -server -serverplatform=Linux -noclient -archive -archivedirectory="%WORKSPACE%/Saved/Builds"
</code></pre>
<p>&nbsp;</p>
<p>I also recently set up Jenkins for my plugins so they get built every time I do a commit etc.</p>
<pre class="language-bash"><code>"C:\Program Files\Epic Games\UE_4.25\Engine\Build\BatchFiles\RunUAT.bat" BuildPlugin -Plugin="%WORKSPACE%\PLUGINNAMEHERE.uplugin" -Package="%WORKSPACE%\Packaged" -Rocket -VS2019 -TargetPlatforms=Win64</code></pre>
<p>&nbsp;</p>
<p>To push the build to Steam do something like this using the "Conditional step" plugin on Jenkins</p>
<pre class="language-no-highlighting"><code>C:\SteamTools\steamcmd.exe +login USERNAME PASSWORD +run_app_build -desc "cs:%PLASTICSCM_CHANGESET_ID% bn:%BUILD_NUMBER%" C:\SteamTools\tools\ContentBuilder\scripts\app_x.vdf +quit</code></pre>
<p>&nbsp;</p>
<h4>Last notes</h4>
<p>Here are some other resources for this.</p>
<ul>
<li><a href="https://blog.mi.hdm-stuttgart.de/index.php/2017/02/11/uat-automation/" target="_blank" rel="noopener">https://blog.mi.hdm-stuttgart.de/index.php/2017/02/11/uat-automation/</a></li>
<li><a href="https://gist.github.com/drewsberry/235e865eee90dc5e60ff" target="_blank" rel="noopener">https://gist.github.com/drewsberry/235e865eee90dc5e60ff</a></li>
<li><a href="https://cairansteverink.nl/cairansteverink/blog/unreal-engine-4-build-automation-with-jenkins-and-perforce/" target="_blank" rel="noopener">https://cairansteverink.nl/cairansteverink/blog/unreal-engine-4-build-automation-with-jenkins-and-perforce/</a></li>
</ul>
<p>&nbsp;</p>
<p>until next time</p>
<p>&nbsp;</p>
    