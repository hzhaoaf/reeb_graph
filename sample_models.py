#sample 100个模型，每个选择5个尺寸，一共500个文件，跑一版效果看看

import os
import random
import re

id_filename = 'unique_ids.txt'
lines = open(id_filename, 'r').readlines()
ids = [l.strip() for l in lines]
sample_ids = set(random.sample(ids, 100))

sid2filename = {}
vrml_dir = 'poc_vrml'

for num, filename in enumerate(os.listdir(vrml_dir)):
    if 'wrl' not in filename:
        continue
    part = re.search('gb\d+', filename, re.IGNORECASE)
    if not part:
        continue
    if part[0] in sample_ids:
        sid2filename.setdefault(part[0], []).append(filename)

sampled_files = set()
for sid, filename_list in sid2filename.items():
    k = 2 if len(filename_list) >= 2 else len(filename_list)
    sampled_filenames = random.sample(filename_list, k)
    sampled_mrgs = [r.replace('wrl', 'mrg') for r in sampled_filenames]
    [sampled_files.add(r) for r in sampled_filenames + sampled_mrgs ]

wfilename = '200_sampled_file.txt'
w = open(wfilename, 'w+')
w.write('\n'.join(sampled_files))
w.close()
