
import difflib
import math
import random

#


class SearchMatcher:

    FOUND = 1000

    def __init__(self, target, value=None, score=None, length=None):
        self.target = target
        if value is None:
            self.value = SearchMatcher.random_value(length)
        else:
            self.value = value
        if score is None:
            self.score = self.compute_score(self.target, self.value)
        else:
            self.score = score

    def __str__(self):
        return "'%s'=%0.3f" % (self.value, self.score)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.score < other.score

    def assign(self, value, score):
        self.value = value
        self.score = score

    def random_value(n):
        L = []
        for i in range(0, n):
            L.append(SearchMatcher.random_character())
        return "".join(L)

    def random_character():
        """Generate a random lower-case alphabet character"""
        return chr(random.choice(range(ord('a'), ord('z')+1)))

    def expand(self, value):
        c = SearchMatcher.random_character()
        L = list(value)
        i = random.randint(0, len(L))
        L.insert(i, c)
        return "".join(L)

    def shrink(self, value):
        if len(value) == 0:
            return ""
        L = list(value)
        i = random.randint(0, len(L)-1)
        del(L[i])
        return "".join(L)

    def prune(self):
        print("pruned! '%s'" % self.value)
        pass

    def decide(self):
        print("")
        print("decide: " + str(self))
        results = []

        if self.target == self.value:
            return SearchMatcher.FOUND

        bigger  = self.expand(self.value)
        score_bigger = self.compute_score(self.target, bigger)
        new = SearchMatcher(self.target, bigger, score_bigger)
        print("expand: " + str(new))
        if self.step(score_bigger):
            results.append(new)

        smaller = self.shrink(self.value)
        score_smaller = self.compute_score(self.target, smaller)
        new = SearchMatcher(self.target, smaller, score_smaller)
        print("shrink: " + str(new))
        if self.step(score_smaller):
            results.append(new)

        if self.value == "":
            self.prune()
        elif random.random()/2 < 1 - self.score:
            self.prune()
        else:
            results.append(self)

        return results

    def compute_score(self, value1, value2):
        L = sorted([value1, value2])
        score = difflib.SequenceMatcher(None, *L).ratio()
        return score

    def step(self, score):
        if score > self.score:
            return True
        if score == 0:
            return random.random() < 0.5
        diff = self.score - score
        print("diff: %0.3f" % diff)
        if diff > 0.3:
            return False
        x = (1 - math.sqrt(diff)*4)
        print("func: %0.3f" % x)
        if random.random() < x/4:
            print("explore: %0.3f" % diff)
            return True
        return False
