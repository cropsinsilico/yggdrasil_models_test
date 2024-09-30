This repository contains YAML files describing computational models that can be used in `yggdrasil <https://github.com/cropsinsilico/yggdrasil>`_ integration. Models can be submitted via pull request or via `this form <https://yggdrasil-models.onrender.com>`_ (`source code <https://github.com/cropsinsilico/model_submission_form>`_) which will validate entries, format entries as a YAML file, and open a pull request to add it.

Requirements
------------

To be merged, a model YAML must meet the following requirements:

  1. Is a valid YAML file with valid syntax
  2. Obeys the ``model_form.json`` schema that can be downloaded from `here <https://cropsinsilico.github.io/yggdrasil/advanced/schema.html#additional-schemas>`_
  3. Points to a valid commit in a Git repository that

     1. Contains a LICENSE file
     2. Passes a general review to ensure that it does not contain any nefarious code that could pose a security risk

  4. Can be run in isolation as a one-model integration


Validation Tools
----------------

YAML files can be validated locally using the ``yggvalidate --model-submission [YAMLFILE]`` command line interface provided by the `yggdrasil <https://github.com/cropsinsilico/yggdrasil>`_ package. yggdrasil can be installed locally or one of the `yggdrasil Docker containers <https://cropsinsilico.github.io/yggdrasil/docker.html>`_ can be used.
