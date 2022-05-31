
import re
import sys

from util import Grepper, Matcher


class Stats(Matcher):

    regexp = "decide|expand-accept|shrink-accept|prune|FOUND"

    def __init__(self):
        super(Stats, self).__init__(Stats.regexp)
        self.count = 0
        self.pattern = re.compile(Stats.regexp)
        self.counts = { "decide": 0,
                        "expand-accept": 0,
                        "shrink-accept": 0,
                        "prune" : 0 }
        self.found = False

    def run(self, line):
        m = self.pattern.match(line)
        if m == "FOUND":
            self.found = True
        else:
            self.counts[m.group(0)] += 1


stats = Stats()
grepper = Grepper([stats])
grepper.grep(sys.argv[1])
for key in stats.counts.keys():
    print("%s = %s" % (key, stats.counts[key]))
print("found: " + str(stats.found))
