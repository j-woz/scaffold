
import io;
import python;
import string;

import search_matcher;

start_count  = 1000;
start_length = 3;
global const string target = "jus";
global const int max_levels = 20;

s0 = start_random(target, start_count, start_length);
string items0[] = split(s0, ";");
foreach item in items0
{
  printf(item);
}

work(string sm, int level)
{
  s1 = decide(target, sm);
  if (s1 == "FOUND")
  {
    printf("FOUND: level=%i");
  }
  else if (level == max_levels)
  {
    printf("EXPIRED");
  }
  else
  {
    string items1[] = split(s1, ";");
    foreach item1 in items1
    {
      printf("new: (%i) %s" % (level, item1));
      work(sm, level+1);
    }
  }
}

foreach item in items0
{
  work(item, 0);
}
