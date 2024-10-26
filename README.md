## My Latest Feed

<!-- feed starts -->
TIL about the cookiecutter PyPi package

It's a quick way to scaffold new python packages, plugins, django projects and [many more](https://cookiecutter.readthedocs.io/en/stable/README.html#special-templates ) from pre-built templates.

Using jinja2 template syntax, one can create an entire cookiecutter project template for use and reuse.

A comprehensive documentation can be found [on the internet](https://cookiecutter.readthedocs.io/en/stable/README.html#cookiecutter ). -- 2024-10-26T13:30:03.046Z

---

AI is (unsurprisingly) good at converting technical notes into Anki Flashcards.

For the uninitiated, it would've taken several minutes to construct questions and answers after taking hours worth of notes but with a relatively small LLM like GPT-4o-mini, one could churn out Q&A list in seconds.

I believe certain unnecessary hurdles of the theoretical learning process is eliminated.


And yes, all one needs now is to be able to actually import said compilation onto Anki in bulk. And most importantly, eat the damn frog!


It seems like AnkiWeb doesn't support export or imports.


I've installed Anki Desktop app so I could bulk import new flashcards.

I've generated [a simple python script to process a text file using GPT-4 (customize prompts) and output a anki importable .txt file.](https://gist.github.com/tnvmadhav/8bc0070b65b263034815127f9974677e)


The process of taking a note file and generating flashcards is now streamlined.

I could setup a local cron job to run everyday, that processes the notes from my local notes directory for the day and generate anki flashcards with the learnings.

I could configure a LaunchAgent or Daemon perhaps using .plist configuration.

 -- 2024-10-26T13:14:16.350Z

---

If you don’t know how something impacts the world around you, you don’t fully understand.
https://twitter.com/twitter/status/1849773180136599989/ -- 2024-10-26T06:30:03.189Z

---

TIL that ICE TSUNAMIS are a thing!

https://en.wikipedia.org/wiki/Ice_shove
https://twitter.com/twitter/status/1849163888895599031/ -- 2024-10-24T12:07:14.479Z

---

To the builders of the future, you need to relive the pain that the thing has genuinely relieved. -- 2024-10-24T06:30:02.956Z

---

Excerpts from ["Desperation Induced Focus"](https://www.rkg.blog/desperation-induced-focus.php )

> "Most big companies aren’t focused on creating things out of nothing. Someone else made the magic money-making machine, and they assume that it will just keep working."
>
> "This lack of focus is a luxury and a disease."

This is called peace time thinking. Thoughts generated out of seemingly derived notions or non-axioms. Sometimes too much trust in the system.

> My advice to people when they are thinking about instituting a new process is to go to a whiteboard and write down the answer to this question: “If you could only get one thing done this year, what would it be?”. 

>  Desperation inspires creativity and intense focus. It is an essential ingredient to building great products and services.

> So, the next time you feel desperate, lean in. Embrace it. Use it as the fuel to create the next founding moment4 for your company.

> And the next time someone tries to tell you to do something because a big company does it, be suspicious.

One must arrive at something from first principles and not because someone told them (a.k.a. by proxy). Keep the advice in mind and use it as a reminder but never an axiom.

To the builders of the future, you need to relive the pain that it has genuinely relieved. -- 2024-10-23T17:30:03.050Z

---

I'd stumbled upon a rather brilliant @leetcode editorial piece and a useful mind map on solving problems. 

This something that a younger version of me would've appreciated especially when starting out.

I've shared some notes and excerpts on my [blog](https://tnvmadhav.me/feed/2024/10/21/ ) -- 2024-10-22T03:37:31.352Z

---

Ownership is important. Start your own blog!
https://twitter.com/twitter/status/1848261668024807887/ -- 2024-10-21T12:30:03.083Z

---

Notes from [leetcode's editorial section](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/editorial/
) on solving data structures and algorithm problems in general.

After solving a leetcode problem, found myself checking out an editorial section to see what other approaches I could've missed. What I found was unexpected.

A guide to identifying patterns and choosing approaches. This is something I could've used when I was a couple of years younger just starting out.

> So this time before diving into the answer, let’s understand a few general patterns that you can use in your future journey:
>
> Sorted Input:
>
> Apply binary search for efficient element lookup.
> Use the two-pointer technique for problems involving pairs or segments.
> Unsorted Input:
>
> Apply dynamic programming for questions related to counting ways or optimizing values.
> Use backtracking for problems that ask for all possibilities or combinations (this is also a suitable fallback if dynamic programming isn’t going to work).
> Use a Trie for prefix matching and string-building scenarios.
> Use a hash map or set to find specific elements quickly.
> Implement a monotonic stack or sliding window technique for managing elements while continuously finding maximum or minimum values.
> Input is a Graph or Tree:

> Use DFS to explore all paths or when the question does not require finding the shortest path.
> Use BFS when the question asks for the shortest path or fewest steps.
> For binary trees, use DFS if the problem involves exploring specific depths or levels.
> Linked List Input:

> Use techniques involving slow and fast pointers or "prev" and "dummy" pointers to facilitate certain operations if you are unsure how to achieve a specific outcome.

> Note: There's so much more to this pattern! We just wanted to give you a glimpse of what pattern recognition boils down to in its simplest form. Feel free to add your own flair and create a detailed chart!

Here's [a useful mindmap of techniques to use](https://assets.leetcode.com/static_assets/media/original_images/1593/1593_mintotal.png) per problem type -- 2024-10-21T03:50:20.239Z

---

This takes the general concept of "put your money where your mouth is" and zooms out a bit IMO.

Reframe as "if your mouth isn't where your money is, where is it?"
https://twitter.com/twitter/status/1848025357061926957/ -- 2024-10-20T22:00:02.964Z
<!-- feed ends -->


---


<table><tr><td valign="top" width="33%">

## Latest Blog Posts

<!-- blog starts -->


More on [MY BLOG POSTS](https://tnvmadhav.me/blog/)
<!-- blog ends -->

</td><td valign="top" width="34%">

## Latest Guides

<!-- guide starts -->


More on [MY GUIDES](https://tnvmadhav.me/guides/)
<!-- guide ends -->

</td><td valign="top" width="33%">

## Latest TILs

<!-- til starts -->


More on [My TILS](https://tnvmadhav.me/til/)
<!-- til ends -->

</td></tr></table>


All credits of this idea to [Simon Willison](https://github.com/simonw/simonw/).