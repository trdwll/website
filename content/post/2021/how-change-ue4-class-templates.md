
+++
title = "How To Change UE4 Class Templates"
description = "I'm going to show you something cool."
date = 2021-02-10T08:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>So have you created a C++ class in UE4 and it creates the class like this? Do you just hate the extra comments or spacing that the template has? Same. 🙁</p>
<pre class="language-cpp"><code>// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "MyActor.generated.h"

UCLASS()
class THINGGAME_API AMyActor : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AMyActor();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
</code></pre>
<p>Well don't worry, you're in the right place to get it looking better.</p>
<p>Head over to your engine install and edit the appropriate file in <code>D:\Program Files\Epic Games\UE_4.26\Engine\Content\Editor</code>. I only edited Actor, ActorComponent, Character, Interface, and Pawn. Unfortunately, you can't do this for classes like PlayerState or GameMode as they're hardcoded in the <code>GameProjectUtils.cpp(496)</code>. So instead you can just edit the <code>UObjectClass.h.template</code> and <code>UObjectClass.cpp.template</code> files. I wish the generation method was via file name instead of actual class type so we could just make a file called <code>PlayerStateClass.h.template</code> and <code>PlayerStateClass.cpp.template</code> and then it just generates the PlayerState based on it. 🤷&zwj;♂️</p>
<p>My result is this.</p>
<pre class="language-cpp"><code>// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"

#include "MyActor.generated.h"

/**
 *
 */
UCLASS()
class THINGGAME_API AMyActor : public AActor
{
	GENERATED_BODY()

public:
	AMyActor();

protected:
	virtual void BeginPlay() override;
	virtual void Tick(float DeltaTime) override;

	virtual void GetLifetimeReplicatedProps(TArray&lt;FLifetimeProperty&gt;&amp; OutLifetimeProps) const override;

private:
};</code></pre>
<p>&nbsp;</p>
<p>Download my template files <a href="https://files.trdwll.net/2021/02/UE4ClassTemplates.zip" target="_blank" rel="noopener">here</a>.</p>
<p>&nbsp;</p>
<p>until next time</p>
    