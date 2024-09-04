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

Social
======

1
-

Head (proposing):
: > Stick the kettle on, would you?

Hand (declining):
: > No time, sorry. I'm just about to leave for my train.

2
-

Head (proposing):
: > Stick the kettle on, would you?

Hand (suggesting):
: > Tea or Coffee?

Head (confirming):
: > Tea, please.

3
-

Head (proposing):
: > Stick the kettle on, would you?

Hand (promising):
: > OK.

Head (abandoning):
: > Do you know what, I think I'll have a bath first. I'll be back down in half an hour.

Kit
===

Conflict
--------

BETH (proposing):
: > Can you get the mugs for me?

ALAN (promising or declining?):
: > My phone's ringing, I'll get them in a second.

His promise lacks conviction. It's a weak enough statement to constitute declining. What happens next?

BETH (countering):
: > Don't worry, I'll do it.

Have they agreed that Beth will get the mugs from the cupboard? There is social value in Alan being involved in the
making of the tea. Perhaps he'd like therefore to be the Hand that does it.

Alan can still be considered the Hand of the Activity which is in Construction.
Beth, with more urgency, has countered his ambiguous Suggestion/Disinclination with a clarification.

Activities are composable. In the Construction state especially, One Activity can create another.
(Also synch!)
Are there two Activities now, or one? I'd say two. Beth is performing a second activity which synchronises with Alan's.
If he she takes the mugs from the cupboard before he does, she will force him to acknowledge he won't complete
the task (Disavowal).

Brew
----
