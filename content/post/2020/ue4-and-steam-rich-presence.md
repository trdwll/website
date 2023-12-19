
+++
title = "UE4 and Steam Rich Presence"
description = "Adding some cool stuff into your game with Steam."
date = 2020-12-01T14:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p><strong>NOTE: If you're wanting a Steam wrapper for UE4 then check out <a href="https://github.com/trdwll/SteamBridge/" target="_blank" rel="noopener">SteamBridge</a>. If you use SteamBridge it already has the code below so you won't need to do any code portion of this guide.</strong></p>
<p>&nbsp;</p>
<p>So you're wanting some cool Rich Presence for your game right?</p>
<p><img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/steamworks_docs/english/party_rp.jpg" alt="" width="286" height="369" /> &nbsp;<img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/steamworks_docs/english/rp_group_images.jpg" alt="" width="606" height="225" /></p>
<p>Cool so here's a quick guide on doing this in C++ in UE4. (don't worry, the methods are exposed to BP)</p>
<p>&nbsp;</p>
<ol>
<li>Go to your projects Build.cs and add Steamworks. <code>PrivateDependencyModuleNames.AddRange(new string[] { "Steamworks" });</code></li>
<li>Regenerate your project and open your solution. Add the following code to whatever class you want. I chose to do this in the GameInstance as it exists for the lifetime of the game.<br />
<pre class="language-cpp"><code>UFUNCTION(BlueprintCallable, Category = "GameInstance")
void SetSteamRichPresence(const FString&amp; Key, const FString&amp; Value);

UFUNCTION(BlueprintCallable, Category = "GameInstance")
void ClearSteamRichPresence();

// At the time of writing this sdk version 150 is released, but UE4 only has 147. This doesn't matter, but just a note.
#include "ThirdParty/Steamworks/Steamv147/sdk/public/steam/steam_api.h"

void UCGameInstance::SetSteamRichPresence(const FString&amp; Key, const FString&amp; Value)
{
	SteamFriends()-&gt;SetRichPresence(TCHAR_TO_UTF8(*Key), TCHAR_TO_UTF8(*Value));
}
void UCGameInstance::ClearSteamRichPresence()
{
	SteamFriends()-&gt;ClearRichPresence();
}</code></pre>
</li>
<li>Before you can go off and do what I did above you should know that you have to make a json file with the strings that can be set. Yeah, the messages have to be uploaded to Steam. 🙁</li>
<li>Head over to <a href="https://partner.steamgames.com/doc/features/enhancedrichpresence" target="_blank" rel="noopener">Steam</a> to view more details on doing this, but I'll show you a quick breakdown.</li>
<li>Sign into Steam's Partner <a href="https://partner.steamgames.com" target="_blank" rel="noopener">site</a>, then navigate to Steamworks settings, and then under Community select Rich Presence.<br /><img src="https://files.trdwll.net/2020/11/05/screenshot_2020-11-05_033207_dC9nSe8.png" /><br /><br /></li>
<li>Here's a short example of a localization file for rich presence. (See this <a href="https://partner.steamgames.com/doc/features/enhancedrichpresence" target="_blank" rel="noopener">page</a> to understand how it works)<br />
<pre class="language-json"><code>"lang"
{
	"english"
	{
		"tokens"
		{
			"#Status_AtMainMenu"	"At the main menu"
			"#Status_WaitingForMatch"	"Waiting for match"
			"#Status_Winning"	"Winning"
			"#Status_Losing"	"Losing"
			"#Status_Tied"	"Tied"
			"#Status_JoiningMatch"	"Joining a match"
			"#Status_InAParty"	"In a party"
		}
    }
}</code></pre>
</li>
<li>Here's how it looks. <br /><img src="https://files.trdwll.net/2020/11/05/screenshot_2020-11-05_034609.png" width="459" height="205" /> &nbsp;<img src="https://files.trdwll.net/2020/11/05/screenshot_2020-11-05_034713.png" /></li>
<li>Congrats you've added Steam Rich Presence to your project!</li>
</ol>
<p>&nbsp;</p>
<p>until next time</p>
    