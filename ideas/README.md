Principles
==========

* Path from text to music

Workflow
========

* Terminal tabs Ctrl-t
* vim .
* vimrc
* :Ex
* :terminal

Netrw Basics
============

* % New file
* x Display, eg: firefox
* p Preview
* mf/MF
* md (diff)
* mx/mX

Formats
=======

1. .txt
2. .rst
3. .md

Windows techniques
==================

* GVim for big text settings
* Win + up for Maximize
* Use clipboard to speed text entry

Running WhisperX offline
========================

* `pip install whisperx` to venv using python 3.12
* Edit *~py3.12-util/lib/python3.12/site-packages/torch/serialization.py* (~1465) to set `weights_only` False
* `~/py3.12-util/bin/whisperx --compute_type int8 ~/Music/data/240915_1706.mp3`
