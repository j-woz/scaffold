
import io;
import python;
import string;

import search_matcher;

start_count  = 10;
start_length = 5;
target = "justin";

s = start_random(target, start_count, start_length);
string items[] = split(s, ";");
foreach item in items
{
  printf(item);
}
