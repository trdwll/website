
+++
title = "Adding Text Chat to UE4 in C++"
description = "I walk you through adding text chat to your project using C++."
date = 2020-11-10T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>Note, this is a C++ based example. However, it's easily converted to BP.</p>
<p>If you want to just check out the code or skip the guide then you can download the project <a href="https://files.trdwll.net/2020/09/22/textchat.zip" target="_blank" rel="noopener">here</a>.</p>
<p>There are a few things wrong with this setup such as no deletion of messages so you'll keep a copy of them until you exit the game so you're probably going to want to set up a timer to destroy them after x time.</p>
<p>&nbsp;</p>
<ol>
<li>Open your <strong>PlayerController</strong> class and add a struct called <code>FChatMessage</code>.
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">USTRUCT(BlueprintType)
struct FChatMessage
{
	GENERATED_BODY()

	UPROPERTY(BlueprintReadWrite)
	FDateTime Time;

	UPROPERTY(BlueprintReadWrite)
	FString Message;

	UPROPERTY(BlueprintReadWrite)
	FColor Color;

	UPROPERTY(BlueprintReadWrite)
	class APlayerState* Sender;

	FChatMessage() : Time(FDateTime::Now()), Message("No Message"), Color(FColor::White) {}
	FChatMessage(const FString&amp; message) : Time(FDateTime::Now()), Message(message), Color(FColor::White) {}
	FChatMessage(const FDateTime&amp; time, const FString&amp; message, const FColor&amp; color, class APlayerState* sender) : Time(time), Message(message), Color(color), Sender(sender) {}
};</code></pre>
</div>
</div>
</div>
</li>
<li>Add a delegate in the <strong>PlayerController</strong> for receiving chat messages. <code>DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnChatMessageReceived, const FChatMessage&amp;, ChatMessage);</code></li>
<li>Add 2 methods and the delegate to your <strong>PlayerController</strong> class.
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">UFUNCTION(BlueprintCallable, Server, Reliable, WithValidation)
void Server_SendChatMessage(const FChatMessage&amp; ChatMessage);

UFUNCTION(Client, Reliable)
void Client_ReceiveChatMessage(const FChatMessage&amp; ChatMessage);

UPROPERTY(BlueprintAssignable, meta = (DisplayName = "OnChatMessageReceived"))
FOnChatMessageReceived m_OnChatMessageReceived;</code></pre>
</div>
</div>
</div>
</li>
<li>Create the implementation of these methods.
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">bool ATCPlayerController::Server_SendChatMessage_Validate(const FChatMessage&amp; ChatMessage) { return true; }
void ATCPlayerController::Server_SendChatMessage_Implementation(const FChatMessage&amp; ChatMessage)
{
	// Our message is empty or the sender is null so don't send a message
	if (ChatMessage.Message.IsEmpty() || ChatMessage.Sender == nullptr)
	{
		return;
	}

	// Iterate over all clients in the map and send the message to them
	for (FConstPlayerControllerIterator Iterator = GetWorld()-&gt;GetPlayerControllerIterator(); Iterator; ++Iterator)
	{
		if (ATCPlayerController* const PC = Cast&lt;ATCPlayerController&gt;(*Iterator))
		{
			PC-&gt;Client_ReceiveChatMessage(ChatMessage);
		}
	}
}

void ATCPlayerController::Client_ReceiveChatMessage_Implementation(const FChatMessage&amp; ChatMessage)
{
	m_OnChatMessageReceived.Broadcast(ChatMessage);
}</code></pre>
</div>
</div>
</div>
</li>
<li>Now onto the non-code portion of this guide. Create 3 widgets (only 2 if you already have a HUD widget). Let's create <strong>WBP_Chat</strong> and <strong>WBP_ChatEntry</strong>.</li>
<li>In <strong>WBP_Chat</strong> add a scroll box and a text box.<br /><a href="https://files.trdwll.net/2020/09/22/image.png" target="_blank" rel="noopener"><img style="height: 79px; width: 346px;" src="https://files.trdwll.net/2020/09/22/image.png" /></a></li>
<li>In <strong>WBP_Chat</strong> create 2 functions called <em>ToggleChat </em>(with an input of boolean) and <em>AddChatMessage</em> (with an input of our <code>FChatMessage</code> struct).</li>
<li>In <strong>WBP_Chat</strong> implement the event OnTextCommitted for the text box.&nbsp;<br /><a href="https://files.trdwll.net/2020/09/22/image_dA9IXLR.png" target="_blank" rel="noopener"><img style="height: 179px; width: 900px;" src="https://files.trdwll.net/2020/09/22/image_dA9IXLR.png" /></a></li>
<li>In <strong>WBP_Chat</strong> on Construct add our binding for our C++ delegate (<code>FOnChatMessageReceived</code>). <br /><a href="https://files.trdwll.net/2020/09/22/image_dR2NxpK.png"><img style="height: 227px; width: 900px;" src="https://files.trdwll.net/2020/09/22/image_dR2NxpK.png" /></a></li>
<li>In <strong>WBP_Chat</strong> implement <em>AddChatMessage</em>. <br /><a href="https://files.trdwll.net/2020/09/22/image_UIVTptJ.png" target="_blank" rel="noopener"><img style="height: 282px; width: 884px;" src="https://files.trdwll.net/2020/09/22/image_UIVTptJ.png" /></a></li>
<li>In <strong>WBP_Chat</strong> implement <em>ToggleChat</em>.<br /><a href="https://files.trdwll.net/2020/09/22/image_LJ5YsPt.png" target="_blank" rel="noopener"><img style="height: 264px; width: 900px;" src="https://files.trdwll.net/2020/09/22/image_LJ5YsPt.png" /></a></li>
<li>In <strong>WBP_ChatEntry</strong> add a text block. Then make a variable exposed on spawn of our <code>FChatMessage</code> struct.</li>
<li>In <strong>WBP_ChatEntry</strong> on Construct set the text of the text block.<br /><a href="https://files.trdwll.net/2020/09/22/image_ZGd8CuL.png" target="_blank" rel="noopener"><img style="height: 314px; width: 900px;" src="https://files.trdwll.net/2020/09/22/image_ZGd8CuL.png" /></a></li>
<li>Now all you have to do is go into your WBP_HUD or whatever and add the WBP_Chat to it wherever you want. Then spawn your HUD in your HUD class or again wherever you want to.</li>
<li>You also need to add a keybinding for the chat called TextChat.</li>
</ol>
<p>&nbsp;</p>
<p>until next time</p>
    