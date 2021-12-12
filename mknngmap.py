import glob
import json
import re

def stmt2origfile(stmt, filenames):
    for fn in filenames:
        with open(fn, 'r') as fp:
            if stmt in fp.read():
                return fn

def origfilename2worldlevel(filename):
    (w, l) = re.findall(r'\d+', filename)
    return {'world': int(w), 'level': int(l)}

with open('nngsave.json', 'r') as nngsave_fp:
    levels = json.load(nngsave_fp)['data']

origfilenames = glob.glob('world*/level*.lean')

nngmap = {}
for level in levels:
    stmt = level['lean']
    origfilename = stmt2origfile(stmt, origfilenames)
    nngmap[stmt] = origfilename2worldlevel(origfilename)

with open('nngmap.json', 'w', encoding='utf8') as nngmap_fp:
    json.dump(nngmap, nngmap_fp, ensure_ascii=False)
