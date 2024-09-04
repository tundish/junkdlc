title: #1: Fruition of Activity
date: 2024-02-24
author: D E Haynes
tags: winograd, flores, fruition
category: Blog
status: published
summary: On Fruition

Winograd and Flores
-------------------

1988.

TBD.

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
    completion = 5
    discussion = 6
    defaulted = 7
    withdrawn = 8
    cancelled = 9
```

[RUP lifecycle](https://en.wikipedia.org/wiki/Rational_unified_process#Four_project_life-cycle_phases)

Introduce 'head' and 'hand'. Explain renaming of arcs.

| When          | Role  | Participle    | Event         | Then          |
|---------------|-------|---------------|---------------|---------------|
| Inception     | Head  | proposing     | Proposal      | Elaboration   |
| Elaboration   | Head  | abandoning    | Abandonment   | Withdrawn     |
| Elaboration   | Hand  | declining     | Disinclination| Withdrawn     |
| Elaboration   | Hand  | promising     | Promise       | Construction  |
| Elaboration   | Hand  | suggesting    | Suggestion    | Discussion    |
| Discussion    | Head  | countering    | Counter       | Elaboration   |
| Discussion    | Head  | confirming    | Confirmation  | Construction  |
| Discussion    | Head  | abandoning    | Abandonment   | Withdrawn     |
| Discussion    | Hand  | declining     | Disinclination| Withdrawn     |
| Construction  | Hand  | disavowing    | Disavowal     | Defaulted     |
| Construction  | Head  | abandoning    | Abandonment   | Cancelled     |
| Construction  | Hand  | delivering    | Delivery      | Transition    |
| Transition    | Head  | condemning    | Condemnation  | Construction  |
| Transition    | Head  | abandoning    | Abandonment   | Cancelled     |
| Transition    | Head  | declaring     | Declaration   | Completion    |

propose
:   inception -> elaboration

[Fruition of Action]({static}/doc/fruition_of_action.pdf){:target="_blank"}

Structuralism vs Phenomenology

Composability
=============

ALICE (proposing):
: > Stick the kettle on, would you?

BARRY (suggesting):
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

BARRY (declining):
: > No time, sorry. I'm just about to leave for my train.

2
-

ALICE (proposing):
: > Stick the kettle on, would you?

BARRY (suggesting):
: > Tea or Coffee?

ALICE (confirming):
: > Tea, please.

3
-

ALICE (proposing):
: > Stick the kettle on, would you?

BARRY (promising):
: > OK.

ALICE (abandoning):
: > Do you know what, I think I'll have a bath first. I'll be back down in half an hour.

Kit
===

Conflict
--------

BARRY (proposing):
: > Can you get the mugs for me?

ALICE (promising or declining?):
: > My phone's ringing, I'll get them in a second.

Her promise lacks conviction. It's a weak enough statement to constitute declining. What happens next?

BARRY (countering):
: > Don't worry, I'll do it.

Have they agreed that Barry will get the mugs from the cupboard?
There is value for Alice in being involved in the making of the tea.
Perhaps she'd like therefore to be the Hand that does it.

Alice can still be considered the Hand of the Activity which is in Construction.
Barry, with more urgency, has countered her ambiguous Suggestion/Disinclination with a clarification.

If he she takes the mugs from the cupboard before he does, she will force him to acknowledge he won't complete
the task (Disavowal).

Brew
----
