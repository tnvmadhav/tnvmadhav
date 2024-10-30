## My Latest Feed

<!-- feed starts -->
TIL we can prevent bash script from prematurely exiting using `set +e`.

```bash
set +e
<some command>
set -e
```

This knowledge is useful if you want to run certain scripts and perform custom actions on the resultant exit code without losing information due to premature exits.

[From bash reference manual](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) -- 2024-10-30T12:43:30.749Z

---

[1] [Open Source AI Definition as per Open Source Initiative](https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition)

> The OSAID offers a standard by which community-led, open and public evaluations will be conducted to validate whether or not an AI system can be deemed Open Source AI.

> "The new definition requires Open Source models to provide enough information about their training data so that a ‘skilled person can recreate a substantially equivalent system using the same or similar data,’ which goes further than what many proprietary or ostensibly Open Source models do today,” said Ayah Bdeir, who leads AI strategy at Mozilla"

[2] [Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)

1. Free to use without permission
2. Study the components to learn how it works
3. Modify for use to change the output
4. Share with other with or without modification

> These freedoms apply both to a fully functional system and to discrete elements of a system. A precondition to exercising these freedoms is to have access to the preferred form to make modifications to the system.

This involves data, code and weights. -- 2024-10-29T06:30:05.879Z

---

This is a dumbed down (simple) take.

A.I. is to “building” as what client side javascript is to HTML.

Elimination of extra time and effort to gain a certain outcome.
https://twitter.com/twitter/status/1850940029155373382/ -- 2024-10-29T06:30:03.058Z

---

I was able to convert, and load some of my computer science related notes in .txt files like HTTP and Redis onto Anki in seconds.

I was able to revise in matter of minutes!

Thank you @openai :)


One can find [this script useful](https://gist.github.com/tnvmadhav/8bc0070b65b263034815127f9974677e) if you wanna automate Anki flashcard generation with Python and ChatGPT.
https://twitter.com/twitter/status/1850163990296433051/ -- 2024-10-27T06:30:17.002Z

---

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
<!-- feed ends -->


---


<table><tr><td valign="top" width="33%">

## Latest Blog Posts

<!-- blog starts -->
[White Screen of Death on my iPhone](https://tnvmadhav.me/blog/white-screen-of-death-on-my-iphone/) -- 2024-09-22T10:00:35+00:00

[Dynamic Feed on My Github Profile](https://tnvmadhav.me/blog/dynamic-feed-on-my-github-profile/) -- 2024-08-03T08:16:05+00:00

[Custom R.S.S. Feed Format in Hugo](https://tnvmadhav.me/blog/custom-rss-feed-format-in-hugo/) -- 2024-07-28T10:49:57+00:00

[Jojo's Bizzare Adventure Season 5 Episode 28](https://tnvmadhav.me/blog/jojos-bizzare-adventure-season-5-episode-28/) -- 2024-07-12T16:29:41+00:00

['Leonardo Da Vinci' by Walter Isaacson](https://tnvmadhav.me/blog/leonardo-da-vinci-by-walter-isaacson/) -- 2024-05-26T10:43:05+00:00

More on [MY BLOG POSTS](https://tnvmadhav.me/blog/)
<!-- blog ends -->

</td><td valign="top" width="34%">

## Latest Guides

<!-- guide starts -->
[On Using Godoc tool for your Go Programs](https://tnvmadhav.me/guides/on-using-godoc-tool/) -- 2024-08-07T08:18:53+00:00

[How to Perform Null Checks for Structs in Golang?](https://tnvmadhav.me/guides/how-to-perform-null-checks-for-structs-in-golang/) -- 2024-02-03T16:10:53+00:00

[How to Build a Simple Websocket Server and Client in Go and Javascript?](https://tnvmadhav.me/guides/how-to-build-a-simple-websocket-server-and-client-in-go/) -- 2023-12-16T14:14:18+00:00

[How to Use Buttons in SwiftUI?](https://tnvmadhav.me/guides/how-to-use-buttons-in-swiftui/) -- 2023-10-26T04:06:07+00:00

[How to go to a Line Number in Visual Studio Code?](https://tnvmadhav.me/guides/how-to-go-to-line-in-visual-studio-code/) -- 2023-09-24T09:55:27+00:00

More on [MY GUIDES](https://tnvmadhav.me/guides/)
<!-- guide ends -->

</td><td valign="top" width="33%">

## Latest TILs

<!-- til starts -->
[About SSH Host Key Verification](https://tnvmadhav.me/til/ssh-host-key-verification/) -- 2024-09-12T15:11:31+00:00

[Network Address Types in Postgres](https://tnvmadhav.me/til/network-address-types-in-postgres/) -- 2024-09-10T04:03:27+00:00

[Nested Functions in Go](https://tnvmadhav.me/til/nested-functions-in-go/) -- 2024-07-07T04:11:51+00:00

[Custom Pagination Html in Django](https://tnvmadhav.me/til/custom-pagination-html-in-django/) -- 2024-07-05T03:17:47+00:00

[Sort Slice of Composite Structures in Go](https://tnvmadhav.me/til/sort-slice-of-composite-structures-in-go/) -- 2024-06-15T05:35:13+00:00

More on [My TILS](https://tnvmadhav.me/til/)
<!-- til ends -->

</td></tr></table>


All credits of this idea to [Simon Willison](https://github.com/simonw/simonw/).