This repository contains YAML files describing computational models that can be used in `yggdrasil <https://github.com/cropsinsilico/yggdrasil>`_ integration. Models can be submitted via pull request or via `this form <https://yggdrasil-models.herokuapp.com>`_ (`source code <https://github.com/cropsinsilico/model_submission_form>`_) which will validate entries, format entries as a YAML file, and open a pull request to add it.

Requirements
------------

To be merged, a model YAML must meet the following requirements:

  1. Is a valid YAML file with valid syntax
  2. Obeys `this JSON schema <https://github.com/cropsinsilico/model_submission_form/blob/main/static/model.json>`_
  3. Points to a valid GitHub repository that
     1. Contains a LICENSE file
     2. Passes a general inspection to ensure that it does not contain any nefarious code that could pose a security risk
  4. Can be run in isolation as a one-model integration

Validation Tools
----------------

The ``utils/validate.py`` script can be used to validate YAML files locally; `yggdrasil <https://github.com/cropsinsilico/yggdrasil>`_ must be installed or one of the `yggdrasil Docker containers <https://cropsinsilico.github.io/yggdrasil/docker.html>`_ can be used.
