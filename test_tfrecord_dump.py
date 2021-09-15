from tfrecord.torch.dataset import TFRecordDataset
import pickle
from tqdm import tqdm

tfrecord_path = "part-r-00001.tfr"
index_path = None
dataset = TFRecordDataset(tfrecord_path, index_path)


index = 0
all_items_list = []
for data in tqdm(iter(dataset)):
    all_items = {}
    for k, v in data.items():
        all_items[k] = v

    all_items_list.append(all_items)

    with open(f"part-r/part-r-00001-{index}.pkl", "wb") as f:
        pickle.dump(all_items, f)

    index = index + 1


import pickle

with open("part-r-00001-111.pkl", "rb") as f:
    my_item = pickle.load(f)

for k, v in my_item.items():
    print(k, type(v), v)
