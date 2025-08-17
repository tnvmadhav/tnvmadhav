## My Latest Feed

<!-- feed starts -->
You can use github codespaces to bootstrap a piece of reproducible behaviour in a particular repository.

This is quite great for showcasing a piece of software. You can also run the software as if you're running it locally without actually running it locally.

This includes GitHub copilot and other plugins.

I was more curious about GitHub Codespaces in general so I asked Claude Sonnet 3.5 that was within my Github Codespace how it all worked:

> How It Works
>
>When you create a codespace, GitHub:
>Spins up a container using your devcontainer.json configuration
>Sets up the development environment with specified tools and extensions
>Clones your repository into the container
>Connects it to VS Code (web or desktop)

> "Code from anywhere with a browser"

Like for instance you can run, test and review code properly as you would from a pc/laptop.

> "No local setup needed"

While this is technically true, but in practice, one would have to be well-versed with setup commands to make effective use of GitHub workspaces. 
Not an issue for the initiated.

Another major concern I had while learning about Codespaces was would the data be lost if code changes weren't commited and pushed to remote source.

But looks like this concern was now relieved. The whole selling point of GitHub Codespaces was that a single codespace persists between sessions, meaning if you accidently close the tab "changes" can be restored.

However there are caveats!

If you're personal account codespace wasn't touched or used in last 30 days it will wipe the codespace clean.


While it's a bummer, most of the workflows may not be hindered because almost everyone has a personal computer with them at most times. Codespace would mainly be used as a convenience layer to work out of a low computer hardware like a phone or tablets like Ipads.

Me personally, I like to make small commits and push to remote if it's my personal projects. Also since this is remote, this is akin to having a VPS with OS and dependencies pre-installed for free to perform some cool experiments.

Moreover, it's perfect for code-reviews.

All changes can be tested on a remote server without worrying about affecting your local server persistence or compute states.

Run a test, write a spec, edit typos, "quick fixes" and many more.

At least all of this can now be done without carrying your laptops to that park or cafe, if you have your tablets or iPads at your disposal.

[Via Simon Willison's TIL post on Configuring GitHub Codespaces](https://til.simonwillison.net/github/codespaces-devcontainers)  -- 2025-08-17T06:43:00.083Z

---

If you can’t recreate workflows from memory, you still haven’t done it enough.

It’s crazy that this has to be made explicit. This is a note to self btw.


🔗 You can read my other content pieces:

https://twitter.com/twitter/status/1956966725578080277  -- 2025-08-17T06:41:16.243Z

---

On Using A.I. for actualy invention and discovery:

Most of the hype is about A.I. to eventually make more money, but the ultimate steelman has always been remove hurdles of group-think and instead generate unique ideas (with help of A.I.).

>A perspective that isn't yet getting enough attention: a way in which AI progress will soon deeply benefit the world is through the discovery and production of new technology.
>
>We measure human progress by technological revolutions; hard to internalize what it'd mean to have a computer which can do much of the work for breakthroughs.

[Quoting Greg Brockman via X](https://x.com/gdb/status/1956893646550356247)  -- 2025-08-17T06:30:02.969Z

---

real shopping 🛒  but in V.R. 🥽 

was this ever attempted? if not can it be attempted now? with A.I. helping with generating aisles in real-time.

like at @ikea  -- 2025-08-17T06:29:47.287Z

---

Killua going back and one-shotting the hunter exam during the greed island arc speaks volumes and is something I think about more often than not.  -- 2025-08-16T18:00:02.928Z

---

On the future of client-side A.I.

Traditional operating systems and client-side applications could be replaced so the compute can be saved for client side models instead.

> The phone/computer will just become an edge node for AI, directly rendering pixels with no real operating system or apps in the traditional sense. 
> There isn’t enough bandwidth to transmit video to all devices from the servers and there won’t always be good connectivity, so there still needs to be significant client-side AI compute.

[Quoting Elon Musk via X](https://x.com/elonmusk/status/1956583412203958733)  -- 2025-08-16T17:00:02.682Z

---

looking up your own guide from a few years ago to do something is *very* satisfying.  -- 2025-08-12T17:30:02.503Z

---

I'd like to believe that the intended purpose of multimodality is to invoke a cached catharsis if you will.  -- 2025-08-12T14:30:02.650Z

---

The internet runs because of a couple of goto statements in the lower levels of technological stack. -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/image_I4NFnyR.png) -- 2025-08-12T09:20:20.680Z

---

inefficiencies, inefficiencies everywhere -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/image_nKhy145.png) -- 2025-08-11T10:19:13.602Z
<!-- feed ends -->

NOTE: This feed is a sliding window. One can find [a significant portion of a feed archive on my website](https://tnvmadhav.me/feed/).

---


<table><tr><td valign="top" width="33%">

## Latest Blog Posts

<!-- blog starts -->
[Pieces of Media That I Often Have Thought About](https://tnvmadhav.me/blog/pieces-of-media-that-i-often-have-thought-about/) -- 2024-12-29T10:28:06+00:00

[White Screen of Death on my iPhone](https://tnvmadhav.me/blog/white-screen-of-death-on-my-iphone/) -- 2024-09-22T10:00:35+00:00

[Dynamic Feed on My Github Profile](https://tnvmadhav.me/blog/dynamic-feed-on-my-github-profile/) -- 2024-08-03T08:16:05+00:00

[Custom R.S.S. Feed Format in Hugo](https://tnvmadhav.me/blog/custom-rss-feed-format-in-hugo/) -- 2024-07-28T10:49:57+00:00

[Jojo's Bizzare Adventure Season 5 Episode 28](https://tnvmadhav.me/blog/jojos-bizzare-adventure-season-5-episode-28/) -- 2024-07-12T16:29:41+00:00

More on [MY BLOG POSTS](https://tnvmadhav.me/blog/)
<!-- blog ends -->

</td><td valign="top" width="34%">

## Latest Guides

<!-- guide starts -->
[Fzf for Code Review](https://tnvmadhav.me/guides/fzf-for-code-review/) -- 2025-06-22T10:52:58+00:00

[On Using Godoc tool for your Go Programs](https://tnvmadhav.me/guides/on-using-godoc-tool/) -- 2024-08-07T08:18:53+00:00

[How to Perform Null Checks for Structs in Golang?](https://tnvmadhav.me/guides/how-to-perform-null-checks-for-structs-in-golang/) -- 2024-02-03T16:10:53+00:00

[How to Build a Simple Websocket Server and Client in Go and Javascript?](https://tnvmadhav.me/guides/how-to-build-a-simple-websocket-server-and-client-in-go/) -- 2023-12-16T14:14:18+00:00

[How to Use Buttons in SwiftUI?](https://tnvmadhav.me/guides/how-to-use-buttons-in-swiftui/) -- 2023-10-26T04:06:07+00:00

More on [MY GUIDES](https://tnvmadhav.me/guides/)
<!-- guide ends -->

</td><td valign="top" width="33%">

## Latest TILs

<!-- til starts -->
[Rosetta 2: Apple's Temporary Fix](https://tnvmadhav.me/til/rosetta-2/) -- 2025-06-22T08:16:35+00:00

[Http Archiving -- Capturing a moment in time](https://tnvmadhav.me/til/http-archiving/) -- 2025-02-23T09:43:37+00:00

[V.S. Code Has a Simple Browser](https://tnvmadhav.me/til/vscode-has-a-simple-browser/) -- 2025-02-22T09:15:32+00:00

[About SSH Host Key Verification](https://tnvmadhav.me/til/ssh-host-key-verification/) -- 2024-09-12T15:11:31+00:00

[Network Address Types in Postgres](https://tnvmadhav.me/til/network-address-types-in-postgres/) -- 2024-09-10T04:03:27+00:00

More on [My TILS](https://tnvmadhav.me/til/)
<!-- til ends -->

</td></tr></table>


All credits of this idea to [Simon Willison](https://github.com/simonw/simonw/).