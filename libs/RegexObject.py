import re
import json

class BaseRegexObject:
    '''
    compile a regex for best performance
    '''
    _container = None

    def __init__(self, regex):
        self._container = re.compile(regex)

    def match(self, content):
        return self._container.match(content)

    def search(self, content, group=1):
        return self._container.search(content).group(group)

    getString = search

    def getInt(self, content, group=1):
        return int(self.search(content, group))

    def getFloat(self, content, group=1):
        return float(self.search(content, group))

    def getJson(self, content, group=1):
        result = self.search(content, group)
        return json.loads(result)


class CLIStatus(BaseRegexObject):
    def __init__(self, label, column=1):
        regex = label
        for i in range(0, column):
            regex += r'\W+'
            if i == column - 1:
                regex += r'(\w+)'
            else:
                regex += r'\w+'

        self._container = re.compile(regex)
