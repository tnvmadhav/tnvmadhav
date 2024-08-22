## My Latest Feed

<!-- feed starts -->
While scrolling on X, I came across an intriguing and deep question from a profile I follow:

[**“Would you quit your job for $1M?”**](https://x.com/LiveDigitalArt/status/1826213407306944547)

A million dollars is life-changing money for 99% of the current human population. 

So, unless someone lives well beyond their means, they could realistically quit their job, even in certain places within first-world nations.

But what would a person do afterward?

Surely, everyone desires the freedom to pursue their own interests. 

Perhaps a person could completely change their life, start over, if you will. 

So what comes next? 

Now that you’re no longer forced to work on things out of necessity, you can do whatever you please.

This scenario is somewhat akin to a life where Universal Basic Income (UBI) is normalized and enforced.

So, what makes this question intriguing?

It’s about what comes after you break free of an obligation. 

You can understand a person by what they choose to do in their free time. 

I think this question can be extended or rephrased as:  **“What projects would you work on if money weren’t a problem?”**

Everyone wants to pursue their life’s work.

➡️ *Almost everyone’s answer to the original question would be “yes” but, answers for latter would truly be fun to read and think about.* -- 2024-08-22T06:30:03.072Z

---

We’re all NPCs until you look 🗿into the bathroom mirror at 3 AM
https://twitter.com/twitter/status/1825954366337200272/ -- 2024-08-21T12:57:48.389Z

---

### On Using Godoc tool for your Go Programs

[“Go takes documentation seriously”](https://go.dev/blog/godoc)[^1] 

The go official team have developed godoc — a useful documentation tool.
This tool parses the source code and formats docstrings and comments into a readable HTML format.
This HTML can be read by starting the documentation HTTP server locally.
One can use to navigate to function implementation from the documentation.

In this guide, I’ll show you how you can get started.

1. Install godoc binary
    `go install http://golang.org/x/tools/cmd/godoc`
2. If all goes good, the godoc binary should’ve been stored in the `$GOPATH/bin/`
3. Initialise the $GOPATH environment variable (if not set correctly already)
    `export GOPATH=$HOME/go`
4. Now you can go to the folder that you’re working on and run the following command
    `$GOPATH/bin/godoc -http=:6060`
5. HTTP server is now running, open `http://localhost:6060` and go through the source code documentation 😊

The guide to writing documentation for your Go programs can be found on [the official guide](https://go.dev/doc/comment)[^2].

### References:
[^1]: https://go.dev/blog/godoc
[^2]: https://go.dev/doc/comment
 -- 2024-08-17T14:04:46.680Z

---

In light of X (finally) increasing the character limit in their POST 2/tweet endpoint [^1], I've reciprocated on my publishing application.

This was verified on [my premium account](https://x.com/TnvMadhav/status/1824789749762077146).

[^1]: https://x.com/tapshah21/status/1823480895678165142 -- 2024-08-17T13:32:43.564Z

---

🥲 stumbled across an old (in this economy) branch of mine -- 2024-08-17T12:34:56.603Z

---

I recently went through a research paper publication on the CLBG method of calculating energy efficiency of various programming languages.

This is an insightful read.

This research was conducted on maximum of 27 programming languages to understand how time and memory correlated to energy efficiency. 

The results were compared with Rosetta's energy[^1] efficiency tier list.[^2]

I'd recommend software engineers to go through this white-paper especially those who deal with energy efficient ways to solve problems on embedded systems like watches or IoT systems. Choosing programming languages can help a ton here.

You can find the whole white paper [here](https://haslab.github.io/SAFER/scp21.pdf).

[^1]: https://rosettacode.org/wiki/Rosetta_Code
[^2]: https://github.com/greensoftwarelab/RosettaExamples -- 2024-08-10T09:38:35.607Z

---

While using Godoc I noticed that the `internal/` directory in my golang repository wasn't showing up. 

...


I searched around and learned that by 
default, the `internal/` directory is hidden.

[To make it visible in the godoc HTTP server you have to use the `?m=all` query parameter](https://stackoverflow.com/questions/67185294/cant-godoc-create-documentation-for-packages-within-internal-folder). -- 2024-08-07T15:30:05.312Z

---

TIL that by default, top level functions in Golang core are concurrent safe (i.e. they are okay to be invoked from multiple goroutines) unless stated otherwise.

🔗 [go.dev/doc/comment](https://go.dev/doc/comment)
 -- 2024-08-07T12:30:03.060Z

---

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
[Nested Functions in Go](https://tnvmadhav.me/til/nested-functions-in-go/) -- 2024-07-07T04:11:51+00:00

[Custom Pagination Html in Django](https://tnvmadhav.me/til/custom-pagination-html-in-django/) -- 2024-07-05T03:17:47+00:00

[Sort Slice of Composite Structures in Go](https://tnvmadhav.me/til/sort-slice-of-composite-structures-in-go/) -- 2024-06-15T05:35:13+00:00

[Slices Package in Golang](https://tnvmadhav.me/til/slices-package-in-golang/) -- 2024-06-14T03:18:00+00:00

[Find point of XSS Trigger in Javascript](https://tnvmadhav.me/til/find-source-of-xss-trigger-in-javascript/) -- 2024-06-13T16:52:43+00:00

More on [My TILS](https://tnvmadhav.me/til/)
<!-- til ends -->

</td></tr></table>


All credits of this idea to [Simon Willison](https://github.com/simonw/simonw/).