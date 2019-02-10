.. _dash:

Plot.ly Dash Examples
======================

Dash's design often causes many callbacks to depend on the same value. This leads to the threads/processes that are
handling the callback to perform the same computation. By using jitcache's KVStore we can prevent this wasteful effort.

Configuration
------------------

You must use gunicorn's preload option when using multiple processes to ensure that the KVStore is shared. Otherwise a
KVStore object will be created for each process.

Use the following command to start your server:

    ``gunicorn --preload app:server``

You can find more details here http://docs.gunicorn.org/en/stable/settings.html#preload-app

Callback Memoization
------------------------------------

.. literalinclude:: ../examples_dash/callback_memoize/app.py
   :linenos:
   :caption: examples_dash/callback_memoize/app.py

General Function Memoization
------------------------------------

.. literalinclude:: ../examples_dash/function_memoize/app.py
   :linenos:
   :caption: examples_dash/function_memoize/app.py
