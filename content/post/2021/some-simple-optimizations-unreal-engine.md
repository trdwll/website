
+++
title = "Some Simple Optimizations in Unreal Engine"
description = "I talk about some simple optimizations you can do in your Unreal Engine project."
date = 2021-05-12T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>When it boils down to it you should profile things before optimizing however, these things can be added without the need to profile. Also, if I'm wrong about any of these or you have any additional tips to add then please reach out via email russ@trdwll.com.</p>
<p>&nbsp;</p>
<ul>
<li>TArray.Reserve(size)
<ul>
<li>This will reserve memory for the array in advance. Do this before modifying an array to prevent allocations in a loop etc.<br />When adding elements to a container in a loop, performances can be impacted because of multiple heap allocations to resize the container.</li>
<li>Also, do this on temporary allocations (see the second example). (if you allocate an array in a method and then return that array later or need to do something specific to the results)<br />
<pre class="language-cpp"><code>// Adds N copies of a character to the end of an array.
void AppendCharacterCopies(char CharToCopy, int32 N, TArray&lt;char&gt;&amp; Result)
{
	if (N &gt; 0)
	{
		Result.Reserve(Result.Num() + N);
		for (int32 Index=0; Index &lt; N; Index++)
		{
			Result.Add(CharToCopy);
		}
	}
}

void AppendCharacterCopies(char CharToCopy, int32 N)
{
	if (N &gt; 0)
	{
		TArray&lt;char&gt; Result;
		Result.Reserve(N);
		for (int32 Index = 0; Index &lt; N; Index++)
		{
			Result.Emplace(CharToCopy);
		}

		// do something with Result
	}
}</code></pre>
</li>
</ul>
</li>
<li>TArray.Emplace(type)
<ul>
<li>By using Emplace over Add you don't create a copy of the type. Really only use emplace on types larger than 8 bytes or rather don't use it on things like ints.</li>
<li><code>Add</code> (or <code>Push</code>) will copy (or move) an instance of the element type into the array.&nbsp;</li>
<li><code>Emplace</code> will use the arguments you give it to construct a new instance of the element type.&nbsp;</li>
</ul>
</li>
<li>Range-based for loops<br />
<ul>
<li>By using range-based for loops you can drop an allocation from the <code>int32 i = 0; ...</code> and it also makes your code a bit cleaner.<br />
<pre class="language-cpp"><code>for (const auto&amp; Elem : MyContainer)
{
	// TArray - Elem
	// TMap - Elem.Key/Elem.Value
}</code></pre>
</li>
</ul>
</li>
<li>Pass by reference
<ul>
<li>Passing by reference you don't copy said member which doesn't do another allocation of the type.</li>
<li>Don't pass normal types (int/float/bool) by reference as that actually can <a href="https://lemire.me/blog/2019/09/05/passing-integers-by-reference-can-be-expensive/" target="_blank" rel="noopener">slow down performance</a>.</li>
<li>Instead of copying an array or any other type <code>TArray&lt;uint8&gt; GetMyArray() const { return MyArray; }</code> return it as a const reference like <code>const TArray&lt;uint8&gt;&amp; GetMyArray() const { return MyArray; }</code> <sub><em>(You can expose this to BP btw)</em></sub></li>
</ul>
</li>
<li>Smaller types
<ul>
<li>Use smaller types like uint8 or uint16 when possible. Sure, uint16 isn't exposed to Blueprint, so that really limits you however, you may not need to expose that to BP.</li>
<li>I only pass by value if the type is &lt; 8 bytes.<br />
<table>
<thead>
<tr>
<th>Type</th>
<th>Kind</th>
<th>Min/Max Values</th>
<th>Size</th>
<th>Exposed to BP</th>
</tr>
</thead>
<tbody>
<tr>
<td>int8/uint8</td>
<td>8 bit signed/unsigned integer</td>
<td>+/- 128 - 0 to 255</td>
<td>1 byte</td>
<td>false/true</td>
</tr>
<tr>
<td>int16/uint16</td>
<td>16 bit signed/unsigned integer</td>
<td>+/- 32,768 - 0 to 65,535</td>
<td>2 bytes</td>
<td>false/false</td>
</tr>
<tr>
<td>int32</td>
<td>32 bit signed integer</td>
<td>+/- 2,147,483,647</td>
<td>4 bytes</td>
<td>true</td>
</tr>
<tr>
<td>uint32</td>
<td>32 bit unsigned integer</td>
<td>&nbsp;0 to 4,294,967,295</td>
<td>4 bytes</td>
<td>false</td>
</tr>
<tr>
<td>int64</td>
<td>64 bit signed integer</td>
<td>+/- 9,223,372,036,854,775,807</td>
<td>8 bytes</td>
<td>true</td>
</tr>
<tr>
<td>uint64</td>
<td>64 bit unsigned integer</td>
<td>0 to 18,446,744,073,709,551,615</td>
<td>8 bytes</td>
<td>false</td>
</tr>
<tr>
<td>FName</td>
<td>sequence of chars</td>
<td>&infin;</td>
<td>12 bytes</td>
<td>true</td>
</tr>
<tr>
<td>FString</td>
<td>sequence of chars</td>
<td>&infin;</td>
<td>16 bytes</td>
<td>true</td>
</tr>
<tr>
<td>FText</td>
<td>sequence of chars</td>
<td>&infin;</td>
<td>24 bytes</td>
<td>true</td>
</tr>
</tbody>
</table>
</li>
</ul>
</li>
<li>Tick<br />
<ul>
<li>Disable tick on actors that don't need ticking.</li>
<li>Add <code>PrimaryActorTick.bCanEverTick = false;</code> to the constructor of the Actor class.</li>
<li>Tick is much more performance in C++ than in BP, but you still shouldn't tick actors that don't need ticking.</li>
</ul>
</li>
<li>UMG
<ul>
<li>Avoid using the bindings as they're essentially Tick with a pretty name. Instead, use delegates to update and maintain your UI.<br /><img src="https://files.trdwll.net/2021/04/ZDCEhw.png" alt="" width="104" height="92" /></li>
</ul>
</li>
<li>FVector_NetQuantize
<ul>
<li>Use these when you don't need a very precise Vector and if it's needing to be sent over the net - otherwise just use FVector.<br /><br />
<table>
<thead>
<tr>
<th>Type</th>
<th>Kind</th>
<th>Min/Max Values</th>
<th>Size / Net Size</th>
<th>Exposed to BP</th>
</tr>
</thead>
<tbody>
<tr>
<td>FVector_NetQuantizeNormal</td>
<td>Vector (x,y,z)</td>
<td>&nbsp;+/- 1</td>
<td>12 bytes / 2 bytes</td>
<td>true</td>
</tr>
<tr>
<td>FVector_NetQuantize</td>
<td>Vector (x,y,z) - 0 decimal place of precision.</td>
<td>+/- 1,048,576</td>
<td>12 bytes / 2.5 bytes</td>
<td>true</td>
</tr>
<tr>
<td>FVector_NetQuantize10</td>
<td>Vector (x,y,z) - 1 decimal place of precision.</td>
<td>+/- 1,677,721.6</td>
<td>12 bytes / 3 bytes</td>
<td>true</td>
</tr>
<tr>
<td>FVector_NetQuantize100</td>
<td>Vector (x,y,z) - 2 decimal place of precision.</td>
<td>+/- 10,737,418.24</td>
<td>12 bytes / 3.75 bytes</td>
<td>true</td>
</tr>
<tr>
<td>FVector</td>
<td>Vector (x,y,z) - 6 decimal place of precision</td>
<td>+/- 3.4E+38</td>
<td>12 bytes / 12 bytes</td>
<td>true</td>
</tr>
</tbody>
</table>
</li>
</ul>
</li>
<li>Structs
<ul>
<li>Instead of passing a ton of variables sometimes, it's better to package them into a struct to send over the net.</li>
</ul>
</li>
<li>DOREPLIFETIME_CONDITION
<ul>
<li>Set members replication condition as necessary.</li>
<li>Sometimes you don't have to replicate something, so always check if you actually have to.</li>
</ul>
</li>
<li>Overlap Events<br />
<ul>
<li>Disable these if you don't need them on an actor.</li>
<li>SetGenerateOverlapEvents</li>
</ul>
</li>
<li>When performing an RPC call in a method do checks before doing an RPC call to have an early out if certain conditions aren't met
<ul>
<li>
<pre class="language-cpp"><code>...
{
	if (x)
	{
		return;
	}

	if (!HasAuthority())
	{
		ServerRPC(...);
		return;
	}
}

instead of 

...
{
	if (!HasAuthority())
	{
		ServerRPC(...);
		return;
	}

	if (x)
	{
		return;
	}
}</code></pre>
</li>
</ul>
</li>
<li>???</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>until next time</p>
    