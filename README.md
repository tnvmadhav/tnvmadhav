## My Latest Feed

<!-- feed starts -->
I bought myself a copy of book on mobile engineering.

Building Mobile Apps at Scale! by Gergely Orosz. -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/image_s10vFSm.png) -- 2026-10-04T11:38:53.506Z

---

First things first, I would like to open a file or folder in xcode, I need to do the following:

```sh
open -a xcode <file/folder>
```

Now, that's out of the way, I need to figure out what the hell xcode does on top of your existing project...

I see that a folder contains a `.xcodeproj` file? folder?.

I always get confused with that is or why is it ever required.

If we open it using vs code, it turns out that it's a folder.

```sh
open -a Visual\ Studio\ Code <some>.xcodeproj
```

So, an xcodeproj folder is context managing folder for your xcode.

if you don't use xcode to build and distribute your apps, then this is entirely not necessary.

All of my personal iOS and macOS apps I have built in the past have been done so using Xcode, so I simply can't remove or drop the related .xcodeproj folder if I wanna keep the development and release flows same.

Inside a xcodeproj file, I found 3 more files and folders:

1. Project.pbxproj
2. xcsharedata folder
3. project.xcworkspace

Project.pbxproj is a 1 file containing the config context on files, references & dependencies etc. 

If this is wired wrongly, then when xcode builds your app for release, things could go wrong.

Project.pbxproj settings and config is responsible for how the files and folders are wired and show up in the xcode UI in our projects.

and finally, Project.xcworkspace inside .xcodeproj should never be tampered with.

It contains information for running your xcode workspace and mainly won't contain changes to be commited to apps.

However, swift package manager lock files should be commited.

`swiftpm/Package.resolved`

this can change when adding or removing dependencies using swift package manager. 

all this, for doing something that go.mod and go.sum files do.

for a novice, this seems like a declarative hell. honestly.

I really wish this isn't normalized.  -- 2026-10-04T11:37:24.607Z

---

I wouldn't say I was really proficient with github comments formatting but today I learnt how to create a collapsable section.

and, it's pretty straightforward!

```html
<details>
<summary>More details:</summary>
**the usual markdown gore**
</details>
``` -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/image_vqD9e8L.png) [🏞️ Context #2](https://cpx.tnvmadhav.me/content/image/content-images/image_ZrwGEpE.png) -- 2026-10-04T09:58:36.072Z

---

I'm reading the Pragmatic Engineer Pulse newsletter...

https://newsletter.pragmaticengineer.com/p/the-pulse-ror-creator-sparks-new


This edition talks about the following:

1. The shock of DHH's positioning and words ofc (I agree with DHH overall positioning)

2. The angst in small, medium and big tech where nobody knows or owns decisions (I too feel the same recently, I'm trying to change the way I work)

This hit me specifically. 

At first, in early 2026, I felt that using AI for work would mean spend less time doing design and development and spend more time living life.

Now that I'm leading a team, I am backtracking this thought right now. 

No! When you are responsible in multiple areas, quality and speed, the work has increased significantly. More effort goes in to quality analysis. 

So, for slow learners & fragile adopters of new tech, this is a warning call.

More effort needs to be put into place for getting this productivity in code generation in the right path to higher ROI.

It's a Gold Rush out there for people successfully navigating this wave and keeping their sanity while realising huge return of interest.

One thing I'm noticing, people who have maintained high standards in product quality through diligent integrity and practices aren't affected much by this. In fact, they are the ones riding this monstrous wave.

Those who have been building software the "right" are way more resilient from facing downsides right now.

The Antifragile live on.  -- 2026-10-04T09:08:32.830Z

---

Shopify is doing a migration to from legacy react native system to native builds for android and iOS.

https://x.com/TnvMadhav/status/2098265718831890565?s=20


source: https://shopify.engineering/back-to-native  -- 2026-09-11T04:25:45.601Z

---

shopify acquires tailwind 😦
https://tailwindcss.com/blog/tailwind-is-joining-shopify


  -- 2026-09-10T04:15:56.959Z

---

I had a nice meal last night 😋 #foodblog -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/IMG_7563.jpeg) -- 2026-08-22T11:12:25.823Z

---

> It will have strong privacy and security options so you can trust it to handle all of your personal content knowing that no one else can access your information, similar to how encryption works on WhatsApp


https://www.meta.com/thefutureisforeveryone/#:~:text=It%20will%20have%20strong%20privacy%20and%20security%20options%20so%20you%20can%20trust%20it%20to%20handle%20all%20of%20your%20personal%20content%20knowing%20that%20no%20one%20else%20can%20access%20your%20information%2C%20similar%20to%20how%20encryption%20works%20on%20WhatsApp.  -- 2026-08-11T05:02:21.597Z

---

List of interesting links I found today:

Read HN twice a day for the last decade. Here's my list of S-Tier HN links
https://news.ycombinator.com/item?id=49183198


Why Estonians invite strangers into their back gardens each summer
https://www.bbc.com/travel/article/20260731-why-estonians-invite-strangers-into-their-backyards-each-summer


My emergent thoughts on ads
https://x.com/TnvMadhav/status/2085657823099433121?s=20


The Friendship That Made Google Huge
https://archive.is/w4oWL  -- 2026-08-07T09:34:43.157Z

---

# New Updates to ChatGPT and Codex

- One super app for both chatGPT and Codex
- You can create automations from chat itself

https://x.com/OpenAI/status/2075274271845404744?s=20

It’s codex but it’s re-introduced for non-coders to start work from ChatGPT work desktop!


OpenAI chatGPT Twitter account also shared a look and feel, a dip toes in the water sort of dem video.
https://x.com/ChatGPTapp/status/2075336584451539353?s=20


While my work is intact on the Codex app, the icon itself has changed a bit, as in the name has changed to chatGPT instead. 

The icon on the status bar, however, is still the chatGPT icon and not the Codex icon. I'm not sure if this is a bug but when I enforced custom icons to be the same as Codex itself, it didn't change on the status bar. 
￼


…and then I opened the app and noticed 3 new models available for use:

- GPT 5.6 Sol
- GPT 5.6 Terra
- GPT 5.6 Luna
 at this point I just don't know what they are but I want to find out quickly. 


Most of the marketing content on my Twitter timeline doesn't talk about soul, luna, or terror. It just talks about GPT 5.6 so clearly you might have to do things and figure out by yourselves. 

What if I asked ChatGPT itself? 


ChatGPT also stated or cited the blog post from openAI. 

> We’re launching the GPT‑5.6 family of models for general availability following our limited preview⁠: our new flagship, Sol, alongside Terra, a balanced model for everyday work, and Luna, our most cost-efficient model.

> GPT‑5.6 Sol sets a new high of 53.6, eclipsing Claude Fable 5 (adaptive reasoning) by 13.1 points. Even at medium reasoning, it beats Fable 5 by 11.4 points at roughly one-quarter the estimated cost. 

Results of a certain few benchmarks have been shared in this blog post.  https://openai.com/index/gpt-5-6/


---

For my automations that are setup, I asked chatGPT to compare the prices of GPT 4o mini and GPT 5.6 Luna and it looks like luna is 6.7x more expensive than the former. 
> If you meant GPT‑4o mini, the gap is larger:
> * GPT‑4o mini: $0.15 input / $0.60 output
> * Luna: $1 input / $6 output
> * Luna is approximately 6.7× more expensive on input and 10× on output. GPT‑4o mini pricing

---

ChatGPT iOS app has replaced codex tab with remote tab


---

The slider feature for reasoning levels for the GPT 5.6 Sol is sort of interesting. Is this feature here to stay?


---
It's also interesting that in the chatGPT app, without the remote connections, GPT 5.6 Terra and Luna aren't available and only Sol is. 


---
Another update then I noticed is that there are more options for selected text on the on the ChatGPT Codex app on the desktop.  

More details seems to be slightly similar to ‘Ask in Side Chat’ (I think the naming wasn’t changed to Side Task or whatever)?

I asked GPT 5.6 Sol about this and learned the following:

1. The ask ‘for more details’ basically means explain this sentence or thing in more words without worrying about follow up questions (you still can if you want to)
2. The ‘ask in side chat’ is a more generic one where you can take things (out of context?) and ask another agent to do something with it.  
So basically ask for more details is a more specific implementation of side-chat.


---
There should be an /action in a /sidechat that essentially tells codex to update findings in the main thread
 -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/ChatGPT.png) [🏞️ Context #2](https://cpx.tnvmadhav.me/content/image/content-images/NiceShotPro_-_for_mac.png) [🏞️ Context #3](https://cpx.tnvmadhav.me/content/image/content-images/15.6_So..png) [🏞️ Context #4](https://cpx.tnvmadhav.me/content/image/content-images/image_tQjHOeq.png) [🏞️ Context #5](https://cpx.tnvmadhav.me/content/image/content-images/Open_Codex.png) [🏞️ Context #6](https://cpx.tnvmadhav.me/content/image/content-images/Advanced__LIPIlJr.png) [🏞️ Context #7](https://cpx.tnvmadhav.me/content/image/content-images/OPT_S.6_Sol.png) [🏞️ Context #8](https://cpx.tnvmadhav.me/content/image/content-images/image_8xJe68W.png) [🏞️ Context #9](https://cpx.tnvmadhav.me/content/image/content-images/update_the_main_thread_with_these_findings_now.png) -- 2026-07-10T10:36:13.114Z
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
[About Http Range Headers](https://tnvmadhav.me/til/about-http-range-headers/) -- 2026-01-29T03:54:45+00:00

[Closing Github Pull Requests in Bulk](https://tnvmadhav.me/til/closing-github-prs-in-bulk/) -- 2026-01-03T04:19:34+00:00

[DynamoDB and F.I.P.S. Compliance](https://tnvmadhav.me/til/dynamodb-and-fips-compliance/) -- 2025-11-02T05:57:47+00:00

[Single Dispatch Functions](https://tnvmadhav.me/til/single-dispatch-functions/) -- 2025-10-20T04:23:01+00:00

[How to Open a File in Browser From Terminal?](https://tnvmadhav.me/til/how-to-open-a-file-in-browser-from-terminal/) -- 2025-10-09T07:46:17+00:00

More on [My TILS](https://tnvmadhav.me/til/)
<!-- til ends -->

</td></tr></table>


All credits of this idea to [Simon Willison](https://github.com/simonw/simonw/).