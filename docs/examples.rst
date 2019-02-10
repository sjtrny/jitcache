.. _examples:

Examples
===================

Basic Usage
--------------------------------------

.. literalinclude:: ../examples/simple.py
   :linenos:
   :caption: examples/simple.py

Output::

    Slow Function Called
    40


Usage with Threads
--------------------------------------

.. literalinclude:: ../examples/threads.py
   :linenos:
   :caption: examples/threads.py

Output::

    Slow Function Called
    Slow Function Called
    [40, 40, 40, 40, 40, 120, 120, 120, 120, 120]

Usage with Processes
--------------------------------------

.. literalinclude:: ../examples/process.py
   :linenos:
   :caption: examples/process.py

Output::

    Slow Function Called
    40


