
+++
title = "Using Interfaces in UE4"
description = "A short guide on using Interfaces."
date = 2020-03-05T07:24:56Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>Interfaces are an amazing thing that's in programming. An interface describes the behavior or capabilities of a C++ class without committing to a particular implementation of that class. Meaning any class that extends an interface has to implement the methods of that interface. You can also add more than 1 interface to a class and an abstract class you can't. More on this later. The simplest way to explain what an interface is would be it's a class with no implementation.</p>
<p>&nbsp;</p>
<h3>Why?</h3>
<p>Say you have an interaction system and you want to only interact with specific actors in your level. You can achieve this in a ton of different ways, but generally, they're messy and a nightmare to maintain (with the exception of having an abstract class such as BaseItem and then Apple is derived from BaseItem). With interfaces, you can set specific information (not variables, but methods such as Interact or Consume or even Drop) on a class (which would force Apple to implement Interact, Consume, and Drop and the same with Banana, etc) or even you can use an interface to be an identifier (for example when using <code>object-&gt;GetClass()-&gt;ImplementsInterface(MYINTERFACE)</code>).</p>
<p>&nbsp;</p>
<h3>When?</h3>
<p>So if you're wanting 2 actors to have the same properties such as Health and a Name then you should probably use an abstract class. If you're wanting to interact with both of those actors then create an interface to handle that. You can use an abstract class (or rather a base class - it holds all of the common variables for your child classes) and then have the interface for interaction.</p>
<p>If you just want to interact with an actor and have no data for that actor then just create an interface so you can interact with it.</p>
<p>&nbsp;</p>
<h3>How?</h3>
<p>Ok, cool so now that you understand. Let's get to it. Because I mainly write C++ over BP I'm going to start this guide with C++. If you just want to download the project and learn on your own then feel free to <a href="https://files.trdwll.net/2020/03/02/interfaceexample.zip">here</a>.</p>
<p><strong>This is the C++ way. If you're wanting to just do interfaces in BP then scroll down more. :)</strong></p>
<ol>
<li><strong>Right-click in your Content browser -&gt; New C++ Class</strong> or <strong>File -&gt; New C++ Class</strong> (scroll to the bottom and choose <em>Unreal Interface</em>) Click <strong>Next</strong>.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302074949-3.png" target="_blank" rel="noopener"><img style="height: 363px; width: 600px;" src="https://files.trdwll.net/2020/03/02/image-20200302074949-3.png" /></a></li>
<li>Type in your Interface name and path then click <strong>Create Class</strong><br /><a href="https://files.trdwll.net/2020/03/02/image-20200302075126-4.png" target="_blank" rel="noopener"><img style="height: 363px; width: 600px;" src="https://files.trdwll.net/2020/03/02/image-20200302075126-4.png" /></a></li>
<li>The same way above, create an <strong>actor class</strong> and name it whatever. I've named mine <strong>InteractableActor</strong>.</li>
<li>Go to <strong>Edit -&gt; Project Settings</strong> then <strong>Engine -&gt; Input</strong>, now add a new <strong>Action Mapping</strong>.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302093543-3.png" target="_blank" rel="noopener"><img style="height: 213px; width: 497px;" src="https://files.trdwll.net/2020/03/02/image-20200302093543-3.png" /></a></li>
<li>Cool, now you're done. Next guide! Just kidding, now you should open Visual Studio or whatever IDE you're using if you haven't already.</li>
<li>Go into your Character class and add the following code.
<div>
<pre><code class="language-cpp">// H
private:
	/** Get the actor in the characters view */
	UFUNCTION(BlueprintCallable)
	class AActor* GetActorInView();

	/** The distance that a character can interact with an actor. */
	float m_MaxUseDistance = 250.0f;
public:

	/** Interact with the item that the character is looking at. */
	UFUNCTION(BlueprintCallable)
	void Interact();

	/** Consume the item that the character is looking at. */
	UFUNCTION(BlueprintCallable)
	void Consume();

// CPP

void AYOURCharacter::Interact()
{
	if (AActor* const actor = GetActorInView())
	{
		// If the actor that you're looking at implements the interface InteractInterface
		if (actor-&gt;GetClass()-&gt;ImplementsInterface(UInteractInterface::StaticClass()))
		{
			IInteractInterface::Execute_Interact(actor);
		}
	}
}

void AYOURCharacter::Consume()
{
	if (AActor* const actor = GetActorInView())
	{
		// If the actor that you're looking at implements the interface InteractInterface
		if (actor-&gt;GetClass()-&gt;ImplementsInterface(UInteractInterface::StaticClass()))
		{
			IInteractInterface::Execute_Consume(actor);
		}
	}
}

class AActor* AYOURCharacter::GetActorInView()
{
	ACharacter* const Character = Cast&lt;ACharacter&gt;(this);

	// If the character or the controller for the character are null then return a nullptr instead of running the rest of the method
	if (Character == nullptr || Character-&gt;GetController() == nullptr)
	{
		return nullptr;
	}

	// Get the players view point (what they're looking at)
	FVector CameraLocation;
	FRotator CameraRotation;
	Character-&gt;GetController()-&gt;GetPlayerViewPoint(CameraLocation, CameraRotation);

	// Calculate the end location for the line trace
	FVector EndLocation = CameraLocation + (CameraRotation.Vector() * m_MaxUseDistance);

	FCollisionQueryParams TraceParams(FName(TEXT("")), true, this);
	TraceParams.bTraceComplex = true;

	// Perform the line trace
	FHitResult HitRes;
	GetWorld()-&gt;LineTraceSingleByChannel(HitRes, CameraLocation, EndLocation, ECC_GameTraceChannel18, TraceParams);

	return Cast&lt;AActor&gt;(HitRes.Actor);
}</code></pre>
</div>
</li>
<li>
<p>Add the following to the <strong>SetupPlayerInputComponent. </strong></p>
<div>
<pre><code class="language-cpp">// Bind interaction event
	PlayerInputComponent-&gt;BindAction("Interact", IE_Pressed, this, &amp;AYOURCharacter::Interact);
	PlayerInputComponent-&gt;BindAction("Consume", IE_Pressed, this, &amp;AYOURCharacter::Consume);</code></pre>
</div>
</li>
<li>Head over to your Interface class and make it look like mine.
<pre><code class="language-cpp">// This class does not need to be modified.
UINTERFACE(MinimalAPI, BlueprintType)
class UInteractInterface : public UInterface
{
	GENERATED_BODY()
};

/**
 * This is where you actually create your methods
 */
class YOURPROJECT_API IInteractInterface
{
	GENERATED_BODY()

public:
	// You can even use BlueprintImplementableEvent instead of BlueprintNativeEvent
	// We're using BlueprintNativeEvent so we can implement the methods in C++

	// Our interact method for actors
	UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "InteractInterface")
	void Interact();

	// Our consume method for actors
	UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category = "InteractInterface")
	void Consume();
};</code></pre>
<p>Basically, you just want to add your methods to the second class in the file.</p>
</li>
<li>Now in your <strong>InteractableActor</strong> class add the following. At the top where it says <code>public Actor</code> you need to change it to <code>public Actor, public IInteractInterface</code>. This implements the interface InteractInterface so you can use its methods. You're also going to have to include the interface's header file at the top of your class.
<pre><code class="language-cpp">// H
UCLASS()
class YOURPROJECT_API AInteractableActor : public AActor, public IInteractInterface // Inherit the interface - you can do this in BP if you'd like to
{
	GENERATED_BODY()

public:
	// MAKE SURE YOU ADD _Implementation TO THE METHOD NAMES!

	// Implement the Consume method from our interface
	virtual void Consume_Implementation() override;

	// Implement the Interact method from our interface
	virtual void Interact_Implementation() override;
};

// CPP
void AInteractableActor::Consume_Implementation()
{
	if (GEngine)
	{
		GEngine-&gt;AddOnScreenDebugMessage(-1, 3.0f, FColor::Orange, "(C++) *gulp* That was a good actor! I'm completely full now. :)");
	}
}

void AInteractableActor::Interact_Implementation()
{
	if (GEngine)
	{
		GEngine-&gt;AddOnScreenDebugMessage(-1, 3.0f, FColor::Orange, "(C++) You've interacted with the actor!");
	}
}</code></pre>
<p>Cool, now you're pretty much done. Go into the editor and create a BP derived of <strong>InteractableActor</strong> and place it into the world. (make sure you add a mesh to the actor so you can see it) If you want to override the C++ implementation in BP you certainly can. Just right click and <strong>Implement Function</strong> and it'll create the node for you.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302092533-1.png" target="_blank" rel="noopener"><img style="height: 135px; width: 318px;" src="https://files.trdwll.net/2020/03/02/image-20200302092533-1.png" /></a><a href="https://files.trdwll.net/2020/03/02/image-20200302092551-2.png" target="_blank" rel="noopener"><img style="height: 104px; width: 215px;" src="https://files.trdwll.net/2020/03/02/image-20200302092551-2.png" /></a></p>
</li>
</ol>
<p>&nbsp;</p>
<p><strong>This is the BP way. If you're wanting to just do interfaces in C++ then scroll up, you passed it. :)</strong></p>
<ol>
<li><strong>Right-click in your Content browser -&gt; Blueprints -&gt; Blueprint Interface</strong>. I named mine <strong>BP_Interface_Interact</strong>.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302093741-4.png" target="_blank" rel="noopener"><img style="height: 513px; width: 300px;" src="https://files.trdwll.net/2020/03/02/image-20200302093741-4.png" /></a></li>
<li>Open your new BP interface and rename the function to <strong>Drop</strong>.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302093951-5.png" target="_blank" rel="noopener"><img style="height: 76px; width: 121px;" src="https://files.trdwll.net/2020/03/02/image-20200302093951-5.png" /></a></li>
<li>Create a new Actor BP and click <strong>Class Settings</strong>.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302094101-6.png" target="_blank" rel="noopener"><img style="height: 67px; width: 99px;" src="https://files.trdwll.net/2020/03/02/image-20200302094101-6.png" /></a></li>
<li>Add the interface that you just created.&nbsp;<br /><a href="https://files.trdwll.net/2020/03/02/interface_search.png" target="_blank" rel="noopener"><img style="height: 151px; width: 368px;" src="https://files.trdwll.net/2020/03/02/interface_search.png" /></a><br /><a href="https://files.trdwll.net/2020/03/02/image-20200302094436-7.png" target="_blank" rel="noopener"><img style="height: 70px; width: 362px;" src="https://files.trdwll.net/2020/03/02/image-20200302094436-7.png" /></a></li>
<li>Right-click and <strong>Implement Function</strong>.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302094646-8.png" target="_blank" rel="noopener"><img style="height: 90px; width: 285px;" src="https://files.trdwll.net/2020/03/02/image-20200302094646-8.png" /></a><br /><a href="https://files.trdwll.net/2020/03/02/image-20200302100203-10.png" target="_blank" rel="noopener"><img style="height: 235px; width: 1321px;" src="https://files.trdwll.net/2020/03/02/image-20200302100203-10.png" /></a></li>
<li>Go into your Character class and add the following.<br /><a href="https://files.trdwll.net/2020/03/02/image-20200302100119-9.png" target="_blank" rel="noopener"><img style="height: 169px; width: 815px;" src="https://files.trdwll.net/2020/03/02/image-20200302100119-9.png" /></a></li>
<li>The last thing to do is to add the actor to the level.</li>
</ol>
<p>&nbsp;</p>
<p>until next time</p>
<p>&nbsp;</p>
    