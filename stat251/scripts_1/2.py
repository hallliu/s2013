#!/usr/bin/python2
# Script that actually counts how many ways there are for a matching to exist

import itertools

def image(a_list_of_tuples):
    img_rpt=itertools.chain(*a_list_of_tuples)
    return set(img_rpt)

combos = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]

nocount=0
for (a,b,c,d) in itertools.product (combos, repeat=4):
    if len(image([a,b,c,d])) < 4:
        nocount=nocount+1
        continue
    if len(image([a,b,c])) < 3:
        nocount=nocount+1
        continue
    if len(image([a,b,d])) < 3:
        nocount=nocount+1
        continue
    if len(image([a,c,d])) < 3:
        nocount=nocount+1
        continue
    if len(image([b,c,d])) < 3:
        nocount=nocount+1
        continue
print nocount
