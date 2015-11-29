===============================
Charlesbot Jira plugin
===============================

.. image:: https://img.shields.io/travis/marvinpinto/charlesbot-jira/master.svg?style=flat-square
    :target: https://travis-ci.org/marvinpinto/charlesbot-jira
    :alt: Travis CI
.. image:: https://img.shields.io/coveralls/marvinpinto/charlesbot-jira/master.svg?style=flat-square
    :target: https://coveralls.io/github/marvinpinto/charlesbot-jira?branch=master
    :alt: Code Coverage
.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
    :target: LICENSE.txt
    :alt: Software License

A Charlesbot__ plugin that interacts with Jira and does some cool shit.

__ https://github.com/marvinpinto/charlesbot


How does this work
------------------

Whenever a person types something in chat that looks like a Jira ticket, this
plugin grabs a bunch of information about that ticket and prints it in chat.

.. image:: https://raw.githubusercontent.com/marvinpinto/charlesbot-jira/master/images/jira.png


Installation
------------

.. code:: bash

    pip install charlesbot-jira

Instructions for how to run Charlesbot are over at https://github.com/marvinpinto/charlesbot!


Configuration
-------------

In your Charlesbot ``config.yaml``, enable this plugin by adding the following
entry to the ``main`` section:

.. code:: yaml

    main:
      enabled_plugins:
        - 'charlesbot_jira.jira.Jira'

Then add a ``jira`` dictionary block that looks something like:

.. code:: yaml

    jira:
      base_url: 'https://jira.atlassian.com'


Sample config file
~~~~~~~~~~~~~~~~~~

.. code:: yaml

    main:
      slackbot_token: 'xoxb-1234'
      enabled_plugins:
        - 'charlesbot_jira.jira.Jira'

    jira:
      base_url: 'https://jira.atlassian.com'

License
-------
See the LICENSE.txt__ file for license rights and limitations (MIT).

__ ./LICENSE.txt
