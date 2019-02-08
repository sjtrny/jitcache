# jitcache

jitcache is a just-in-time key-value cache that is thread/process safe. jitcache also prevents repeated computation
when multiple workers request the same value.

jitcache was designed to improve the performance of Plot.ly Dash apps by caching results and reducing CPU load.
 