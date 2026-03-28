## My Latest Feed

<!-- feed starts -->
I've thought about this beforehand so don't fret too much. just follow.

The answer is to be in "war mode" until you're "done".

What "done" is depends on when you wanna stop but if you wanna do it more, you're not done.

"War Mode" is basically falling back on "hard work" over "soft work"

"Hard Work" is working with full concentration without context switching until a "milestone" is reached.

A "Milestone" is anything that will help you do the same thing in lesser time and hopefully lesser effort. It's also something that will "up your attributes" to know what the next milestone is. If you don't know what you're next milestone is, you don't know what to do so that's where you're likely "done".

Now you can think if you wanna do more of it but you don't know what to do, that means you've ascended to local maxima. You may have to backtrack and find the next "milestone" in the process. This is hard but you must walk it.

The goal is to work until you don't know what to do next and you're ready to hang it and relax on that aspect.

I generally think this would be at the age of 65 where you're not providing value to the world even with the best (90%) of your capability without hurting yourself more.  -- 2026-03-28T09:03:55.945Z

---

Today I learned that we can check if 2d **slices** are equal using `reflect.DeepEqual` function in golang. 

This isn't fast because recursion is involved so writing an iterative loop is must faster.

I always thought we could use `==` operator but looks like we can't (unlike 2d arrays) :/

so `reflect.DeepEqual` seems to be a syntactical sugar of sorts, which was what I wanted :P  -- 2026-03-22T11:53:52.785Z

---

Today I learned how to convert an integer to binary string format in python using standard functions available.

binary_string = format(n, '0Nb')

where N is the number of digits we need

```txt
>>> format(10)
'10'
>>> format(10, 'b')
'1010'
>>> format(10, '9b')
'     1010'
>>> format(10, '09b')
'000001010'
```

I also found another way to convert binary string back to integer.

integer = int(binary_string, 2)

Now, this means the following python statement will always be true for any integer (I guess there are no edge cases here but maybe I'm wrong):

assert integer == int(format(integer, 'b'), 2)  -- 2026-03-08T12:08:11.952Z

---

TIL how to format strings in PostgreSQL using format function.

It’s similar to formatting like that if go or c.

https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-FORMAT  -- 2026-02-18T03:13:38.330Z

---

we have come to a point where we don’t know if anything is real or not. like if it’s found on digital media. which is why I feel there will be a Cambrian explosion of things that people build on the internet create and in terms of content (video content especially) and also for the other modalities, which is why we need to conclude that everything  is going to blow up like never seen before, and hence we should limit what we consume on the internet through pools of peer reviewed facts and news (if not already)  -- 2026-02-15T05:31:48.871Z

---

i found myself reading a post from go blog: https://go.dev/blog/defer-panic-and-recover  -- 2026-02-11T03:22:03.499Z

---

if you feel that you’re falling behind, then know that what you do between 5 to 9 will improve your 9 to 5 experience sooner than later.  -- 2026-02-05T03:06:22.072Z

---

Excerpts from “Code is cheap, show me talk” by Kailash Nadh

> An experienced developer who can talk well, that is, imagine, articulate, define problem statements, architect and engineer, has a massive advantage over someone who cannot, more disproportionately than ever.

for reference https://nadh.in/blog/code-is-cheap/  -- 2026-01-31T05:06:30.887Z

---

TIL about HTTP Range Headers

https://tnvmadhav.me/til/about-http-range-headers/ -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/image_7c5oZw0.png) -- 2026-01-29T04:52:52.400Z

---

I decided to give in and setup a @clawdbot daemon today for fun. Remotely on a fresh ec2 instance.

Apart from some hurdles, i got it working via telegram trigger.

I see the vision, have some ideas and yes we’re getting close.

Remote personal agents. Cambrian explosion. I see it.  -- 2026-01-25T12:31:07.842Z
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