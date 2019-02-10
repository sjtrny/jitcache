.. jitcache documentation master file, created by
   sphinx-quickstart on Fri Feb  8 14:01:53 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

jitcache
====================================

jitcache is a just-in-time key-value cache that is thread/process safe. jitcache also prevents repeated computation
when multiple workers request the same value.

jitcache was designed to improve the performance of Plot.ly Dash apps by caching results and reducing CPU load.

Installation
-------------------

Install via pip::

    $ pip install jitcache

Documentation
-------------------

Examples and specific information on classes and methods are below.

.. toctree::
   :maxdepth: 2

   dash
   examples
   api

Basic Usage
-------------------

.. literalinclude:: ../examples/simple.py
   :linenos:
   :caption: examples/simple.py


Plot.ly Dash Usage
-------------------

.. literalinclude:: ../examples_dash/callback_memoize/app.py
   :linenos:
   :caption: examples_dash/callback_memoize/app.py


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`