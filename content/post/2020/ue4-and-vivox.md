
+++
title = "UE4 and Vivox"
description = "Implementing Vivox into your UE4 project."
date = 2020-11-18T15:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>So you want a cross-platform and scalable voice chat? Great, let's begin.</p>
<h3>Prerequisites</h3>
<ul>
<li>A <a href="https://developer.vivox.com/" target="_blank" rel="noopener">Vivox developer account</a> (you need a v5 account so ask for a v5 account via email)</li>
<li>A Vivox app</li>
<li>A C++ UE4 project (or ability to add C++)</li>
<li>Patience</li>
</ul>
<p><strong>NOTE: Make sure you check this or like I said above email the support for a v5 account.</strong></p>
<p><img src="https://files.trdwll.net/2020/11/08/screenshot_2020-11-08_040526.png" width="778" height="126" /></p>
<p>&nbsp;</p>
<h4>BeginPlay()</h4>
<p>Cool once you have your app and credentials then proceed to step 1.</p>
<p>So most of this will be implemented in your GameInstance, GameMode, and PlayerController. <em>If you have better classes to add this to then by all means reach out and let me know. </em>You could also just download the example project by Vivox instead of reading this post if you want to see their implementation.</p>
<p>You can skip the guide and just download the project if you'd like. Get it <a href="https://files.trdwll.net/2020/11/08/vivoxexample.zip" target="_blank" rel="noopener">here</a>.</p>
<p>&nbsp;</p>
<ol>
<li>Download the <a href="https://developer.vivox.com/downloads" target="_blank" rel="noopener">SDK</a> (Unreal Windows SDK) from Vivox. (at the time of writing this the SDK is on version 5.12.0)</li>
<li>Add the plugin to your Plugins folder in your project and then edit your <strong>Build.cs</strong> file and add the following. <br />
<pre class="language-cpp"><code>if (Target.Type != TargetRules.TargetType.Server &amp;&amp; Target.Platform == UnrealTargetPlatform.Win64)
{
    PublicDefinitions.Add("WITH_VIVOXCORE=1");
    PrivateDependencyModuleNames.AddRange(new string[] { "VivoxCore" });
}
else
{
    PublicDefinitions.Add("WITH_VIVOXCORE=0");
}</code></pre>
</li>
<li>One quick note before you start writing code, make sure you add your GameInstance as the default one in Edit -&gt; Project Settings.</li>
<li>Go to your <strong>GameInstance</strong> and add the following. (I didn't add the code directly to the post since it's a few hundred lines - instead, you can get it <a href="https://files.trdwll.net/2020/11/08/vivoxgameinstance.txt" target="_blank" rel="noopener">here</a>.)<br /><strong>(NOTE: I'm not 100% sure if the muting and audio device code works, I just threw it together)</strong></li>
<li>Now to your <strong>PlayerController</strong> and <strong>GameMode</strong> classes.<br />
<pre class="language-cpp"><code>#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"

#include "MyPlayerController.generated.h"

UCLASS()
class VIVOXEXAMPLE_API AMyPlayerController : public APlayerController
{
	GENERATED_BODY()

public:
	UFUNCTION(Client, Unreliable)
	void ClientJoinVoice(const uint8 TeamNumber, const FString&amp; SessionID);
};


// -------------------------------------------- CPP
#include "MyPlayerController.h"

#include "MyGameInstance.h"

void AMyPlayerController::ClientJoinVoice_Implementation(const uint8 TeamNumber, const FString&amp; SessionID)
{
	if (!IsPrimaryPlayer())
	{
		return;
	}

	if (IsLocalController())
	{
		if (UMyGameInstance* const GI = GetWorld()-&gt;GetGameInstance&lt;UMyGameInstance&gt;())
		{
#if WITH_VIVOXCORE
			GI-&gt;JoinVoiceChannels(TeamNumber, SessionID);
#endif
		}
	}
}


//-------------------------------------------------------------------------------------------
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"

#include "MyGameModeBase.generated.h"

UCLASS()
class VIVOXEXAMPLE_API AMyGameModeBase : public AGameModeBase
{
	GENERATED_BODY()

public:
	AMyGameModeBase();

	virtual void PostLogin(APlayerController* NewPlayer) override;

private:
	FString m_VivoxServerGuid;
};

// -------------------------------------------- CPP
#include "MyGameModeBase.h"
#include "MyPlayerController.h"

AMyGameModeBase::AMyGameModeBase()
{
	m_VivoxServerGuid = FGuid::NewGuid().ToString(EGuidFormats::DigitsWithHyphens);
}

void AMyGameModeBase::PostLogin(APlayerController* NewPlayer)
{
	Super::PostLogin(NewPlayer);

	if (AMyPlayerController* const ConnectingPlayerController = Cast&lt;AMyPlayerController&gt;(NewPlayer))
	{
		// TODO: Here you should get the PlayerState or whatever to get the players team - in Shifted we used an enum to determine teams (which is a uint8)
		ConnectingPlayerController-&gt;ClientJoinVoice(1, m_VivoxServerGuid);
	}
}
</code></pre>
</li>
<li>Should be good and working. If it isn't then feel free to reach out via Discord (trdwll#2006) or email (<a href="mailto:russ@trdwll.com">russ@trdwll.com</a>).</li>
</ol>
<p>&nbsp;</p>
<h4>Last notes</h4>
<p>So in the GameMode, I'm generating a guid for server identification. You could replace this with the actual session id (if using the session system in UE4) or you could even set it to the SteamID of the server (if using Steam) etc. The possibilities here are endless. You do however want a unique id for it so all players even in different servers don't join the same channel. 😁</p>
<p>This probably isn't the best or even the only way to implement Vivox, but I can say it does work. This is very similar to the implementation I did for Shifted and it's also mainly from the example project that Vivox made.</p>
<p>I also didn't implement push to talk here, but it's 100% doable. I believe the example project from Vivox has PTT.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>I originally was going to post this over Summer 2020, but I never finished the post. So sorry for the delay, but it's finally here. 😀</p>
<p>&nbsp;</p>
<p>until next time</p>
    