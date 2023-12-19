
+++
title = "Using Other Types in UE4 BP"
description = "I show you how to quickly expose different types to BP in UE4."
date = 2020-11-24T13:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>While building out SteamBridge I needed a way to access <code>SteamID</code> in BP which happens to be a <code>uint64</code> so I'm not able to directly. Here's the solution I came up with and I must say it's not the most ideal solution as I mainly needed <code>typedef</code>s, but this works.</p>
<p>&nbsp;</p>
<pre class="language-cpp"><code>USTRUCT(BlueprintType)
struct FUint64
{
	GENERATED_BODY()

	uint64 Value;

	operator uint64() const { return Value; }

	FUint64() : Value(0) {}
	FUint64(uint64 value) : Value(value) {}
};

USTRUCT(BlueprintType)
struct FMyCoolUint64Type : public FUint64 { GENERATED_BODY() using FUint64::FUint64; };</code></pre>
<p>To avoid writing the same <code>FUint64</code> struct for all of the types that just need to be a <code>uint64</code> you can just derive your struct from it and add a <code>using FUint64::FUint64;</code> so we use it's constructors.</p>
<p>You should also add a method in your class to be able to construct this struct in BP since you can't set the value in BP as it's a type that isn't supported. You can add a method to take a string that's converted to a <code>uint64</code> to output the <code>FMyCoolUint64Type</code>.</p>
<pre class="language-cpp"><code>// psudo-code

UFUNCTION(BlueprintCallable)
void makecoolstruct(const FString&amp; convert, FMyCoolUint64Type&amp; type)
{
    type = { FCString::Strtoui64(*convert, NULL, 10) };
// or some conversion from string to type etc
}</code></pre>
<p>&nbsp;</p>
<p>until next time</p>
<p>&nbsp;</p>
    