
+++
title = "Feedback via Discord in UE4"
description = "I show you how to allow your players to send feedback directly to your discord."
date = 2020-09-26T19:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p><a href="https://files.trdwll.net/2020/09/26/image.png" target="_blank" rel="noopener"><img style="height: 273px; width: 300px;" src="https://files.trdwll.net/2020/09/26/image.png" /></a></p>
<p>&nbsp;</p>
<p>You can just download the class here if you're lazy. <a href="https://files.trdwll.net/2020/09/26/mbpfl.h" target="_blank" rel="noopener">mbpfl.h</a> and <a href="https://files.trdwll.net/2020/09/26/mbpfl.cpp" target="_blank" rel="noopener">mbpfl.cpp</a></p>
<p>&nbsp;</p>
<ol>
<li>Create a BlueprintFunctionLibrary class in C++ and add these includes and defines.
<div>
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">#if PLATFORM_WINDOWS
#include "Windows/WindowsPlatformMisc.h"
#elif PLATFORM_LINUX
#include "Linux/LinuxPlatformMisc.h"
#elif PLATFORM_MAC
#include "Mac/MacPlatformMisc.h"
#endif

#include "GameFramework/GameUserSettings.h"

#define BUG_REPORT_WEBHOOK_URL "YOURWEBHOOKURLHERE"
#define MYGAME_VERSION "v1.0-pre-alpha"
#define DEFAULT_ICON_URL "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"</code></pre>
</div>
</div>
</div>
</div>
<p>&nbsp;</p>
</li>
<li>Add the following enums and structs to the header.
<div>
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">UENUM(BlueprintType)
enum class EBugReportCategory : uint8
{
	Map,
	Weapon,
	Other
};

UENUM(BlueprintType)
enum class EBugReportPriority : uint8
{
	Crash,
	High,
	Med,
	Low
};

USTRUCT()
struct FDiscordMessageField
{
	GENERATED_BODY()

	UPROPERTY()
	FString name;
	UPROPERTY()
	FString value;
	UPROPERTY()
	bool binline;
};

USTRUCT()
struct FDiscordMessageEmbedAuthor
{
	GENERATED_BODY()

	UPROPERTY()
	FString name;
	UPROPERTY()
	FString url;
	UPROPERTY()
	FString icon_url;

	FDiscordMessageEmbedAuthor() : url("https://trdwll.com"), icon_url(DEFAULT_ICON_URL) {}
};

USTRUCT()
struct FDiscordMessageEmbedFooter
{
	GENERATED_BODY()

	UPROPERTY()
	FString text;
	UPROPERTY()
	FString icon_url;

	FDiscordMessageEmbedFooter() : icon_url(DEFAULT_ICON_URL) {}
};

USTRUCT()
struct FDiscordMessageEmbed
{
	GENERATED_BODY()

	UPROPERTY()
	FString title;
	UPROPERTY()
	FString description;
	UPROPERTY()
	uint32 color;
	UPROPERTY()
	TArray&lt;FDiscordMessageField&gt; fields;
	UPROPERTY()
	FDiscordMessageEmbedAuthor author;
	UPROPERTY()
	FDiscordMessageEmbedFooter footer;
	UPROPERTY()
	FString timestamp;

	FDiscordMessageEmbed() : color(720640), timestamp(FDateTime::Now().ToIso8601()) {}

	uint32 GetColor(const EBugReportPriority Priority)
	{
		switch (Priority)
		{
		case EBugReportPriority::Crash: return 16711680;
		case EBugReportPriority::High: return 12389388;
		case EBugReportPriority::Med: return 16742912;
		default:
		case EBugReportPriority::Low: return 720640;
		}
	}
};

USTRUCT()
struct FDiscordMessage
{
	GENERATED_BODY()

	UPROPERTY()
	FString username;
	UPROPERTY()
	FString avatar_url;
	UPROPERTY()
	FString content;
	UPROPERTY()
	TArray&lt;FDiscordMessageEmbed&gt; embeds;

	FDiscordMessage() : avatar_url(DEFAULT_ICON_URL) {}
};

USTRUCT(BlueprintType)
struct FBugReportUserData
{
	GENERATED_BODY()

	UPROPERTY(BlueprintReadWrite)
	FString Author;
	UPROPERTY(BlueprintReadWrite)
	FVector Location;
	UPROPERTY(BlueprintReadWrite)
	FString MapName;
	UPROPERTY(BlueprintReadWrite)
	FString Message;
};</code></pre>
</div>
</div>
</div>
</div>
</li>
<li>Add the following to your header file.
<div>
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">	// Thanks to Rama for this method
	// GetEnumValueAsString&lt;EEnumType&gt;("EEnumType", Value);
	template&lt;typename TEnum&gt;
	static FString GetEnumValueAsString(const FString&amp; Name, TEnum Value)
	{
		const UEnum* enumPtr = FindObject&lt;UEnum&gt;(ANY_PACKAGE, *Name, true);
		if (!enumPtr)
		{
			return FString("Invalid");
		}
		return enumPtr-&gt;GetNameByValue((int64)Value).ToString();
	}

	UFUNCTION(BlueprintCallable, Category = "Discord")
	static void SubmitBugReport(const EBugReportCategory Category, const EBugReportPriority Priority, const FBugReportUserData&amp; AuthorData, FString&amp; ReportID, bool bIncludeSpecs = true);

	/**
	 * Gets the number of RAM on the system
	 */
	UFUNCTION(BlueprintPure)
	static FORCEINLINE int32 GetTotalRAM()
	{
		const FPlatformMemoryConstants&amp; MemoryConstants = FPlatformMemory::GetConstants();
		return MemoryConstants.TotalPhysicalGB;
	}

	UFUNCTION(BlueprintPure)
	static FString GetGameResolution() { return *FString::Printf(TEXT("%dx%d"), UGameUserSettings::GetGameUserSettings()-&gt;GetScreenResolution().X, UGameUserSettings::GetGameUserSettings()-&gt;GetScreenResolution().Y); }

	/**
	 * Gets the CPU Brand Name information.
	 */
	UFUNCTION(BlueprintPure)
	static FString GetCPUBrandName()
	{
#if PLATFORM_WINDOWS
		return FWindowsPlatformMisc::GetCPUBrand();
#elif PLATFORM_LINUX
		return FLinuxPlatformMisc::GetCPUBrand();
#elif PLATFORM_MAC
		return FMacPlatformMisc::GetCPUBrand();
#endif
	}

	/**
	 * Gets the CPU Vendor Name information.
	 */
	UFUNCTION(BlueprintPure)
	static FString GetCPUVendorName()
	{
#if PLATFORM_WINDOWS
		return FWindowsPlatformMisc::GetCPUVendor();
#elif PLATFORM_LINUX
		return FLinuxPlatformMisc::GetCPUVendor();
#elif PLATFORM_MAC
		return FMacPlatformMisc::GetCPUVendor();
#endif
	}

	/**
	 * Gets the GPU Brand Name information.
	 */
	UFUNCTION(BlueprintPure)
	static FString GetGPUBrandName()
	{
#if PLATFORM_WINDOWS
		return FWindowsPlatformMisc::GetPrimaryGPUBrand();
#elif PLATFORM_LINUX
		return FLinuxPlatformMisc::GetPrimaryGPUBrand();
#elif PLATFORM_MAC
		return FMacPlatformMisc::GetPrimaryGPUBrand();
#endif
	}

	/**
	 * Gets the GPU Driver information.
	 */
	UFUNCTION(BlueprintPure)
	static FORCEINLINE FString GetGPUDriverInfo() { return GRHIAdapterUserDriverVersion; }</code></pre>
</div>
</div>
</div>
</div>
<p>&nbsp;</p>
</li>
<li>
<p>In your BPFL source file add includes.</p>
</li>
<li>
<div>
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">#include "Http.h"
#include "Interfaces/IHttpRequest.h"
#include "JsonObjectConverter.h"</code></pre>
</div>
</div>
</div>
</div>
</li>
<li>The implementation for <code>SubmitBugReport</code>.
<div>
<div>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">void UMBPFL::SubmitBugReport(const EBugReportCategory Category, const EBugReportPriority Priority, const FBugReportUserData&amp; AuthorData, FString&amp; ReportID, bool bIncludeSpecs)
{
	// Just some quick checks to prevent spamming
	if (AuthorData.Author == "" || AuthorData.MapName == "" || AuthorData.Message == "")
	{
		return;
	}

	if (FHttpModule* http = &amp;FHttpModule::Get())
	{
		TSharedRef&lt;IHttpRequest&gt; request = http-&gt;CreateRequest();
		request-&gt;SetVerb("POST");
		request-&gt;SetHeader("Content-Type", "application/json");
		request-&gt;SetURL(BUG_REPORT_WEBHOOK_URL);

		ReportID = FGuid::NewGuid().ToString();

		// Create the embed for the report
		FDiscordMessageEmbed embed;
		embed.title = GetEnumValueAsString&lt;EBugReportCategory&gt;("EBugReportCategory", Category);
		embed.author.icon_url = "";
		embed.author.name = AuthorData.Author;
		embed.description = AuthorData.Message;
		embed.color = embed.GetColor(Priority);
		embed.fields.Add({ "Priority", GetEnumValueAsString&lt;EBugReportPriority&gt;("EBugReportPriority", Priority) });
		embed.fields.Add({ "Location", AuthorData.Location.ToString(), true });
		embed.fields.Add({ "Map", AuthorData.MapName, true });
		embed.footer.text = FString::Printf(TEXT("MYGame %s | %s"), *FString(MYGAME_VERSION), *ReportID);

		FDiscordMessage data;
		data.username = "Bug Reporter";
		data.embeds.Add(embed);

		// Don't show "private" information unless the player wants to
		if (bIncludeSpecs)
		{
			// Create another embed for the users pc specs
			FDiscordMessageEmbed embed2;
			embed2.title = FString::Printf(TEXT("%s PC Specs"), *AuthorData.Author);
			embed2.color = embed.GetColor(Priority);
			embed2.fields.Add({ "Resolution", GetGameResolution(), true });
			embed2.fields.Add({ "RAM", FString::Printf(TEXT("%dGB"), GetTotalRAM()), true });
			embed2.fields.Add({ "CPU", GetCPUBrandName(), true });
			embed2.fields.Add({ "GPU", GetGPUBrandName(), true });
			embed2.fields.Add({ "GPU Driver", GetGPUDriverInfo(), true });
			data.embeds.Add(embed2);
		}

		FString OutputString;
		FJsonObjectConverter::UStructToJsonObjectString(data, OutputString);
		OutputString = OutputString.Replace(TEXT("binline"), TEXT("inline"));

		request-&gt;SetContentAsString(OutputString);
		request-&gt;ProcessRequest();
	}
}</code></pre>
</div>
</div>
</div>
</div>
</li>
<li>Add <code>"Http", "Json", "JsonUtilities", "RHI"</code> to your <strong>Project.Build.cs</strong> under PublicDependencyModuleNames.</li>
<li>Head on over to your discord server Server Settings -&gt; Integrations -&gt; Create Webhook. Then replace the URL for BUG_REPORT_WEBHOOK_URL with the one it gives you.</li>
</ol>
<div>&nbsp;</div>
<div>&nbsp;</div>
<div>until next time</div>
<p>&nbsp;</p>
    