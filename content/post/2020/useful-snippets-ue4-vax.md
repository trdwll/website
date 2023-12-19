
+++
title = "Useful Snippets for UE4 using VAX"
description = "Setting up snippets for UE4 and VAX."
date = 2020-11-16T13:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>These require Visual Assist, but you might be able to set this up using the default stuff with Visual Studio.</p>
<p>&nbsp;</p>
<ol>
<li><strong>Extensions -&gt; VAssistX -&gt; Code Generation and Refactoring -&gt; Edit Refactoring Snippets...</strong></li>
<li><strong>Type: By Title</strong> then click the <img src="https://files.trdwll.net/2020/11/15/addsnippetvax.png" /> button.</li>
<li>Add the following options. Repeat the process for each of these.<br /><img src="https://files.trdwll.net/2020/11/15/ufcall.png" /><br />
<pre class="language-cpp"><code>Title: UFUNCTION Callable Macro
Shortcut: ufcall
UFUNCTION(BlueprintCallable, Category = "$PROJECT_NAME$|$ClassName$")

Title: UFUNCTION Const Callable Macro
Shortcut: ufcon
UFUNCTION(BlueprintCallable, BlueprintPure=false, Category = "$PROJECT_NAME$|$ClassName$")

Title: UFUNCTION Get Macro
Shortcut: ufget
UFUNCTION(BlueprintPure, Category = "$PROJECT_NAME$|$ClassName$")

Title: UPROPERTY BlueprintAssignable Macro
Shortcut: upass
UPROPERTY(BlueprintAssignable, Category = "$PROJECT_NAME$|$ClassName$", meta = (DisplayName = "$SymbolName$"))

Title: UPROPERTY BlueprintReadOnly Macro
Shortcut: upread
UPROPERTY(BlueprintReadOnly, Category = "$PROJECT_NAME$|$ClassName$", meta = (DisplayName = "$SymbolName$"))

Title: UPROPERTY EditAnywhere Macro
Shortcut: upedit
UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "$PROJECT_NAME$|$ClassName$", meta = (DisplayName = "$SymbolName$"))

Title: UPROPERTY EditDefaultsOnly Macro
Shortcut: updef
UPROPERTY(EditDefaultsOnly, Category = "$PROJECT_NAME$|$ClassName$", meta = (DisplayName = "$SymbolName$"))

Title: UPROPERTY Replicated Macro
Shortcut: uprep
UPROPERTY(Replicated)

Title: UENUM Macro
Shortcut: uenum
UENUM(BlueprintType)
enum class E$SymbolName$ : uint8
{
	None	 UMETA(DisplayName = "None"),
};

Title: USTRUCT Macro
Shortcut: ustruct
USTRUCT(BlueprintType)
struct F$SymbolName$
{
	GENERATED_BODY()
	
	F$SymbolName$() {}
}</code></pre>
</li>
<li>To use these you just type the shortcut in the editor and it should popup.</li>
</ol>
<p>&nbsp;</p>
<p>until next time</p>
    