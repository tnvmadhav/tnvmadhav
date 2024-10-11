## My Latest Feed

<!-- feed starts -->
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

---

I finally bit the bullet and learned to use SwiftData and it turned out to be simple to use (as a beginner). 

I'm playing around to try and learn how the data is modeled.

I could go from ephemeral to persistent storage in a couple of hours.  -- 2024-09-29T14:59:30.158Z

---

Excerpts from [Using Progressive Enhancement by GOV dot UK](https://www.gov.uk/service-manual/technology/using-progressive-enhancement)

> "Progressive enhancement is a way of building websites and applications based on the idea that you should make your page work with HTML first."

HTML and CSS layers are fault-tolerant (browsers will ignore declarations that it doesn't understand). 

Javascript must only be used to enhance user experience in necessary parts of data that are already in HTML.

>"Where possible the JavaScript should enhance HTML and CSS that provide the same core functionality. For example, an autocomplete could enhance an element, or something similar. This still lets the user do what they need to do, even if the JavaScript fails."

HTML and CSS offer the bottom layer (Layer 1) where things can happen but rather slowly. Javascript layer to exist to make a certain action faster. If the javascript layer is to be removed, the required functionality would still be possible albeit slowly as initially intended.

This way, no process is "blocked" during Javascript-based failures, etc.

> "If you believe your service can only be built using JavaScript, you should think about using simpler solutions that are built using HTML and CSS and will meet user needs."
> For example, if you want to use JavaScript to provide interactive graphs, other options are to:
> 
> Display the data in a table
> Allow the data to be exported so that it can analysed in another application
> Pre-render the graphs as images
>
> If the core functionality of your service cannot be provided without JavaScript, you’ll need to consider how users can access your service through other channels. This might be telephone calls or in-person visits to offices.

Looks like the UK gov prefers in-person processes rather than injecting Javascript into government websites. This a highly opinionated decision.

> If you do choose to use client-side JavaScript frameworks, be aware that although they can be helpful when building a service with a complex user interface, they can introduce problems.
>
> Using a client-side JavaScript framework can:
>
> Increase the overall size of your code base and push processing to the client side, causing performance issues for users with a slower network connection or lower-powered device
> Create a reliance on third-party code that your developers do not have control over, requiring you to make major changes to your service to stay up to date with changes in the framework
> make it difficult to find people with the skills required to maintain the code, if the frameworks lose popularity over time
> If you use a JavaScript framework you should:
>
> Be able to justify with evidence, how using JavaScript would benefit users
> Be aware of any negative impacts and be able to mitigate them
> Consider whether the benefits of using it outweigh the potential problems
> Only use the framework for parts of the user interface that cannot be built using HTML and CSS alone
design each part of the user interface as a separate component
>
> Having separate components means that if the JavaScript fails to load, it will only be that single component that fails. The rest of the page will load as normal.

I can understand this approach, keeping things light and simple is a win, and keeping the user base in mind (literally everyone in the country in this example), it's important to ensure stability and dependency-less design.

The userbase for a normal corporate may or may not be the same, so the design for the userbase is a good way to think about problem-solving.

> "If you use JavaScript, it should only be used to enhance the HTML and CSS so users can still use the service if the JavaScript fails."

> "Some users may deliberately turn off features in their browsers. You should respect their decision and make sure those users can still use your service. Some users may deliberately turn off features in their browsers. You should respect their decision and make sure those users can still use your service."

A user can turn off JavaScript in their browsers AND direly need certain services.


> "Do not build your service as a single-page application (SPA). This is where the loading of pages within your service is handled by JavaScript, rather than the browser."

A subset of users using accessibility features may get a sub-optimal or dead-end experience. The heavy use of back and forward buttons and page refresh can cause states that they don't intend or understand.

The UK government has [written another piece](https://technology.blog.gov.uk/2016/09/19/why-we-use-progressive-enhancement-to-build-gov-uk/)  on why progressive enhancement is good (I agree in favor of incremental improvements as good engineering practice): 

### Quoting architect of gov dot uk

> "Progressive enhancement is about resilience as much as it is about inclusiveness." -- 2024-09-29T04:39:18.497Z

---

TIL there is a site [pyvideo.org](https://pyvideo.org) that curates videos from community and related events. -- 2024-09-28T16:30:03.005Z

---

I found [a really useful refresher/guide](https://ssoready.com/docs/saml/saml-technical-primer) to get back to while working with SAML

Worthy of a bookmark! -- 2024-09-28T12:30:03.033Z

---

Some text snippets from the white paper on reading comprehension on plain paper vs on a screen

> "If texts are longer than a page, scrolling and the lack of spatiotemporal markers of the digital texts to aid memory and reading comprehension might impede reading performance."

> "...Hence, we cannot say whether the visual ergonomics of the laptop computer screens hurt subjects’ reading. In future studies, employing online measures including eye tracking methods would appropriately address this important issue."

> ".... Scrolling is known to hamper the process of reading, by imposing a spatial instability which may negatively affect the reader’s mental representation of the text and, by implication, comprehension."

via [HN](https://news.ycombinator.com/item?id=41644086) -- 2024-09-28T09:30:03.016Z

---

If your AWS deployments seem unnecessarily slow, you could do something about it.

I've found a [well-written piece](https://nathanpeck.com/speeding-up-amazon-ecs-container-deployments/) that could help. -- 2024-09-27T12:30:03.052Z

---

They’re perfect for airpods
https://twitter.com/twitter/status/1839351084630028749/ -- 2024-09-27T06:30:03.003Z
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