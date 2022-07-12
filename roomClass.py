class room:
    def __init__(self, number, info, price, status, time=None):
        self.number = number
        self.info = info
        self.price = price
        self.status = status
        if(time!=None):
            #*use datetime to implement date subtraction to check if reservation has expired
            self.time = time
        else:
            self.time = None
    def changeStatus(self,status):
        self.status = status
    def changeTime(self,time):
        self.time = time
    def checkNum(self):
        return self.number
    def checkStatus(self):
        return self.status
    def checkTime(self):
        return self.time

    def printInfo(self, printAll=False):
        if(printAll == True):
            if(self.status!='VACANT'):
                print("UNAVAILABLE",end=" ")
            print(self.number, '-', *self.info, "$"+self.price+'/night',self.status, self.time, sep=" ")
        else:
            if((self.status=='VACANT')):
                print(self.number, '-', *self.info, "$"+self.price+'/night', sep=" ")


    