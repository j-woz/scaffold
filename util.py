
import re


class Matcher:

    """ Abstract class for use with Grepper """

    def __init__(self, regexp):
        self.regexp  = regexp
        self.pattern = re.compile(self.regexp)

    def match(self, line):
        m = self.pattern.match(line)
        if m is None:
            return None
        self.run(line)

    def run(self, line):
        """ User code should override this """
        pass

    def reset(self):
        """ User code should override this """
        pass


class Grepper:

    def __init__(self, matchers):
        """ matchers: List of Matchers """
        self.matchers = matchers

    def grep(self, filename):
        with open(filename, "r") as fp:
            while True:
                line = fp.readline()
                if len(line) == 0: break
                for matcher in self.matchers:
                    matcher.match(line)

    def reset(self):
        for matcher in self.matchers:
            matcher.reset()
