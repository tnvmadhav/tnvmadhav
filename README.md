## My Latest Feed

<!-- feed starts -->
I noticed that the footnote cardinality indicators aren't readable and one can easily miss them while skimming the blog posts.

In the process, I learned that Hugo uses Goldmark markdown processor.


I also learned that Goldmark markdown processor [is CommonMark 0.31.2 compliant](https://michal.sapka.me/blog/2023/footnotes-in-hugo-and-goldmark/)[^1]


Then, I found a blog post from [geek this](https://geekthis.net/post/hugo-footnotes-and-citations/) that answered my question.


I finally followed the latter solution that involved adding a nascent/vanilla css code snippet at the root of my blog's HTML

> .footnote-ref::before {content: '[';}
> .footnote-ref::after {content: ']';}


[^1]: Only today I got to know about something called CommonMark that defines markdown specification.  You can refer to this RFC document that describes the protocol to convert markdown to html. https://spec.commonmark.org/0.31.2/.  -- 2024-08-03T12:30:12.658Z

---

Things I use LLMs for

— summarizing a piece of writing to add as metadata
— patching grammatical mistakes in my writing (no rewrites)
— generating function definitions with one specific job
— generating boilerplate and fixture tools for unit tests 
— formatting ugly json strings
— generating example SQL statements for a given DDL (when non-trivial types are involved)
— finding bugs in pieces of code that I seem to overlook, and learning what I had missed
— analysing time complexity of a piece of code (as reference to compare with my own analysis)

 -- 2024-08-03T11:15:59.321Z

---

Today, I came across one of my favorite bloggers' GitHub profile, [@Simonw](https://github.com/simonw). What caught my eye was the profile readme section, where Simon lists the latest posts from his blog.

###  Simon's GitHub Profile

This content section seemed automated, so I inspected the repository and found that it indeed was. What impressed me (and reaffirmed my respect) was that there was [a blog post](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/)[^1] linked to this creative expression, explaining how it was made.

It appeared that a significant portion of the content was hosted elsewhere (if not already on GitHub). All that was done was to compile everything neatly into one place.

### My Existing System

Coincidentally, I also have a feed of my own, both live (where content is hosted on my publishing platform) and RSS-based. This meant that I could set up a similar dynamically generated readme system to showcase my content on my GitHub profile.

So, I spent some time learning from Simon's implementation and setting up a similar workflow. 


The readme is generated as a cron task using a GitHub Actions Workflow. The key part is [a simple script, less than 100 lines of Python](https://github.com/tnvmadhav/tnvmadhav/blob/main/build_readme.py).

### My GitHub (New) Profile

[You can find my current feed on my GitHub profile](https://github.com/tnvmadhav).

It feels like an eye sore **but I want to sleep on it**.

The current design is very similar to Simon's (with some noticeable tweaks), but it's prone to changes with time and mood.

➡️ So now, every time I tweet / post on X via my Content Publisher System, if it's among the latest 10 posts (excluding replies and perhaps quotes), it's prone to be part of this new 'Latest Feed' on my GitHub profile.

This was fun.

### References

[^1]: https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/

Alternatively, you can read the HTML version on [my blog]( https://tnvmadhav.me/blog/dynamic-feed-on-my-github-profile/) -- 2024-08-03T08:51:57.604Z

---

It’s a beautiful day to thug it out with indomitable human spirit. -- 2024-08-02T06:30:07.436Z

---

After 12 years, Russ Cox is stepping down as Tech Lead of the Go project starting from 1st September 2024. Austin Clements is taking over.

> "I am not leaving the Go project, but I think the time is right for a change." -- rsc


> " In particular, I don’t believe that the “BDFL” (benevolent dictator for life) model is healthy for a person or a project." -- rsc


> "I will still be available to talk about Go designs, review CLs, answer obscure history questions, and generally help and support you all in whatever way I can. I will still file issues and send CLs from time to time, ...


> (contd)... I have been working on a few potential new standard libraries, I will still advocate for Go across the industry, and I will be speaking about Go at GoLab in Italy in November." -- rsc


Russ Cox will be focusing the efforts on Oscar (support for agent-like model baked with @gabybot). You can read more on Oscar [here](https://go.googlesource.com/oscar/+/refs/heads/master/README.md). 


Thank you, RSC 🫡🫡 for all the hard work on Go. It's an amazing piece of software.


You can find the note in the Go Dev google developer group ["passing torches to Austin and Cherry"](https://groups.google.com/g/golang-dev/c/0OqBkS2RzWw) -- 2024-08-02T03:30:17.236Z

---

So Telegram has a new in-app browser that is used to support applications built on top of the [Ton](https://ton.org) decentralized network that is designed by telegram https://telegram.org/blog/w3-browser-mini-app-store


A user on X posted [a neat diagram](https://x.com/ryoheikomy/status/1817139565926481935) that explains how these apps are accessed on the telegram layer while handling contracts on the TON network.


[The post was shared by Durov himself on X](https://x.com/durov/status/1818760336537010401)


I tried to check this out myself and it seems as though some apps already have more than a million users (hours after launch post on X).

 -- 2024-08-01T12:30:16.325Z

---

I must say [perplexity](https://perplexity.ai) is a delight to use. I usually find the answer I need in less than 2-3 prompts. I think of it as using a search engine and not an LLM. 

https://x.com/balajis/status/1818848829187539266


I think what keeps me coming back is not only the citation confidence but the 🤌🏻 UX.
 -- 2024-08-01T06:30:05.411Z

---

>  [...]the services I'm referring to are S3 Select, CloudSearch, Cloud9, SimpleDB, Forecast, Data Pipeline, and CodeCommit.- [Jeff Barr](https://x.com/jeffbarr/status/1818488419347317217 )


It looks like it's more than "just" these services. You can find a compiled list on a [GitHub repository called "AWS Breaking Changes and price increases"](https://github.com/SummitRoute/aws_breaking_changes)  -- 2024-08-01T03:56:33.098Z

---

+ 10000 Aura -- 2024-07-31T06:30:12.136Z

---

TIL that Caroline Ellison was one of the toppers in the International Linguistics Olympiad (ILO) 2011.

Wild.
https://twitter.com/twitter/status/1818477947277525242/ -- 2024-07-31T06:30:03.052Z
<!-- feed ends -->


---


<table><tr><td valign="top" width="33%">

## Latest Blog Posts

<!-- blog starts -->
[Dynamic Feed on My Github Profile](https://tnvmadhav.me/blog/dynamic-feed-on-my-github-profile/) -- 2024-08-03T08:16:05+00:00

[Custom R.S.S. Feed Format in Hugo](https://tnvmadhav.me/blog/custom-rss-feed-format-in-hugo/) -- 2024-07-28T10:49:57+00:00

[Jojo's Bizzare Adventure Season 5 Episode 28](https://tnvmadhav.me/blog/jojos-bizzare-adventure-season-5-episode-28/) -- 2024-07-12T16:29:41+00:00

['Leonardo Da Vinci' by Walter Isaacson](https://tnvmadhav.me/blog/leonardo-da-vinci-by-walter-isaacson/) -- 2024-05-26T10:43:05+00:00

[git angel](https://tnvmadhav.me/blog/good-git-practices/) -- 2024-02-12T04:17:37+00:00

More on [MY BLOG POSTS](https://tnvmadhav.me/blog/)
<!-- blog ends -->

</td><td valign="top" width="34%">

## Latest Guides

<!-- guide starts -->
[How to Perform Null Checks for Structs in Golang?](https://tnvmadhav.me/guides/how-to-perform-null-checks-for-structs-in-golang/) -- 2024-02-03T16:10:53+00:00

[How to Build a Simple Websocket Server and Client in Go and Javascript?](https://tnvmadhav.me/guides/how-to-build-a-simple-websocket-server-and-client-in-go/) -- 2023-12-16T14:14:18+00:00

[How to Use Buttons in SwiftUI?](https://tnvmadhav.me/guides/how-to-use-buttons-in-swiftui/) -- 2023-10-26T04:06:07+00:00

[How to go to a Line Number in Visual Studio Code?](https://tnvmadhav.me/guides/how-to-go-to-line-in-visual-studio-code/) -- 2023-09-24T09:55:27+00:00

[How to Copy to Clipboard in Neovim?](https://tnvmadhav.me/guides/how-to-copy-text-to-clipboard-neovim/) -- 2023-08-12T07:10:43+00:00

More on [MY GUIDES](https://tnvmadhav.me/guides/)
<!-- guide ends -->

</td><td valign="top" width="33%">

## Latest TILs

<!-- til starts -->
[Nested Functions in Go](https://tnvmadhav.me/til/nested-functions-in-go/) -- 2024-07-07T04:11:51+00:00

[Custom Pagination Html in Django](https://tnvmadhav.me/til/custom-pagination-html-in-django/) -- 2024-07-05T03:17:47+00:00

[Sort Slice of Composite Structures in Go](https://tnvmadhav.me/til/sort-slice-of-composite-structures-in-go/) -- 2024-06-15T05:35:13+00:00

[Slices Package in Golang](https://tnvmadhav.me/til/slices-package-in-golang/) -- 2024-06-14T03:18:00+00:00

[Find point of XSS Trigger in Javascript](https://tnvmadhav.me/til/find-source-of-xss-trigger-in-javascript/) -- 2024-06-13T16:52:43+00:00

More on [My TILS](https://tnvmadhav.me/til/)
<!-- til ends -->

</td></tr></table>


All credits of this idea to [Simon Willison](https://github.com/simonw/simonw/).