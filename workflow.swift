
import io;
import python;
import string;

import search_matcher;

// Number of initial random strings
start_count  = 1000;
// Length of initial strings
start_length = 3;
// The string to find
global const string target = "jus";
// Maximal number of recursive calls to work()
global const int max_levels = 20;

// Get the initial strings
s0 = start_random(target, start_count, start_length);
string items0[] = split(s0, ";");
// Report initial strings
foreach item in items0
{
  printf(item);
}

/** The main recursive work function */
work(string sm, int level)
{
  // Get new strings from the Python API
  s1 = decide(target, sm);
  if (s1 == "FOUND")
  {
    // We found it- we're done
    printf("FOUND: level=%i");
  }
  else if (level == max_levels)
  {
    // Too much recursion- give up
    printf("EXPIRED");
  }
  else
  {
    // Recurse and work on each new string
    string items1[] = split(s1, ";");
    foreach item1 in items1
    {
      printf("new: (%i) %s" % (level, item1));
      // Each call runs concurrently
      work(sm, level+1);
    }
  }
}

// Start workflow by working on all initial strings
// Each call runs concurrently
foreach item in items0
{
  work(item, 0);
}
