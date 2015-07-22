from mrjob.job import MRJob
from collections import defaultdict

class TrimmerCount(MRJob):
    def mapper(self, _, doc):
        c = defaultdict(int)
        for w in [doc[i:i+3] for i in xrange(len(doc) - 2)]:
            c[w] += 1

        for w, c in c.items():
            yield w, c

    def reducer(self, key, cs):
        yield key, sum(cs)

wc = TrimmerCount()
wc.run()
