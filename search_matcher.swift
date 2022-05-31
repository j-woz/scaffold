
(string o) start_random(string target, int start, int length)
{
  o = python_persist(
----
from search_matcher import SearchMatcher
target = "%s"
start  =  %i
length =  %i
L = []  # List of strings
for i in range(0, start):
    L.append(str(SearchMatcher(target, None, None, length)))
result = ";".join(L)
---- % (target, start, length),
"result");
}

(string o) decide(string target, string candidate)
{
  o = python_persist(
----
from search_matcher import SearchMatcher
target    = "%s"
candidate = "%s"
sm = SearchMatcher.parse(target, candidate)
new = sm.decide()
if new == SearchMatcher.FOUND:
    result = "FOUND"
else:
    L = [ str(sm) for sm in new ]
    result = ";".join(L)
---- % (target, candidate),
"result");
}
