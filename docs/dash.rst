.. _dash:

Plot.ly Dash Example
======================

Dash's design often causes many callbacks to depend on the same value. This leads to the threads/processes that are
handling the callback to perform the same computation. By using jitcache's KVStore we can prevent this wasteful effort.

.. literalinclude:: ../dash_example/app.py
   :linenos:
   :lines: 3-
   :caption: ../dash_example/app.py
