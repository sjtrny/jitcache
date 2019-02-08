from cache import ThingStoreJIT
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from utils.cluster import aaw_occ_cluster

aaw = pd.read_csv("../data/AAW_clean.csv")

kwargs = {
    'data': aaw,
    'n_clusters': 57,
    'direction': "up",
}

store = ThingStoreJIT()

n_jobs = 10
n_threads = 2

executor = ThreadPoolExecutor(max_workers=n_threads)

future_list = []
result_list = []

for i in range(n_jobs):
    f = executor.submit(store.get_value, aaw_occ_cluster, kwargs)
    future_list.append(f)

for f in future_list:
    result_list.append(f.result())


