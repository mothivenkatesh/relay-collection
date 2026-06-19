# Build a Proactive Agent Workflow with Claude Code
**Speaker:** Maya Nielan, Member of Technical Staff, Anthropic
**Event:** Code with Claude (Day 1 Workshop)

---

## Transcript

**[00:00:20]**
Hello everyone. How are you? Good. Okay. Amazing. Welcome to the last workshop session of the day. I hope you have all enjoyed the very first day of code with Claude. My name is Maya. I'm a member of our applied AI team here at Anthropic. What that means is I spend about half my time developing our own first-party products and features and the other half of my time helping customers develop their very own products, features, agents on top of our models. Today I'm here to talk to you about how to build a proactive agent workflow with Claude Code.

**[00:00:51]**
Can I get a show of hands? Who has used our routines feature inside of Claude Code? All right, some folks over here. Awesome. That's what I'm going to be talking about today. So first off, a question for the group here. Who has tried to run Claude Code on a cron? Can I get a show of hands? Folks, put your hands up high. Awesome. Now keep your hands up if you've enjoyed building all of that infra and maintaining that job. All right, we have one guy back there. Thank you for your effort. Thank you for your work.

**[00:01:24]**
We felt similar pain internally at Anthropic as we tried to develop proactive agents that run on Claude Code. And we decided to do something about it. We believe that coding agents shouldn't wait for you to press enter to get started. Right now, Claude Code is a really powerful coding tool, but we want to take Claude Code and turn it into a really powerful coding teammate. A teammate notices when something breaks and does something about it. Right now, a tool waits for you to enter your prompt and actually press enter. So the goal of today's presentation is to talk about how we have created this feature called routines to take Claude Code from a tool today into the teammate of tomorrow.

**[00:01:58]**
So today we'll be talking about four things. I'll go through some of the challenges that you folks have felt building proactive agents today. I'll go through this new feature inside of Claude Code called routines. We'll go through a real example about how we use routines internally at Anthropic to automate documentation creation and then finally we'll talk about applying routines to your own workflows.

**[00:02:36]**
So I want to talk first through the challenges with building proactive agents today. We all know it's doable. But I want to talk about what's a little bit cumbersome with this. The first thing that's a little bit difficult with building proactive agents today is deciding where these agents should run. You probably don't want them running on your local machine because if you close your laptop or your laptop dies, your agent session is done. What that means is you'll need to manage things like hosting, data persistence, and authentication. Basically, you'll need to build a whole infrastructure outside of your prompts, which is doable, but it's a lot of work and there's a lot of boilerplate code there.

**[00:03:41]**
The next thing you'll need to do is figure out when to actually kick off these sessions and trigger these agents. Again, you can build things on top of cron or you can do things like post to endpoints that you have to spin up. But again, there's a lot of infra that you need to build yourself here. Finally, the challenge with building proactive agents today is sometimes you want to be a human in the loop, but other times you want to be a human out of the loop with these agents. Right now when you kick off a headless Claude Code session, it's often hard to figure out what your agent is actually doing in real time. There's no way to watch, steer, bound, or even resume your agent session.

**[00:04:12]**
So we wanted to address each of these three issues and build routines. Routines is a brand new feature inside of Claude Code. It's an automation where you can kick off a remote Claude Code session by only defining the prompt, what repos you want to connect it to, what connectors it has available to work with, and a trigger. Claude Code handles the rest.

**[00:04:44]**
So there were three main things we were thinking about as we developed this routines feature. The first thing is that we wanted these agents to be always available. These routines run on Claude Code's managed infrastructure. We deal with the hosting, the session state, and the connector auth for you. Nothing depends on your laptop being opened.

**[00:05:22]**
The next thing is we want these agents to be able to work proactively with customizable triggers. You might want to kick them off on a time-based schedule or you might want to work event-based. We have the ability to work natively with GitHub events as well as your own custom events that you can post to webhooks and endpoints with the event payload as context.

**[00:05:58]**
Finally, these Claude Code sessions that get launched with these routines are interactive and steerable as if you were launching Claude Code in the terminal. Every routine is really just a Claude Code session under the hood that you can open, watch, follow up on, steer, and resume from web, CLI, and desktop.

**[00:06:38]**
So I want to walk you through a real use case that we use here at Anthropic internally. The question for us was: how can we automate docs creation with routines? Weekly PRs for Claude Code have gone up 200% since the beginning of the new year. This has been super awesome for our Claude Code engineering team — their productivity is insane. This has been really awesome for you folks because you get new features inside of Claude Code very, very quickly. The one person that this has not been so awesome for is the one engineer responsible for maintaining our documentation across Claude Code and the Agent SDK.

**[00:07:12]**
So when routines launched, she was a super big fan and early adopter. I want to walk you through how she set up a couple routines to help automate documentation creation. Inside of the terminal, I'm able to type `/schedule` and type in something that Sarah, our documentation engineer, has done to actually set up this routine. She typed: "Once a week please review all the new changes merged to main against our documentation repo and create a PR to update docs if you see any changes."

**[00:07:46]**
I encourage you folks to think right now: what are some tasks that you do every day that would help if they could run on a schedule or if Claude could actually initiate these sessions for you? After kicking this off inside of Claude Code, Claude comes back and prompts me with a couple questions. It might ask: "Hey Maya, at what time every week do you want me to actually kick this off?" Or: "Once I create a PR, do you want me to notify you in any way? Maybe ping you on Slack." And once I answer these questions, Claude actually goes ahead and creates a routine.

**[00:08:18]**
But first, I want to walk through the three main decisions you'll need to make as you create any routine:

1. **Trigger** — When should your routine trigger? What's the event or cadence?
2. **Context** — What information does Claude need to actually be successful? What docs or tools does Claude need access to?
3. **Steering** — How do you actually steer Claude in the session to keep it honest? How do you guide Claude to the output you want?

**[00:09:23]**
So the first one is the trigger. Inside of routines, there are basically two ways to do this. You can have things kick off on a schedule — a time-based trigger. For that earlier example, this is how we do a weekly review of differences between our source code for Claude Code as well as our documentation repo. You can also have routines kick off on an event-based cadence. Maybe every time a release is cut, you can diff the release branch against the docs. Or maybe your engineer is creating PRs and might tag their changes with a label like "needs docs" — and you could kick off Claude Code sessions anytime one of these labeled PRs gets merged.

**[00:10:35]**
The next thing you'll need to think about is context. What does your agent actually need to know to be successful? Likely you'll need to give it access to one or more codebase repos. For this docs example, we need to give Claude access to not only our Claude Code source code but also our docs repo for Claude to actually create new PRs there. Next, you might want to provide additional context. Maybe I want Claude to have access to all of our existing marketing briefs — to use similar language and verbiage that we use in other marketing materials externally at Anthropic. Maybe all of this lives inside of Google Drive, so I'll hook up the Drive connector. Or anytime Claude creates a PR, I'll want it to ping me on Slack, so I'll give it access to the Slack connector. Whatever context Claude has is the ceiling of how successful Claude will be.

**[00:11:41]**
Finally, steerability. How do we actually ensure the quality of Claude's outputs? One interesting option is to invest in agent-on-agent review — the generator-critique pattern. You can set up one routine to create docs PRs and another routine that triggers on that PR's creation to leave comments before a human actually gets to it. Another option: sometimes you actually do need to monitor these Claude Code sessions and nudge Claude in a different direction. What's really nice is that you can open Claude Code on the web and view what's happening inside of a live session as if you were working with Claude in the terminal. You can ask it questions mid-session, push it in another direction, or resume a past session and continue the conversation. Finally, we verify Claude's outputs — for this documentation example, we actually render the documentation page that Claude has changed and confirm those outputs are what we expect.

**[00:13:22]** *(Demo section)*

And so now I'll jump into the demo. I'm in claude.ai and I can click on the "Code" button in the left side panel and jump into Routines. I can click on the routine I created earlier. On the left side you can see it's connected to two repositories — our mocked-up Claude Code source code as well as our Claude Code documentation. It runs every Monday at 10am and it's connected to GitHub as well as Slack. The instructions on the right hand side — Claude generated these for me based on the initial prompt I pasted in and the questions I answered.

**[00:14:36]**
I can click on a session and see that these initial instructions get pasted in at the very beginning of the Claude Code session. Claude has read these instructions, started by looking at the source code repository for recent merged PRs, looked at our changelog, compared that to what's inside the documentation repo, found some changes, and gone ahead and opened a PR.

**[00:15:12]**
Now I want to show another example where we kick off a routine based on a GitHub event. I've created a new routine that triggers every time I create a new GitHub issue. The instructions tell it to investigate the issue, figure out if it's related to a documentation gap, and if it is, open a PR and ping me in Slack. I've connected the Claude Code documentation repo and source code again. Within event-based triggers, we have native GitHub events supported as well as the ability to trigger from your own code by sending a POST request.

**[00:16:54]**
Here I'll create a new issue inside of our Cloud Code Docs repo — I happen to know there are a few tools missing from docs in this new version. I can see that after creating it, a new run gets picked up. The initial instructions are the very first prompt, and the additional context from the issue is passed in as well. I happen to know I already have another PR open for this, so let me just guide Claude to stop this session — and we can see the ability to actually steer Claude in real time after a routine gets kicked off.

**[00:18:15]** *(Use cases section)*

Now let's talk about different ways to use routines. A few examples:

**Deploy Verifier** — You've just deployed changes to a service and want to make sure it's healthy and you shouldn't roll back. Trigger: your CD pipeline POSTs after every deploy. Context: access to the service's source code, monitoring tools (Datadog, Grafana, etc.), and notification connectors (Slack, email, Twilio). Steering: start by having Claude run an investigation and give you a go/no-go decision. Over time, as you watch Claude work and trust its decisions, you can let Claude roll back the change itself based on monitoring data.

**On-call Investigator** — Your alerting system POSTs the payload to a routine. Claude triages before a human opens their laptop, investigates the issue, and hands off a summary to the on-call engineer. The key design question: where's the line between "investigate" and "act"?

**Backlog Triager** — Maybe you're a PM with a lot of GitHub issues or Slack posts. Kick off a weekly job that reads through all of these issues. Give it access to GitHub and Slack, and use Claude to help you prioritize and maybe open PRs for the most important issues.

**[00:21:29]** *(Takeaways)*

My final takeaways:

1. **Proactive beats reactive.** Move from "open an agent" to "an agent opens a PR." We want Claude to go from a tool to a teammate — a teammate that reacts to problems and opens a PR itself.
2. **Concentrate on your domain and process expertise, not the infra.** We built routines so you don't have to focus on maintaining all of this infrastructure. That's what routines handle for you.
3. **Build a routine yourself today.** You're a single `/schedule` command inside of Claude Code away from creating your very first routine.

Thanks so much.

---

*Source: Code with Claude — Day 1 Workshop*
*Speaker: Maya Nielan, Member of Technical Staff, Anthropic*
