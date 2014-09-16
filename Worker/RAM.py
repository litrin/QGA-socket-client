from BaseAgentWorker import BaseQGAAgentWorker
from libs.RegexObject import CLIStatus


class Swap(BaseQGAAgentWorker):

    _reg_compile = {}

    def __init__(self, host, filename=None):
        super(Swap, self).__init__(host, filename)

        self._reg_compile = {
            'total': CLIStatus(r'SwapTotal:'),
            'free': CLIStatus(r'SwapFree:')
        }


    def update(self):
        self.Timestamp = self.time()

        self.Message = {'action': 'LoadAvg'}
        swapUsage = self.get_swap_usage()

        if swapUsage is not None:
            self.Message['content'] = swapUsage

            if (swapUsage['total'] * 0.2 < swapUsage['free']):
                self.Priority = self.ERROR
                self.Message['content']['message'] = 'No more swap left'

        else:
            self.Priority = self.ERROR
            self.Message['content'] = "pipe broken!"

            self.exit()

    def get_swap_usage(self):
        try:
            content = self.fetch('/proc/meminfo')

            return {'total': self._reg_compile['total'].getInt(content),
                    'free': self._reg_compile['free'].getInt(content)}
        except:
            return None
