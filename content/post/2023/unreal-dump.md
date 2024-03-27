
+++
title = "Unreal Dump"
description = "Things that I find out about Unreal Engine that are cool."
date = 2023-04-20T10:22:28Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<ul>

<li><a href="https://docs.unrealengine.com/5.1/en-US/API/Runtime/Core/Misc/TEnumRange/" target="_blank" rel="noopener">TEnumRange</a> <br />

<ul>

<li>see <code>\Runtime\Core\Public\Misc\EnumRange.h</code>.</li>

<li><code>for (const EMyEnum Val : TEnumRange&lt;EMyEnum&gt;())</code></li>

<li>Required to use <code>ENUM_RANGE_BY_COUNT</code>, <code>ENUM_RANGE_BY_FIRST_AND_LAST</code>, or <code>ENUM_RANGE_BY_VALUES</code></li>

</ul>

</li>

<li>BlueprintAuthorityOnly, tbh some of <a href="https://docs.unrealengine.com/5.1/en-US/ProgrammingAndScripting/GameplayArchitecture/Functions/Specifiers/" target="_blank" rel="noopener">these</a> TIL.

<ul>

<li><code>UFUNCTION(BlueprintCallable, BlueprintAuthorityOnly, Category = "MyCategory")</code></li>

</ul>

</li>

<li>EditCondition, VisibleCondition, and EditConditionHides

<ul>

<li><code>UPROPERTY(..., meta = (EditCondition="bToggled"))</code> or <code>UPROPERTY(..., meta = (EditCondition="MyEnum == MyEnum::None"))</code> etc</li>

</ul>

</li>

<li>FSimpleMulticastDelegate and FSimpleDelegate

<ul>

<li>These are delegates that you can bind only in C++ and don't support any args. If using these you don't have to do the macro to define them as they're already defined so it helps clean up your classes.</li>

</ul>

</li>

<li>TArrayView

<ul>

<li>You can do some cool stuff with this class, such as splitting an array.</li>

</ul>

</li>

<li>FDateRange, FDoubleRange, FFloatRange, FInt8Range, FInt16Range, FInt32Range, FInt64Range -

<ul>

<li>see <code>\Runtime\Core\Public\Math\Range.h</code></li>

</ul>

</li>

<li><a href="https://docs.unrealengine.com/5.1/en-US/API/Runtime/Engine/GameFramework/APlayerState/CopyProperties/" target="_blank" rel="noopener">APlayerState::CopyProperties</a> and <a href="https://docs.unrealengine.com/5.1/en-US/API/Runtime/Engine/GameFramework/APlayerState/OverrideWith/" target="_blank" rel="noopener">APlayerState::OverrideWith</a></li>

<li>FWorldDelegates&nbsp;</li>

<li>UE_NONCOPYABLE macro</li>

<li>FFormatNamedArguments</li>

<li>UE_ARRAY_COUNT</li>

<li>ThisClass - used when well... using delegates etc &amp;ThisClass::MethodName</li>

<li>UEnum class - has some really useful methods</li>

<li>PawnLeavingGame - override this in your PlayerController class and it will prevent your pawn from being destroyed on disconnect</li>

<li>FDebug::DumpStackTraceToLog to dump the callstack to the log</li>

<li>ObjectInitializer.DoNotCreateDefaultSubobject</li>

<li>NotifyControllerChanged on the Pawn</li>

<li>#include UE_INLINE_GENERATED_CPP_BY_NAME(ClassFileName) in cpp files</li>
<li>ULineBatchComponent - useful for drawing debug (DrawDebug*)</li>
<li>UE_DISABLE_OPTIMIZATION & UE_ENABLE_OPTIMIZATION</li>
<li>FMessageLog("MapCheck").*</li>
<li>[/Script/EngineSettings.GameMapsSettings] - EditorTemplateMapOverrides</li>
</ul>

<p>&nbsp;</p>

<p>until next time</p>
    
