from BaseDispatcher import BaseDispatcher


class Collection(BaseDispatcher):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if (cls.__instance is None):
            cls.__instance = super(Collection, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self, cfg):
        pass

    def __del__(self):
        pass

    def save(self, agentWorker):
        agentWorker.Host
        agentWorker.Guest
        pass