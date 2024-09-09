title: #1: Getting Things Done
date: 2024-02-24
author: D E Haynes
tags: winograd, flores, fruition
category: Blog
status: published
summary: On Fruition

Flores and Winograd
-------------------

The Chilean Minister of Finance and a Stanford Professor of Artificial Intelligence walk into a bar.

They down a few Rum cocktails and begin to recognize a shared appreciation of Phenomenology.
They raise their glasses to Hans-Georg Gadamer. They toast the hermeneutics of Martin Heidegger.
Then against a glorious Pacific sunset, the two men sling some horseshoes and conclude that there is no stable
representation of reality.

Language is action. Interpretation depends on what is present at hand.

Eventually they write a book, *Understanding Computers and Cognition*.
The copy I have is the third printing, from 1988. It's a very interesting read, and most of it remains relevant to this
day.

In Chapter 5,

![JunkDLCPelican]({static}/img/UCAC_fig5-1.png){:style="width:96%;margin:1rem"}

```python
class Fruition(State, enum.Enum):
    """
    Adapted from 'Understanding Computers and Cognition'
    by Terry Winograd and Fernando Flores,
    fig 5.1: The basic conversation for action.

    """

    inception = 1
    elaboration = 2
    construction = 3
    transition = 4
    evaluation = 4
    completion = 5
    discussion = 6
    defaulted = 7
    withdrawn = 8
    cancelled = 9
```

[RUP lifecycle](https://en.wikipedia.org/wiki/Rational_unified_process#Four_project_life-cycle_phases)

![Fruition of Action]({static}/img/fruition.png){:style="width:96%;margin:1rem"}

Introduce 'head' and 'hand'. Explain renaming of arcs.

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

propose
:   inception -> elaboration

[Fruition of Action]({static}/doc/fruition_of_action.pdf){:target="_blank"}

Structuralism vs Phenomenology

Composability
=============

ALICE (proposing):
: > Stick the kettle on, would you?

BORIS (suggesting):
: > Tea or Coffee?

ALICE (confirming):
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

BORIS (suggesting):
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

Ambiguity
---------

ALICE (proposing):
: > Can you get the mugs for me?

BORIS (suggesting?):
: > My phone's ringing, I'll get them in a second.

His words lack conviction. It's a weak enough statement to constitute Disinclination.
Even if it's meant as a Promise, it might not meet Alice's expectations for timeliness.
What happens next?

ALICE (confirming):
: > Don't worry, I'll do it.

Have they agreed that Alice will get the mugs from the cupboard?
She is about to take the role of the Hand for this Activity.
But it seems to me that Barry is still involved somehow, like a sort of sleeping partner.
I wonder if he now owes Alice a favour?

We risk going down some fascinating rabbit holes which sadly, like Barry, I don't
currently have time for.
