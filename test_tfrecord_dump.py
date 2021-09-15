from tfrecord.torch.dataset import TFRecordDataset
import pickle
from tqdm import tqdm

tfrecord_path = "part-r-00001.tfr"
index_path = None
dataset = TFRecordDataset(tfrecord_path, index_path)


all_items_list = []
for data in tqdm(iter(dataset)):
    all_items = {}
    for k, v in data.items():
        all_items[k] = v

    all_items_list.append(all_items)

with open(f"part-r/part-r-00001.pkl", "wb") as f:
    pickle.dump(all_items_list, f)


# 测试读取
with open("part-r-00001.pkl", "rb") as f:
    my_item_list = pickle.load(f)

for k, v in my_item_list[0].items():
    print(k, type(v), v)
