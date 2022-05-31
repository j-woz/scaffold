
from collections import deque

from search_matcher import SearchMatcher


start  = 100
length = 5
target = "justin"

Q = deque()

for i in range(0, start):
    Q.append(SearchMatcher(target, None, None, length))
print(Q)

max_tries = 10*1000*1000
tries = 0

success = False
while True:

    print(len(Q))
    try:
        current = Q.popleft()
    except IndexError:
        break
    if tries == max_tries:
        break
    new = current.decide()
    if new == SearchMatcher.FOUND:
        success = True
        break
    Q.extend(new)
    tries += 1

# print(Q)
print("queue:")
L = sorted(Q)
for item in L:
    print(item)
print("length: %i" % len(Q))
print("result: " + str(success))
