## My Latest Feed

<!-- feed starts -->
Moving slowly is much better than giving up. -- 2024-10-20T15:44:28.929Z

---

Notes from [Local First Software](https://martin.kleppmann.com/papers/local-first.pdf):

With the introduction and proliferation of "cloud-hosted" Software as a Service (SaaS), especially for consumer software, it becomes unclear who owns the data that flows through them.

Many times, the users who upload/generate data don't have complete control over what happens to them.

Moreover, the experience of using application software has become unnecessarily complex and painful.

> If you’re a software engineer, designer, product manager, or independent app developer working on production-ready software today, how can you help? 

The paper proposes an alternative concept called "Local First", a guide for software developers to support experiences w.r.t. speed, ownership of data, and quality of use.

Seven points to use as guideways for the uninitiated:

> 1. Make it Fast

Feedback has to be instant and non-blocking. Network calls (to servers or stores for example) affect this the most.

> 2. Multi-Device

As the name suggests, "local first" doesn't mean data and software should always be offline; rather, the "sync" if necessary, needs to be quiet, in the background, and non-blocking.

> 3. Offline Support

Not all software / client-side applications, need to interact with remote servers for all tasks.

Offline support means having a copy of all relevant resources available to work on without internet access.

> 4. Collaborative

When a large enough ecosystem supports local first development, there needs to be a system to support collision detection and resolution systems. 

This is highly relevant for Google, GitHub, etc.

> 5. Longevity

This is purely data-centric. Data needs to persist independently of the software that creates/processes it.

This means data should be importable/exportable into standard formats.

> 6. Privacy

Data that is private must be able to remain private. Local First Development supports this philosophy.

> 7. User Control

The user must be able to choose where the data is stored. The user should be able to have 100% ownership of the data. The user can choose to do whatever they want with it. -- 2024-10-19T08:34:42.678Z

---

Great timing.

I looked forward to the customizability of NotebookLM's, audio podcast generation (Solid Product!).

I can now customize and provide instructions on what to focus on when given a particularly technical document.

Thank you @Google and team!
https://twitter.com/twitter/status/1846946225251406039/


I can't wait to start implementing this today! -- 2024-10-18T03:38:04.022Z

---

TIL you can inspect a CLI command using the `type <cmd>` CLI command.

I usually use  `which <cmd>` to verify this but `type` provides a human-readable description/comment of the command.

Here's an example from my terminal:

```bash
$ type openai-env
openai-env is a shell function from /Users/<user>/.zshrc

$ which openai-env
openai-env () {
	export $(cat $PYTHON_PROJECT_PATH/.env)
}
```

I learned this from [Julia Evans' recent comic strip on PATH](https://wizardzines.com/comics/path-tips/ ) -- 2024-10-16T03:28:30.965Z

---

Excerpts from [Machines of Loving Grace](https://darioamodei.com/machines-of-loving-grace) by the CEO of [Anthropic](https://www.anthropic.com)

>  ..."I think their rate of discovery could be increased by 10x or more if there were a lot more talented, creative researchers. Or, put another way, I think the returns to intelligence are high for these discoveries, and that everything else in biology and medicine mostly follows from them."

Yes, it's mostly not (just) about doing what we already do... just faster. But, having enough brain juice (left) to be open to doing other things.

> "While that might sound crazy, the fact is that civilization has successfully navigated major economic shifts in the past: from hunter-gathering to farming, farming to feudalism, and feudalism to industrialism. I suspect that some new and stranger thing will be needed, and that it’s something no one today has done a good job of envisioning."

I try to believe that cost of executing and applying "solved problems" will go down eventually with machines taking over the replication part. 

It's then up to humans to pick up new challenges. This could be improving lifespan, brain capacity, low latency and efficient modes of communication, transport, energy efficiency, climate control/repair, food and water scarcity, etc.

To know about what lies beyond the horizon (which appears to be approaching quite rapidly), we must practice research ourselves, observe the work of researchers right now. What they think / dream about. 

Human creativity will have to be put to the test to find meaning on this [pale blue dot](https://en.wikipedia.org/wiki/Pale_Blue_Dot). -- 2024-10-13T12:30:03.176Z

---

I'm (obviously) not there yet but doing stuff like this makes you competent.

You're either doing it for fun/satisfaction/requirement (or) you're doing it to learn. 

Either way you'll gain enough skills to pick more ambitious projects.

https://twitter.com/twitter/status/1845186558414159875/ -- 2024-10-13T09:13:33.290Z

---

I'm reminded of [Kernighan's Law](https://github.com/dwmkerr/hacker-laws?tab=readme-ov-file#kernighans-law).

> Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it. ~ Brian Kernighan 

But here's the thing, if you stick to simple solutions, you'll not be prepared for inevitable scenarios where your debugging skills aren't up to the mark.

There is great risk in coming up with clever solutions but this actually pays off when you constantly push this boundary by debugging and finding faults in said clever solutions.
https://twitter.com/twitter/status/1845062132326449455/ -- 2024-10-12T12:30:03.243Z

---

Linus Torvalds on [working with GitHub Pull Requests](https://github.com/torvalds/linux/pull/17#issuecomment-5654674) -- 2024-10-04T06:30:03.070Z

---

TIL that the .me is country code based TLD (ccTLD) for Montenegro.

And that it's not some individualistic / personal branding thing that we could take as granted.


Reference:
[Wix](https://www.wix.com/encyclopedia/definition/me-domain)
[Perplexity](https://www.perplexity.ai/search/is-the-me-tld-associated-with-NyGlFbWATfGHTs0qM6ATPA) -- 2024-10-04T04:30:09.183Z

---

When I checked simon's openai-dev-day live text stream, I noticed something different (than the usual posts). The structure of the blog post itself.

Luckily, we've a [nice and detailed write up](https://til.simonwillison.net/django/live-blog) on how it was implemented  (using LLM help) in a very short span of time.

If you missed the live blog, you can check it out [here](https://simonwillison.net/2024/Oct/1/openai-devday-2024-live-blog/)


And, this changes are [available on GitHub](https://github.com/simonw/simonwillisonblog/commits/910d2c3be68de7198c76dd25d75662a81c4d76e2/) -- 2024-10-03T05:00:05.329Z
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