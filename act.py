import re

class Act:
    @staticmethod
    def parseAct(raw):
        dayAndStage = raw.find('span', {'class': 'right txtTiny'}).contents[0]
        day = dayAndStage.split(", ")[0]
        stage = dayAndStage.split(", ")[1]
        status = raw.find('a').find('span', {'class': re.compile("stat*")}).contents[0]
        name = raw.find('a').contents[1][1:]
        if (name == ""):
            name = raw.find('a').find('span', {'class': re.compile("lu_new*")}).contents[0]
        return Act(name, stage, day, status)

    def __init__(self, name, stage, day, status):
        self.name = name
        self.stage = stage
        self.day = day
        self.status = status
        
    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.stage, self.day, self.status)