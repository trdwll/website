
+++
title = "Using const in C++"
description = "An easy to understand guide on using const in C++."
date = 2020-04-02T12:00:00Z
draft = false
type = 'post'
tags = ['TODO']
old_content_duration = 0
+++

<p>So what is const? Const means constant... Why should you use const? You should use const when you don't need to edit the value etc.</p>
<p>I'm by no means an expert, but if I made a typo feel free to reach out.</p>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">class Example
{
public:

    Example() {}

    // const on the end means you "promise" that the method won't edit any values in the class Example (can get around this by marking a variable mutable)
    int GetA() const { return m_A; }

    // If you're going to return a pointer you can add const before and after the * just like below (ugly)
    const int* const GetB() const { return m_B; }

private:
    int m_A;
    int* m_B;
};

int main()
{
    // const before a * means you can't modify the contents of the pointer
    // const after a * means you can't modify the pointer
    // const before and after adds both above

    int VALUE = 1337;

    int* a = new int(1);
    const int* b = new int(50);
    int* const c = new int(100);
    const int* const d = new int(8000);

    // You can also do int const* instead of const int* which means the same thing as they're before the *

	std::cout &lt;&lt; "A: " &lt;&lt; *a &lt;&lt; std::endl;
	std::cout &lt;&lt; "B: " &lt;&lt; *b &lt;&lt; std::endl;
	std::cout &lt;&lt; "C: " &lt;&lt; *c &lt;&lt; std::endl;
	std::cout &lt;&lt; "D: " &lt;&lt; *d &lt;&lt; std::endl;

    *a = 2; // We can set the value
    // *b = 10; // We can't set the value of b since const is before the *
    b = &amp;VALUE; // We can set the pointer
	*c = 25; // We can set the value
	// c = &amp;a; // We can't set the pointer to something else

    // We can't do anything to d as we specify const before and after the * (there are ways around stuff like this though)
    // *d = 80;
    // d = &amp;CONST_VALUE;

	std::cout &lt;&lt; "A: " &lt;&lt; *a &lt;&lt; std::endl;
	std::cout &lt;&lt; "B: " &lt;&lt; *b &lt;&lt; std::endl;
	std::cout &lt;&lt; "C: " &lt;&lt; *c &lt;&lt; std::endl;
	std::cout &lt;&lt; "D: " &lt;&lt; *d &lt;&lt; std::endl;

	std::cin.get();
}</code></pre>
</div>
<img style="height: 129px; width: 71px;" src="https://files.trdwll.net/2020/03/20/image-20200320225804-1.png" /></div>
<p>&nbsp;</p>
<p>Also, generally when passing a struct or a user-defined type you should pass by const reference like so unless you want to copy or even edit that value.</p>
<div>
<div tabindex="-1" contenteditable="false">
<pre data-widget="codeSnippet"><code class="language-cpp hljs">void TestMethod(const Example&amp; ex)
{

}</code></pre>
until next time</div>
</div>
    