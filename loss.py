# %%

import numpy as np
import pandas as pd
# %%


def weighted_loss_func(p, dataset_path):
    dataset = pd.read_csv(dataset_path)

    def loss():
        pass


# %%
dataset_path = 'dataset/train.csv'
dataset = pd.read_csv(dataset_path)

# %%
dataset.groupby('label').count().

# %%
