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

   examples
   api

Example Usage
-------------------

Notice that ``slow_fn`` is only called once, despite two requests.

.. literalinclude:: ../examples/cache_simple.py
   :linenos:
   :lines: 3-
   :caption: examples/cache_simple.py

Output::

    Slow Function Called
    40
    40

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`