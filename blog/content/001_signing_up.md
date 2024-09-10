title: #1: Getting Things Done
date: 2024-02-24
author: D E Haynes
tags: winograd, flores, fruition
category: Blog
status: published
summary: On Fruition

Flores and Winograd
===================

The Chilean Minister of Finance and a Stanford Professor of Artificial Intelligence walk into a bar.

They down a few Rum cocktails and recognize that they share an appreciation of Phenomenology.
So they raise their glasses to Hans-Georg Gadamer. They salute the hermeneutics of Martin Heidegger.
Then against a glorious Pacific sunset, the two men sling some horseshoes and conclude that there is no stable
representation of reality.

Language is action. Interpretation depends on what is present at hand.

Eventually they write a book called *Understanding Computers and Cognition*.
The copy I have is the third printing, from 1988. It's an excellent read, and much of it remains relevant to this
very day.

Conversation for Action
=======================

The fifth chapter of the book explores Language as protocol for shared Activity. It presents a state machine that describes the
conversation between two parties who are collaborating on a task of work.


![JunkDLCPelican]({static}/img/UCAC_fig5-1.png){:style="width:96%;margin:1rem"}

The protagonists are labelled *A* and *B*.
The states are numbered. The terminal nodes are drawn slightly darker than the internal states of the diagram.

It begins with A making a request of B. B can reject it, promise to do it, or negotiate the terms of the request.

The action progresses as a conversation. Each transition is achieved by a piece of Speech.
The ideal outcome is to reach state 5, but there are various paths that terminate elsewhere.

Modifications
=============

Now I've seen a lot of state diagrams in my time, but few so generally applicable as this one.

It appeals to me as a template for writing screenplay.
I think it might serve very well in constructing branching trees of dialogue, such as you find in role-playing games.

As I experiment with it, a couple of issues arise which tempt me to extend the original idea.

Indirection
-----------

It's the custom in Computer Science to give the protagonists names such as *Alice* and *Boris*.
Sometimes in the field of Security Engineering there's another character too, *Colin*, who is usually trying to interrupt and spoil everything.

I prefer to separate the names of the characters from the roles they play.
So I think of the *Head* and the *Hand* as being the initiating and the responding party respectively.

My characters *Alice* and *Boris* (and *Colin* too if necessary) play the roles of Head and Hand, but are not bound to them.
Some activities actually negotiate these roles on the fly, and so I find the extra level of indirection to be important.

If Boris misunderstands what's expected of him, can he ask Colin for help? Can Colin step in and take his place?
Does Alice trust Colin? Does Boris now owe Colin a favour? And so on.

Composition
-----------

Imagine the dialogue around making a pot of tea. There are many actions to perform.
You've got to find the cups, fill the kettle, and that's before all the questions about *how* people prefer
their tea.

So the top-level action spawns others. Some of them may be performed concurrently, but many depend on the outcome of a
previous action.
Some can be tried again; with others it's the end of the whole process if they fail.

I'm starting to think there's a difference between an Action and an Activity. The word *Action* feels spontaneous and
bounded in time, whereas an *Activity* takes longer. Perhaps it's the repetition of an Action until it succeeds.

Fruition of Action
==================

Here's my update to the original diagram. I call this variant *Fruition of Action*.

![Fruition of Action]({static}/img/fruition.png){:style="width:96%;margin:1rem"}

I've given each state a name. The happy path for the action consists of:

+ Inception
+ Elaboration
+ Construction
+ Evaluation
+ Completion

The Discussion state represents the negotiation between parties prior to Construction.
The action may terminate sub-optimally in states Withdrawn, Defaulted or Cancelled.

I renamed some of the transitions so they are specific to the role which
performs them. This disambiguates the negotiation phase between Elaboration and Discussion.
An *offer* comes from the Hand, and the Head makes the corresponding *clarification*.

The arrowheads are different in each case. The Head transitions have triangular points, whereas those
of the Hand are rounded and open.

Here is the full state table, including participle names for the transitions:

| When          | Role  | Participle    | Event         | Then          |
|---------------|-------|---------------|---------------|---------------|
| Inception     | Head  | proposing     | proposal      | Elaboration   |
| Elaboration   | Head  | withdrawing   | withdrawal    | Withdrawn     |
| Elaboration   | Hand  | declining     | disinclination| Withdrawn     |
| Elaboration   | Hand  | promising     | promise       | Construction  |
| Elaboration   | Hand  | offering      | offer         | Discussion    |
| Discussion    | Head  | clarifying    | clarification | Elaboration   |
| Discussion    | Head  | confirming    | confirmation  | Construction  |
| Discussion    | Head  | withdrawing   | withdrawal    | Withdrawn     |
| Discussion    | Hand  | declining     | disinclination| Withdrawn     |
| Construction  | Hand  | disavowing    | disavowal     | Defaulted     |
| Construction  | Head  | cancelling    | cancellation  | Cancelled     |
| Construction  | Hand  | delivering    | delivery      | Evaluation    |
| Evaluation    | Head  | refusing      | refusal       | Construction  |
| Evaluation    | Head  | cancelling    | cancellation  | Cancelled     |
| Evaluation    | Head  | adopting      | adoption      | Completion    |

Examples
========

Modelling social situations requires some thought. It's not about who's doing what.
The key is to understand the contracts woven by their Speech Acts.

Commission of Action
--------------------

> ALICE: (proposing)
> Stick the kettle on, would you?
>
> BORIS: (offering)
> Tea or Coffee?
>
> ALICE: (clarifying)
> Tea please.
>
> BORIS: (promising)
> Righto.

It is very clear what's required here. Alice, the Head, wants tea and Boris as the Hand will make it.

Of course there's a chance Boris might be disinclined:

> ALICE (proposing):
> Stick the kettle on, would you?
>
> BORIS (declining):
> No time, sorry. I'm just about to leave for my train.

And Alice has been known to change her mind:

> ALICE (proposing):
> Stick the kettle on, would you?
>
> BORIS (promising):
> OK.
>
> ALICE (cancelling):
> Do you know what, I think I'll have a bath first. I'll be back down in half an hour.

Invitation to Action
--------------------

What if Alice goes down to the Kitchen and finds Boris there:

> ALICE: (proposing)
> Tea?
>
> BORIS: (promising)
> Sure.

Alice (Head) has announced she's making tea. Boris (Hand) has promised if she does he'll drink a cup. They are in the Construction
state of that agreement.

Now another action is born:

> ALICE (proposing):
> Can you get the mugs for me?

> BORIS: (offering)
> Mugs or cups?
>
> ALICE: (clarifying)
> My big blue mug.
>
> BORIS: (offering)
> It's in the sink. I'll give it a rinse.

> ALICE: (confirming)
> Thank you.
>

Misunderstandings and conflicts arise from time to time. As they do here:

> ALICE (proposing):
> Can you get the mugs for me?

> BORIS (offering):
> My phone's ringing, I'll get them in a second.

His words lack conviction. It's a weak offer which might equally be interpreted as disinclination.
Even if he means to make a promise, Boris might not be able to meet Alice's expectations for timeliness.
What happens next?

Would it change Boris' intentions if he spots the illocutionary nod from Alice?

> ALICE (confirming): .

How long will it be before we hear this:

> ALICE (cancelling):
> Oh forget it, I'll get them myself.

Conclusion
==========

When you start to use this system of writing, it doesn't take long for the terminology to become second nature.
I'm finding it a great way of annotating my dialogue.

If you want a hard copy of the Fruition diagram, this
[PDF version]({static}/doc/fruition_of_action.pdf){:target="_blank"} is convenient for printing.

