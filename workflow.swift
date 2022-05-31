
import io;
import python;
import string;

import search_matcher;

start_count  = 10;
start_length = 5;
target = "justin";
max_levels = 3;

s0 = start_random(target, start_count, start_length);
string items[] = split(s0, ";");
foreach item in items
{
  printf(item);
}

foreach item in items
{
  s1 = decide(target, item);
  printf(s1);
}
