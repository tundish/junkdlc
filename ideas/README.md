Running WhisperX offline
========================

* `pip install whisperx` to venv using python 3.12
* Edit *~py3.12-util/lib/python3.12/site-packages/torch/serialization.py* (~1465) to set `weights_only` False
* `~/py3.12-util/bin/whisperx --compute_type int8 ~/Music/data/240915_1706.mp3`
