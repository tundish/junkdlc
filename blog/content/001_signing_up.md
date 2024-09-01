title: #1: September
date: 2024-02-24
author: D E Haynes
tags: winograd, flores, fruition
category: Blog
status: published
summary: On Fruition

Conversation for Action
-----------------------

TBD.

![JunkDLCPelican]({static}/img/junkdlc_sketch_headshot.jpg){:style="width:35%;margin:1rem"}

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

