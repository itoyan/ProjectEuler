# -*- encoding: utf-8 -*-

import math

f = open('base_exp99.txt', 'r')
dic = {}
for num, line in enumerate(f):
    base, exp = map(int, line.split(','))
    # enumerateは0から始まるので行数にするときは足しておく
    dic[num+1] = math.log10(base) * exp

max_value = max(dic.values())
# 最大値にほぼ等しいものが複数あったときのための
# 対策のため、リストとして最大値のある行を求めている
print [key for key, value in dic.iteritems()
       if abs(dic[key] - max_value) < 10**-10]

