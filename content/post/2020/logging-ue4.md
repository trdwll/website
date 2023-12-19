
+++
title = "Logging in UE4"
description = "How to log in Unreal Engine 4."
date = 2020-04-05T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>Macros that I use for logging/printing.</p>

<p>Use them via <code>PRINT(&quot;MyStringToPrint&quot;);</code> or <code>LOG(&quot;MyStringToLog&quot;);</code> or <code>LOG(&quot;MyStringToLog %f&quot;, 3.0f);</code> etc.</p>

<div>
<pre>
<code class="language-cpp">#if 1
#include "Engine/Engine.h"
#include "DrawDebugHelpers.h"

#define GETSTR(text, ...) *FString::Printf(TEXT(text), ##__VA_ARGS__)

#define PRINT(color, text, ...) if (GEngine) GEngine-&gt;AddOnScreenDebugMessage(-1, 10.f, color, CUR_CLASS_LINE + ": " + GETSTR(text, ##__VA_ARGS__))
#define PRINT_S(text, ...) if (GEngine) GEngine-&gt;AddOnScreenDebugMessage(-1, 10.f, FColor::Yellow, CUR_CLASS_LINE + ": [SUCCESS] " + GETSTR(text, ##__VA_ARGS__))
#define PRINT_E(text, ...) if (GEngine) GEngine-&gt;AddOnScreenDebugMessage(-1, 10.f, FColor::Red, CUR_CLASS_LINE + ": [ERROR] " + GETSTR(text, ##__VA_ARGS__))
#define PRINT_W(text, ...) if (GEngine) GEngine-&gt;AddOnScreenDebugMessage(-1, 10.f, FColor::Orange, CUR_CLASS_LINE + ": [WARNING] " + GETSTR(text, ##__VA_ARGS__))
#define LOG(text, ...) UE_LOG(LogTemp, Log, TEXT("%s: %s"), *CUR_CLASS, GETSTR(text, ##__VA_ARGS__))
#define LOG_S(text, ...) UE_LOG(LogTemp, Log, TEXT("%s: [SUCCESS] %s"), *CUR_CLASS, GETSTR(text, ##__VA_ARGS__))
#define LOG_W(text, ...) UE_LOG(LogTemp, Warning, TEXT("%s: [WARNING] %s"), *CUR_CLASS, GETSTR(text, ##__VA_ARGS__))
#define LOG_E(text, ...) UE_LOG(LogTemp, Error, TEXT("%s: [ERROR] %s"), *CUR_CLASS, GETSTR(text, ##__VA_ARGS__))
#define LOG_D(text, ...) UE_LOG(LogTemp, Display, TEXT("%s: [WARNING] %s"), *CUR_CLASS, GETSTR(text, ##__VA_ARGS__))

#define PRINT_LOG(color, text, ...) PRINT(color, text, ##__VA_ARGS__); LOG(text, ##__VA_ARGS__);
#define PRINT_LOG_S(text, ...) PRINT_S(text, ##__VA_ARGS__); LOG_S(text, ##__VA_ARGS__);
#define PRINT_LOG_W(text, ...) PRINT_W(text, ##__VA_ARGS__); LOG_W(text, ##__VA_ARGS__);
#define PRINT_LOG_E(text, ...) PRINT_E(text, ##__VA_ARGS__); LOG_E(text, ##__VA_ARGS__);

/** Current Class Name + Function Name where this is called! */
#define CUR_CLASS_FUNC (FString(__FUNCTION__))

/** Current Class where this is called! */
#define CUR_CLASS (FString(__FUNCTION__).Left(FString(__FUNCTION__).Find(TEXT(":"))) )

/** Current Function Name where this is called! */
#define CUR_FUNC (FString(__FUNCTION__).Right(FString(__FUNCTION__).Len() - FString(__FUNCTION__).Find(TEXT("::")) - 2 ))

/** Current Line Number in the code where this is called! */
#define CUR_LINE  (FString::FromInt(__LINE__))

/** Current Class and Line Number where this is called! */
#define CUR_CLASS_LINE (CUR_CLASS + "(" + CUR_LINE + ")")

/** Current Function Signature where this is called! */
#define CUR_FUNCSIG (FString(__FUNCSIG__))
#else
#define PRINT(color, text)
#define PRINT_S(text)
#define PRINT_E(text)
#define LOG(text, ...)
#define LOG_S(text, ...)
#define LOG_W(text, ...)
#define LOG_E(text, ...)
#define LOG_D(text, ...)
#define PRINT_LOG_S(text)
#define PRINT_LOG_W(text)
#define PRINT_LOG_E(text)
#endif</code></pre>
</div>

<h2><strong>UE_LOG</strong></h2>

<h3>Custom categories</h3>

<p>You can change the log category (LogTemp) to your own by defining your category like so.</p>

<h4>MyGame.H</h4>

<pre>
//General Log
DECLARE_LOG_CATEGORY_EXTERN(LogMyGame, Log, All);
//Logging during game startup
DECLARE_LOG_CATEGORY_EXTERN(LogMyGameInit, Log, All);
//Logging for your AI system
DECLARE_LOG_CATEGORY_EXTERN(LogMyGameAI, Log, All);
//Logging for a that troublesome system
DECLARE_LOG_CATEGORY_EXTERN(LogMyGameSomeSystem, Log, All);
//Logging for Critical Errors that must always be addressed
DECLARE_LOG_CATEGORY_EXTERN(LogMyGameCriticalErrors, Log, All);
</pre>

<h4>MyGame.CPP</h4>

<pre>
#include &quot;MyGame.h&quot;

//General Log
DEFINE_LOG_CATEGORY(LogMyGame);
//Logging during game startup
DEFINE_LOG_CATEGORY(LogMyGameInit);
//Logging for your AI system
DEFINE_LOG_CATEGORY(LogMyGameAI);
//Logging for some system
DEFINE_LOG_CATEGORY(LogMyGameSomeSystem);
//Logging for Critical Errors that must always be addressed
DEFINE_LOG_CATEGORY(LogMyGameCriticalErrors);
</pre>

<p>So then after you have your own category you&#39;d use it like <code>UE_LOG(<strong>LogMyGame</strong>, Log, TEXT(&quot;Your message&quot;));</code>.</p>

<h3>Verbosity</h3>

<p>UE_LOG(LogTemp, <strong>Warning</strong>, TEXT(&quot;Your message&quot;));</p>

<p>You can change the Warning to be one of the following.</p>

<ul>
	<li>Fatal - Fatal level logs are always printed to console and log files and crashes even if logging is disabled.</li>
	<li>Error - Error level logs are printed to console and log files. <span style="color:#ff0000">These appear red by default.</span></li>
	<li>Warning - Warning level logs are printed to console and log files. <span style="color:#ffff00">These appear yellow by default.</span></li>
	<li>Display - Display level logs are printed to console and log files.</li>
	<li>Log - Log level logs are printed to log files but not to the in-game console. They can still be viewed in the editor as they appear via the Output Log window.</li>
	<li>Verbose - Verbose level logs are printed to log files but not the in-game console. This is usually used for detailed logging and debugging.</li>
	<li>VeryVerbose - VeryVerbose level logs are printed to log files but not the in-game console. This is usually used for very detailed logging that would otherwise spam output.</li>
</ul>

<h3>Formatting</h3>

<ul>
	<li>FString - <code>UE_LOG(YourLog,Warning,TEXT(&quot;MyCharacter&#39;s Name is %s&quot;), *MyCharacter-&gt;GetName() );</code></li>
	<li>bool - <code>UE_LOG(YourLog,Warning,TEXT(&quot;MyCharacter&#39;s Bool is %s&quot;), (MyCharacter-&gt;MyBool ? TEXT(&quot;True&quot;) : TEXT(&quot;False&quot;)));</code></li>
	<li>int - <code>UE_LOG(YourLog,Warning,TEXT(&quot;MyCharacter&#39;s Health is %d&quot;), MyCharacter-&gt;Health);</code></li>
	<li>float - <code>UE_LOG(YourLog,Warning,TEXT(&quot;MyCharacter&#39;s Health is %f&quot;), MyCharacter-&gt;Health);</code></li>
	<li>FVector - <code>UE_LOG(YourLog,Warning,TEXT(&quot;MyCharacter&#39;s Location is %s&quot;), *MyCharacter-&gt;GetActorLocation().ToString());</code></li>
	<li>FName - <code>UE_LOG(YourLog,Warning,TEXT(&quot;MyCharacter&#39;s FName is %s&quot;), *MyCharacter-&gt;GetFName().ToString());</code></li>
	<li>FString, int, and float - <code>UE_LOG(YourLog,Warning,TEXT(&quot;%s has health %d, which is %f percent of total health&quot;), *MyCharacter-&gt;GetName(), MyCharacter-&gt;Health, MyCharacter-&gt;HealthPercent);</code></li>
</ul>

<p>&nbsp;</p>

<p>GEngine-&gt;AddOnScreenDebugMessage works very similar to UE_LOG so no need to add info for it.</p>

<p>Most of this was written by Rama (from the UE4 wiki that was closed down).</p>

<p>&nbsp;</p>

<p>until next time</p>
    