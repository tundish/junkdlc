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

| When          | Role  | Event         | Then          | Participle    |
|---------------|-------|---------------|---------------|---------------|
| Inception     | Head  | Proposal      | Elaboration   | proposing     |
| Elaboration   | Head  | Abandonment   | Withdrawn     | abandoning    |
| Elaboration   | Hand  | Disinclination| Withdrawn     | declining     |
| Elaboration   |       | disavowal     | Withdrawn     | proposing     |
|               |       | condemnation  |               | condemning    |
|               |       | Disinclination|               | declining     |

propose
:   inception -> elaboration

Structuralism vs Phenomenology

