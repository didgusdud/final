import math

class Point:
    __x=0
    __y=0

    def __init__(self,a,b):
        self.x=a
        self.y=b
    
    def distance(self,other):
        dist=math.sqrt(((other.x-self.x)*(other.x-self.x))+(other.y-self.y)*(other.y-self.y))
        return dist
    
    def __add__(self,other):
        self.x=self.x+other.x
        self.y=self.y+other.y
        print("{0:s} : ({1:d},{2:d})".format("p1+p2",self.x,self.y))


def main():
    p1 = Point(1,1)
    p2 = Point(2,2)
    dista=p1.distance(p2)
    print("{0:s} : {1:.5f}".format("distance",dista))
    p=p1+p2
    

if __name__ == "__main__":
    main()
