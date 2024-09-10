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

Eventually they write a book, *Understanding Computers and Cognition*.
The copy I have is the third printing, from 1988. It's an excellent read, and much of it remains relevant to this
very day.

Conversation for Action
=======================

The fifth chapter of the book explores Language as protocol for shared Activity. It presents a state machine which describes the
conversation between two parties who are collaborating on a task of work.


![JunkDLCPelican]({static}/img/UCAC_fig5-1.png){:style="width:96%;margin:1rem"}

The protagonists are labelled *A* and *B*.
The states are numbered. The terminal nodes are drawn slightly darker than the internal states of the diagram.

It begins with A making a request of B. B can reject it, promise to do it, or negotiate the terms of the request.

The action progresses as a conversation. Each transition is achieved by a piece of Speech.
The ideal outcome is to reach state 5, but there are various ways that things can go wrong. 

Modifications
=============

Now, I've seen a lot of state diagrams in my time, but few so generally applicable as this one.

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

Composability
-------------

Imagine the dialogue around making tea. There are many actions to perform.
You've got to find the cups, fill the kettle, and that's before all the questions about *how* people prefer
their tea.

So the top-level action spawns others. Some of them may be performed concurrently, but many depend on the outcome of a
previous action.
Some can be tried again; with others it's the end of the whole process if they fail.

I'm starting to think there's a difference between an Action and an Activity. The word *Action* feels spontaneous and
bounded in time, whereas an *Activity* takes longer. Perhaps it's the repetition of an Action until it succeeds.

Fruition of Action
==================

Here's my update of the original diagram. I call this variant *Fruition of Action*.

![Fruition of Action]({static}/img/fruition.png){:style="width:96%;margin:1rem"}

I've given each state a name. The 'happy path' for the action consists of:

+ Inception
+ Elaboration
+ Construction
+ Evaluation
+ Completion

Also, I renamed some of the transitions so that they are specific to the role which
performs thema. This disambiguates the negotiation phase between Elaboration and Discussion.
An *offer* comes from the Hand, and the Head makes the corresponding *clarification*.

Composability
=============

ALICE (proposing):
: > Stick the kettle on, would you?

BORIS (offering):
: > Tea or Coffee?

ALICE (clarifying):
: > Tea, please.

Each of these may in turn instantiate other activities when necessary.
Activities are composable. In the Construction state especially, One Activity can create another.
(Also synch!)

Two types of activities:

* Collecting materials
* Assembling the product

If two people are involved, the work can take place in two different regions of the activity model.
But in a social context, neither party acts in isolation. There is regular chit-chat and exchange of information.

The different activities proceed concurrently and from time to time synchronize upon each other.

I'm stirring the teapot with a spoon. Are we having sugar? Where is the spoon for the sugar?
I could use this spoon, but I can't put a wet spoon in the sugar.
So I need a tea towel. Or maybe just another spoon.

And so on.

Perspective
===========

Social
======

1
-

ALICE (proposing):
: > Stick the kettle on, would you?

BORIS (declining):
: > No time, sorry. I'm just about to leave for my train.

2
-

ALICE (proposing):
: > Stick the kettle on, would you?

BORIS (offering):
: > Tea or Coffee?

ALICE (confirming):
: > Tea, please.

3
-

ALICE (proposing):
: > Stick the kettle on, would you?

BORIS (promising):
: > OK.

ALICE (abandoning):
: > Do you know what, I think I'll have a bath first. I'll be back down in half an hour.

The Context Horizon
===================

ALICE (proposing):
: > Can you get the mugs for me?

BORIS (offering?):
: > My phone's ringing, I'll get them in a second.

His words lack conviction. It's a weak enough statement to constitute Disinclination.
Even if it's meant as a Promise, it might not meet Alice's expectations for timeliness.
What happens next?

ALICE (clarifying):
: > Don't worry, I'll do it.

Have they agreed that Alice will get the mugs from the cupboard?
She is about to take the role of the Hand for this Activity.
But it seems to me that Boris is still involved somehow, like a sort of sleeping partner.
I wonder if he now owes Alice a favour?

**Abandon this activity and replay it? Memory Horizon?**
Is the purpose of a *Ceremony* to reset the memory?

We risk going down some fascinating rabbit holes which sadly, like Boris, I don't
currently have time for.

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

[Fruition of Action]({static}/doc/fruition_of_action.pdf){:target="_blank"}

