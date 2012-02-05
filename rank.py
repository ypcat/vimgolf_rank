#!/usr/bin/python

from BeautifulSoup import BeautifulSoup

ch = {}
for c in BeautifulSoup(open('all.html').read()).findAll('h5'):
    ch[c.a['href'].split('/')[-1]] = c.text.split()[-2]

def rank1(u):
    return sum(int(u[c] if c in u else e) for c, e in ch.items())

def rank2(u):
    return sum(int(ch[c])-int(u[c]) for c in u.keys())

o1=o2=0
print 'rank handle            rank1  rank2'
for i, u in enumerate(BeautifulSoup(open('top100.html').read()).findAll('h6')[1:]):
    handle = u.text.split('@')[-1]
    user = {}
    for c in BeautifulSoup(open('top100/'+handle).read()).findAll('h5'):
        if c.b:
            user[c.a['href'].split('/')[-1]] = c.b.text.split('/')[0]
    r1, r2 = rank1(user), rank2(user)
    print '%4d %-16s %6d %6d %6d %6d %6d' % (i+1, handle, r1, r2, r1+r2, r1-o1, r2-o2)
    o1, o2 = r1, r2

