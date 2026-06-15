**Q1: How does a payment event trigger and complete a process?**

When a payment event occurs, Relay instantly springs into action. It automatically checks two things: 

* Is this event relevant to you,   
* Have all the right conditions been met?

Once confirmed, the system executes all the steps you've configured—in any order you've set up—to automate your task. The process runs until it's finished, and for complete peace of mind, every single action is recorded and stored in our system for a perfect audit trail.

\---

**Q2. What does the payload of a Payment Success event actually contain? What fields does a developer get that they wouldn't get from a generic Zapier webhook?**

The data you receive is similar to what Zapier provides, but our solution is integrated with cashfree notifications. It does seamless integration with Cashfree's webhooks and APIs. This means less effort for you because you have direct access to our public APIs. You don’t have to go back to our developer documentation again and again.

\---

**Q3: What's the difference between a simple Webhook and the more powerful HTTP Request connector?**

* **Webhook (Simple Alert):** This is just a notification that tells your system, "Something happened" (like an "order placed"). It's mostly for receiving updates.  
* **HTTP Request Connector (Two-Way Action):** This is much more powerful. It can perform complex security checks and actually take action in other systems, such as creating, changing, finding, or deleting information.

\---

**Q4: How does the AI feature work within the workflow, and what models do we support?**

The AI capabilities are built into "skills" we provide. We use an mcp (platform) that seamlessly works with all the popular and cutting-edge large language model (LLM) tools, including Claude, OpenAI, and Gemini. We don't limit you to a single provider. Our approach is to give you maximum speed, so you can start using the newest models. In a nutshell, you don’t need to wait for us to release "Claude Mythos," you will be able to use it the day it is launched.

\---

**Q5: What are the biggest technical challenges behind the scenes for Relay?**

While our team of developers, product managers, marketing and account managers work collaboratively to solve problems, we face typical challenges that every engineer at Cashfree is trained to handle, such as:

* **MultiTenancy:** Ensuring that every customer's data and operations are completely separate and secure.  
* **Scale:** Handling massive volumes of transactions efficiently.  
* **Security and Latency:** Keeping everything fast and extremely secure.  
* **Service Continuity:** Making sure your automated processes never stop working, even if there is a problem, so that every critical business task is always completed.

\---

**Q6: What's the most powerful, often overlooked capability of Relay?**

Your integration with Cashfree no longer ends with simple webhook notifications. Now, Relay can communicate with and automate processes across all your other business systems. The best part? You can build these sophisticated integrations yourself using Relay, our mcp (platform), and the pre-built skills, all without writing a single line of code. This means you save time because you don't have to deploy or maintain any custom code.  
