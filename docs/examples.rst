.. _examples:

Examples
===================

Basic Usage
--------------------------------------

Notice that ``slow_fn`` is only called once, despite two requests.

.. literalinclude:: ../examples/cache_simple.py
   :linenos:
   :lines: 3-
   :caption: examples/cache_simple.py

Output::

    Slow Function Called
    40
    40

Initialise with an existing dictionary
--------------------------------------

.. literalinclude:: ../examples/cache_initialise.py
   :linenos:
   :lines: 3-
   :caption: examples/cache_initialise.py

Output::

    Slow Function Called
    Same object
    20
    20

Insert a single value into the store
--------------------------------------

.. literalinclude:: ../examples/cache_set.py
   :linenos:
   :lines: 3-
   :caption: examples/cache_set.py

Output::

    Start
    Slow Function Called
    Value inserted
    40

Usage with Threads
--------------------------------------

.. literalinclude:: ../examples/cache_threads.py
   :linenos:
   :lines: 3-
   :caption: examples/cache_threads.py

Output::

    Slow Function Called
    Slow Function Called
    [40, 40, 40, 40, 40, 120, 120, 120, 120, 120]

Usage with Processes
--------------------------------------

.. literalinclude:: ../examples/cache_process.py
   :linenos:
   :lines: 3-
   :caption: examples/cache_process.py

Output::

    Slow Function Called
    40


