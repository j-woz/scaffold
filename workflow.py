
from collections import deque

from search_matcher import SearchMatcher


# Number of random strings to bootstrap the search
start_count  = 100
# Length of start strings
start_length = 5
# The string we are trying to find
target = "justin"

# List of SearchMatchers.  The work to do.
Q = deque()

# Create the initial strings
for i in range(0, start_count):
    Q.append(SearchMatcher(target, None, None, start_length))
print(Q)

# Max number of strings to evaluate before giving up
max_tries = 1*1000*1000
# Number of tries so far
tries = 0

# Did we find the target?
success = False
while True:

    print(len(Q))
    try:
        current = Q.popleft()
    except IndexError:
        break
    if tries == max_tries:
        break
    # new: List of new SearchMatchers
    new = current.decide()
    if new == SearchMatcher.FOUND:
        success = True
        break
    # Add new candidate strings:
    Q.extend(new)
    tries += 1

# print(Q)
# Dump the remaining Q in order of score:
print("queue:")
L = sorted(Q)
for item in L:
    print(item)
print("length: %i" % len(Q))
print("result: " + str(success))
