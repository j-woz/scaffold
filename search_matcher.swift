
(string o) start_random(string target, int start, int length)
{
  o = python_persist(
----
from search_matcher import SearchMatcher
target = '%s'
start  =  %i
length =  %i
L = []  # List of strings
for i in range(0, start):
    L.append(str(SearchMatcher(target, None, None, length)))
result = ";".join(L)
---- % (target, start, length),
"result");
}