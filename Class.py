class car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedLimit=speedLimit
    def start(self):
        print('started')
audi=car('A6','red','Audi',100)
print(audi.start())


