__author__ = 'timyu'
d = {'a':1, 'b':2, 'c':3}
print d
for key in d:
    print key
print '--------'
print d
for value in d.itervalues():
    print value
print '--------'
print d
for k,v in d.iteritems():
    print k,'--',v

print '========'
for ch in 'ABC':
    print ch

for i, value in enumerate(['A','b','c']):
    print i ,value

