from BaseAgentWorker import BaseAgentWorker
import os


class fake1(BaseAgentWorker):
    #Host = None
    counter = 0
    # def __init__(self, filename):
    #     self.Host = filename
    __Content = None

    def update(self):
        self.Priority = self.INFO

        self.Timestamp = self.time()
        self.counter +=1
        try:
            file = open(os.path.join('/home/ilab/Public/0' , self.Guest), 'r')
            content = file.readlines()
            file.close()

            self.Message = {'counter' : self.counter, 'action': 'facke', 'content' : content}

            if (content != self.__Content):
                if (self.__Content is not None):
                    self.Priority = self.ERROR
                    self.Message['addition_message'] =  "I'm be changed!!!!!!!"

                self.__Content = content

        except:
            self.Priority = self.ERROR
            self.Message = {'counter' : self.counter, 'action': 'facke', 'content' : "I'm hung!"}
            self.exit()
