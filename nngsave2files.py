import json
import sys
import pathlib

# command-line args
try:
    nngsavefilename = sys.argv[1]
except IndexError:
    print('Usage:')
    print('{} SAVEGAME'.format(sys.argv[0]))
    sys.exit(1)

# load nngmap
with open('nngmap.json', 'r') as nngmap_fp:
    nngmap = json.load(nngmap_fp)

# load worldnames
worldnames = {}
worldnames[1]  = 'tutorial'
worldnames[2]  = 'addition'
worldnames[3]  = 'multiplication'
worldnames[4]  = 'power'
worldnames[5]  = 'function'
worldnames[6]  = 'proposition'
worldnames[7]  = 'advanced-proposition'
worldnames[8]  = 'advanced-addition'
worldnames[9]  = 'advanced-multiplication'
worldnames[10] = 'inequality'

# load levels
with open(nngsavefilename, 'r') as nngsave_fp:
    levels = json.load(nngsave_fp)['data']

#### helper functions

def w2wdir(w, human=True):
    if human:
        return '{}-{}'.format(w, worldnames[w])
    else:
        return 'world{}'.format(w)

def l2lfile(w, l, human=True):
    if human:
        return '{}-{}.lean'.format(w, l)
    else:
        return 'level{}.lean'.format(l)

def levelextract(level, human=True):
    # get: statement, world, level, text
    s = level['lean']
    w = nngmap[s]['world']
    l = nngmap[s]['level']
    t = level['editorText']
    # format world dir and level file
    wdir = w2wdir(w, human)
    lfile = l2lfile(w, l, human)
    # create world dir if needed
    pathlib.Path('{}'.format(wdir)).mkdir(parents=True, exist_ok=True)
    # write level file in world dir
    with open('{}/{}'.format(wdir,lfile), 'w') as fp:
        fp.write(t)

#### main loop

for level in levels:
    if level.get('isSolved'):
        levelextract(level)

