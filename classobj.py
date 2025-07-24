class AREA:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    # method to calculate area
    def area(self):
        return self.length * self.width
        
    
l=float(input("Enter length: "))
w=float(input("Enter width: "))   
obj = AREA(l,w)
print("Area of rectangle is: ",obj.area())