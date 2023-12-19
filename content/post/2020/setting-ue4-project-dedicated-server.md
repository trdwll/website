
+++
title = "Setting up a UE4 Project for Dedicated Server"
description = "A quick guide on how to setup dedicated server."
date = 2020-01-20T06:26:55Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>Ready to build your game's dedicated server? Whoa there buddy. We have some work to do before you can.</p>
<p><strong>Before you start down the road of following this guide make sure you have ~130GB free storage for the engine. </strong></p>
<ol>
<li>Download <a href="https://github.com/epicgames/unrealengine">UnrealEngine</a> from GitHub. If you don't have access to this then go and follow this <a href="https://www.unrealengine.com/en-US/ue4-on-github">guide</a>.<br />You can either download the zip (<a href="https://github.com/EpicGames/UnrealEngine/archive/release.zip">release</a>) or do a <em>git clone</em>.</li>
<li>Go into the directory where you downloaded the engine and run <strong>Setup.bat</strong>.</li>
<li>Run <strong>GenerateProjectFiles.bat</strong> and then open <strong>UE4.sln</strong>.</li>
<li>Select <strong>Development Editor</strong>, <strong>Win64</strong>, and <strong>UE4</strong> then press Local Windows Debugger (or Debug -&gt; Start Debugging or Build -&gt; Build Solution). This will take a while (~40 minutes) so just let it do its thing.<br /><img style="height: 40px; width: 800px;" src="https://files.trdwll.net/2020/01/20/wtnthn.png" alt="" /></li>
<li>After it's completed the project selector will show up (if you had no errors) and then you can just close the editor and Visual Studio.</li>
<li>Go to your project and right click your uproject (Switch Unreal Engine version) then select the Source build.<br /><img style="height: 108px; width: 454px;" src="https://files.trdwll.net/2020/01/20/tgr3hh.png" alt="" /></li>
<li>Create a Server and Client target.cs file.<br /><img style="height: 123px; width: 619px;" src="https://files.trdwll.net/2020/01/20/mzrluk.png" alt="" /><br />The <strong>Client.Target.cs</strong> file will look similar to: (download example <a href="https://files.trdwll.net/2020/01/21/exampleprojectclienttarget.cs" target="_blank" rel="noopener">ExampleProjectClient.Target.cs</a>)
<div>
<pre class="language-csharp"><code>using UnrealBuildTool;
using System.Collections.Generic;

public class ExampleProjectClientTarget : TargetRules
{
    public ExampleProjectClientTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Client;
        DefaultBuildSettings = BuildSettingsVersion.V2;
        ExtraModuleNames.Add("ExampleProject");
    }
}</code></pre>
</div>
<div>The <strong>Server.Target.cs</strong> file will look similar to: (download example <a href="https://files.trdwll.net/2020/01/21/exampleprojectservertarget.cs" target="_blank" rel="noopener">ExampleProjectServer.Target.cs</a>)</div>
<div>
<pre class="language-csharp"><code>using UnrealBuildTool;
using System.Collections.Generic;

public class ExampleProjectServerTarget : TargetRules
{
    public ExampleProjectServerTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Server;
        DefaultBuildSettings = BuildSettingsVersion.V2;
        ExtraModuleNames.Add("ExampleProject");
    }
}</code></pre>
</div>
<p>&nbsp;</p>
</li>
<li>Check out my guide on using <a href="https://trdwll.com/blog/using-unreal-frontend-package-your-project/">Unreal Frontend</a>.</li>
<li>In Unreal Frontend select <strong>Platform</strong><em>Server</em> and <strong>Platform</strong><em>Client. </em>You don't need <strong>Platform</strong><em>NoEditor</em> etc. (By using Client builds it removes unnecessary code that allows listen servers.) Also, your Unreal Frontend should be from your Source build not binary build from the launcher. (as from the photo above my Source build is in D:\dev\UnrealEngine so my UF is <strong>D:\dev\UnrealEngine\Engine\Binaries\Win64</strong>.)<br /><img style="height: 37px; width: 114px;" src="https://files.trdwll.net/2020/01/20/image-20200120102325-2.png" /></li>
<li>Just build your project like the <a href="https://trdwll.com/blog/using-unreal-frontend-package-your-project/">UF guide</a>.</li>
<li>If you're not using Sessions, Steam, or any other third party to handle connections you can connect to the dedicated server by doing <strong>open &lt;ip&gt;</strong> in the console in your Client.exe. If you're in Shipping build then the console is disabled so you'd need to do a server browser or even a button on your main menu etc to execute a console command.<br /><img style="height: 187px; width: 533px;" src="https://files.trdwll.net/2020/01/20/image-20200120111008-1.png" /></li>
<li>Once the project has been built you can boot up the <strong>Server.exe -log&nbsp; </strong>or you can put it on a <a href="https://en.wikipedia.org/wiki/Virtual_private_server">VPS</a> or Dedicated server etc and boot it from there.<br /><img style="height: 124px; width: 528px;" src="https://files.trdwll.net/2020/01/20/image-20200120103725-1.png" /><br />In other words, zip up the WindowsServer (or whateverServer) and put that on your server to boot if you want other players to connect. (or you could <a href="https://portforward.com/unreal/">port forward</a> etc)</li>
</ol>
<p>&nbsp;</p>
<h3>Using server without building binaries (for development or debugging)</h3>
<p>Server.bat</p>
<div>
<pre class="language-markdown"><code>@echo off
"Path\To\UE4Editor.exe" "Path\To\My\Project.uproject" -log -server</code></pre>
</div>
<p>Client.bat</p>
<div>
<pre class="language-markdown"><code>@echo off
"Path\To\UE4Editor.exe" "Path\To\My\Project.uproject" -log -game -windowed -ResX=1080 -ResY=720</code></pre>
</div>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>until next time</p>
    