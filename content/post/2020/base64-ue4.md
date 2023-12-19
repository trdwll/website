
+++
title = "Base64 in UE4"
description = "The base64 methods in UE4 don't work natively with cyrillic etc."
date = 2020-03-15T13:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>While I was looking for projects to contribute to on GitHub I remembered <a href="https://github.com/ufna/VaRest" target="_blank" rel="noopener">VaRest</a> was on GitHub. I headed over to VaRest's repo and was looking at issues. I found the <a href="https://github.com/ufna/VaRest/issues/92" target="_blank" rel="noopener">issue</a> and so I went on my way of finding a <a href="https://github.com/ufna/VaRest/commit/abd16db578c2efb62b4439e05742f4878f25e3e9">solution</a>.</p>
<p>&nbsp;</p>
<p>My solution for encoding was to convert the input string to utf8 and then encode. My solution for decoding was practically the same, I convert the string to a tchar from utf8, decode, and then output the result. Pretty easy right? Yeah no this solution took me about an hour and I had to get some assistance from an acquaintance, because the encoding was adding extra chars on the end and some other random issues.</p>
<pre><code class="language-cpp">FString MyClass::Base64Encode(const FString&amp; Source)
{
	TArray&lt;uint8&gt; ByteArray;
	FTCHARToUTF8 StringSrc = FTCHARToUTF8(Source.GetCharArray().GetData());
	ByteArray.Append((uint8*)StringSrc.Get(), StringSrc.Length());

	return FBase64::Encode(ByteArray);
}

// I don't know why I didn't change this method to just return the string like the encode string above...
bool MyClass::Base64Decode(const FString&amp; Source, FString&amp; Dest)
{
	TArray&lt;uint8&gt; ByteArray;
	bool Success = FBase64::Decode(Source, ByteArray);

	FUTF8ToTCHAR StringSrc = FUTF8ToTCHAR((const ANSICHAR*)ByteArray.GetData(), ByteArray.Num());
	Dest.AppendChars(StringSrc.Get(), StringSrc.Length() + 1);

	return Success;
}</code></pre>
<p>&nbsp;</p>
<p>until next time</p>
    