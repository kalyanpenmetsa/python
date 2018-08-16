import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class drawPie:
    def openFile(self,logPath):
        self.logPath = logPath
        f = open(logPath)
        return f.read()

    def drawPie(self,explode,labelList,sizeList,autoPct='%1.1f%%',shadow=True,startAngle='90'):
        self.explode = explode
        self.labelList = labelList
        self.sizeList = sizeList
        self.autoPct = autoPct
        self.shadow = shadow
        self.startAngle = startAngle

        if len(labelList) == len(sizeList):
            fig1, ax1 = plt.subplots()
            ax1.pie(sizeList, explode=explode, labels=labelList, autopct=autoPct, shadow=shadow, startangle=90)
            ax1.axis('equal')
            return plt.show()
        else:
            print("len(labelList) not equal to len(sizeList)")
            print(pie.openFile('error.log'))

#pie.drawPie(logPath,explodeList,labelList,sizeList)
pie.drawPie([0,0,0,0],['Info','Access','Warning','Error'],[1,2,3,4])

# print(np.arange(3))


class drawBar:
    def drawBar(self,xList,yList):
        self.xList = xList
        self.yList = yList
        if len(xList) == len(yList):
            plt.bar(xList,yList)
            plt.show()
        else:
            print("len(xList) not equal to len(yList)")

pie = drawPie()
bar = drawBar()
bar.drawBar([0,1,2],[1,2,4])
print(bar.yList)
