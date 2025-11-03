## My Latest Feed

<!-- feed starts -->
Start by copying, you'll end up with something new.  -- 2025-11-03T12:30:02.866Z

---

I went down a rabbit hole on the aws us-east-1 outage that happened on 20th October 2025 and learned a bunch of things. 
Noted down some things I learned https://tnvmadhav.me/til/dynamodb-and-fips-compliance/  -- 2025-11-02T14:30:23.044Z

---

Read "The Day You Became a Better Writer" by Scott Adams. -- [🏞️ Context #1](https://cpx.tnvmadhav.me/content/image/content-images/image_rnqguj5.png) -- 2025-11-02T14:23:44.711Z

---

The root cause of anything is the big bang.  -- 2025-11-02T13:08:25.690Z

---

The code I wrote a year ago to the same problem is identical to the code I wrote today and I don't know how I should feel about it.  -- 2025-11-01T05:17:24.600Z

---

> In the Survival Stage of your business, focus your efforts on creating the features that make your service noticeably better for the majority of your users without making the product harder to use. If a feature accomplishes this, go ahead and build it. If it doesn't, stash it for now and build something else that does.

Excerpt from Kahl, Arvid. Zero to Sold: How to Start, Run, and Sell a Bootstrapped Business (pp. 233-234). (Function). Kindle Edition.  -- 2025-10-31T13:40:57.986Z

---

I asked chatGPT help understand OpenAI’s PBC transition:

WHAT IS A PUBLIC BENEFIT CORPORATION (PBC)?

A Public Benefit Corporation (PBC) is a legal for-profit corporate form that requires
directors to balance financial interests of shareholders with a stated public benefit(s).
It blends profit motive with an explicit mission (e.g., social, environmental, educational).
PBCs typically have extra transparency and reporting obligations and may embed the
public benefit into governance documents.


STRUCTURE & KEY PARTS OF A PBC

- For-profit entity: Operates to make profit and can raise capital like a normal corporation.
- Public benefit statement: A clear, often legally required statement of the specific public benefit(s) the company aims to pursue.
- Board of directors' duties: Directors must consider both shareholder value and the public benefit; decisions should reflect a balance.
- Accountability & reporting: Many jurisdictions require an annual benefit report describing progress on the public benefit.
- Stakeholders: Beyond shareholders — customers, employees, community, environment are legitimate considerations.
- Benefit enforcement: Stakeholders or special benefit directors/inspectors may have standing to enforce benefit obligations depending on jurisdiction.


COMPARISON: PBC vs TRADITIONAL CORP vs NONPROFIT

Characteristic        | PBC                         | Traditional Corporation     | Nonprofit                  
Primary purpose       | Profit + explicit public benefit | Maximize shareholder value | Public benefit (no private profit)
Profit distribution   | Yes (to owners/investors)   | Yes                         | No (surpluses re-invested)  
Legal duty of directors | Balance profit + benefit  | Primarily shareholder value | Advance mission; no private dividends
Raising capital       | Easier (can attract equity) | Easiest                     | Limited (grants, donations)
Transparency/reporting| Often required (benefit report) | Typically financial only   | Often high mission reporting

Note: exact duties and enforcement depend on jurisdiction (state/country law).


EXAMPLE PBC OBJECT:

SunForAll, Inc. — PBC
Owners: InvestorA(40.0%), Founder1(30.0%), Founder2(20.0%), EmployeesPool(10.0%)
Board: Founder1, Founder2, IndependentDirectorA, BenefitDirector
Benefit: Affordable clean energy access
Description: Increase access to low-cost, low-carbon electricity for low-income communities.
Retained earnings: $120,000.00

CURRENT BENEFIT METRICS (sample values 0..1):
 - reduction_in_cost_per_unit: 0.75
 - access_increase_index: 0.60
 - worker_safety_index: 0.95
 - retention_improvement: 0.50
 - community_outreach: 0.20

SIMULATION: Decisions balancing profit vs public benefit

Note: Directors must consciously weigh financial outcomes and the declared public benefit.
You can adjust 'weight_profit' and 'weight_benefit' to model different board priorities.

Proposal: Open a new mass-production line
  Estimated profit change: $600,000
  Benefit metric summary: {'reduction_in_cost_per_unit': 0.8, 'access_increase_index': 0.4}
  Combined decision score: 0.650 -> APPROVE

Proposal: Improve workplace safety with expensive retrofit
  Estimated profit change: -150,000
  Benefit metric summary: {'worker_safety_index': 0.95, 'retention_improvement': 0.6}
  Combined decision score: 0.612 -> APPROVE

Proposal: Marketing campaign increasing prices slightly
  Estimated profit change: $200,000
  Benefit metric summary: {'community_outreach': 0.1}
  Combined decision score: 0.425 -> REJECT


FURTHER NOTES / REAL-WORLD POINTS:

- Legal details vary by jurisdiction (e.g., Delaware, other US states, and other countries).
  Some places call similar entities 'benefit corporations' or have different rules.
- Enforcement varies: in some places, shareholders, the benefit director, or other stakeholders
  can bring lawsuits if the company fails to pursue its benefit.
- PBC structure helps align mission-driven founders with investors by making the mission
  a legally protected part of the entity's purpose.
- A PBC does not guarantee success in both profit and benefit; it changes the legal obligations
  and governance to require balancing, and increases transparency/expectations.


i'm referencing a post that can be found here:
https://openai.com/index/built-to-benefit-everyone/  -- 2025-10-29T04:44:28.114Z

---

The “making it” for variety of things have different time frames.

>  “Fake it until you make it” is often dismissed as shallow, but it’s closer to Franklin’s truth. Faking it long enough is making it. The repetition of behavior, not the sincerity of belief, is what shapes character.

The time frame is dependent on how aligned your honest self is to your phony self[^1]

i'm referencing a post that can be found here: https://boz.com/articles/you-are-how-you-act


[^1]: https://en.wikipedia.org/wiki/True_self_and_false_self?wprov=sfti1  -- 2025-10-27T04:45:00.042Z

---

The browser wars have officially begun and whoever participates is forced to improve the agentic flows and there would be (IMO) a local maxima beyond which prompt injection becomes a catastrophic vector.

If google chooses to not participate, a significant portion of people can choose to migrate off google chrome and google might lose a significant chunk of market share or something idk… only until things go belly up when really bad prompt injection events come to light 

If google chooses to participate, then it’s over. Google chrome has a large market share and this means google will also be cornered into the aforementioned local maxima until damage is already done to small % of affected users. small % but large absolute number.

Prompt injections cannot be stopped until something novels comes about. but for time being it’s not looking good for google (in near term atleast). happy to be wrong about it. 

i'm referencing a post that can be found here: https://x.com/daniellockyer/status/1980895459670634933?s=12  -- 2025-10-22T13:25:10.993Z

---

You must’ve heard the “why is my washing machine sending soo much data to cloud?” joke from a few years ago.

Well, now replace ‘washing machine’ with ‘bed’

[Quoting Michael Zimmermann](https://x.com/zimm3rmann/status/1980491408948572167?s=46)

> Is 16+gb/mo a normal amount of telemetry? Can you not do any local compute of “get hot” or “get cold” with a multi core processor and multiple gigabytes of memory? Can’t just repeat the previous nights settings? 
> 
> It’s bad enough that you slapped a $ 200/yr subscription on things, worse that it doesn’t work at all without internet.


This whole thing came to light after many instances of EightSleep mattresses (pods) stopped functioning due to an AWS outage (which is hilarious and horrific at the same time).

This reminds me of a joke (and a truth):

> If you want to know how dependent something is to the world, turn it off
 
A single high-value region on AWS went down recently and several external entities were disrupted and EightSleep pods were one of them.

EightSleep is fine but anything else that’s very critical is not. 

This global incident should be a wake up call for dependent services to plan and support failovers. For consumer products to support offline mode. (either ways for a temp controlled bed to depend on cloud to function normally is ridiculous to a layman).

i'm referencing a post that can be found [here](https://x.com/m_franceschetti/status/1980419272766583262?s=12).


I tried to make a joke on [x dot com](https://x.com/tnvmadhav/status/1980853076312633665?s=46)  -- 2025-10-22T04:28:05.994Z
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
[DynamoDB and F.I.P.S. Compliance](https://tnvmadhav.me/til/dynamodb-and-fips-compliance/) -- 2025-11-02T05:57:47+00:00

[Single Dispatch Functions](https://tnvmadhav.me/til/single-dispatch-functions/) -- 2025-10-20T04:23:01+00:00

[How to Open a File in Browser From Terminal?](https://tnvmadhav.me/til/how-to-open-a-file-in-browser-from-terminal/) -- 2025-10-09T07:46:17+00:00

[Rosetta 2: Apple's Temporary Fix](https://tnvmadhav.me/til/rosetta-2/) -- 2025-06-22T08:16:35+00:00

[Http Archiving -- Capturing a moment in time](https://tnvmadhav.me/til/http-archiving/) -- 2025-02-23T09:43:37+00:00

More on [My TILS](https://tnvmadhav.me/til/)
<!-- til ends -->

</td></tr></table>


All credits of this idea to [Simon Willison](https://github.com/simonw/simonw/).