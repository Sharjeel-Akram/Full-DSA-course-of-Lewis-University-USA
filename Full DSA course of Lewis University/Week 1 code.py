# P-1.36: write a Python program that inputs a list of words, separated by whitespace, 
# and outputs how many times each word appears in the list. You need not worry about efficiency at this point, 
# however, as this topic is something that will be addressed later in this book.


String = input('Enter words:  ')
words=String.split(' ')

word_list = set(words)
word_count={}
for word in word_list:
    if word != '':
        word_count[word]=words.count(word)

print(word_count)



# P-2.39: for class hierarchy, in order to keep math of calculating area and perimeter, 
# you don't need to implement all sub-class shapes, it is enough to implement, 
# Square, Rectangle and Triangle (with right angle). 

print("\nP-2.39: for class hierarchy, in order to keep math of calculating area and perimeter, you don't need to implement all sub-class shapes, it is enough to implement, Square, Rectangle and Triangle (with right angle). \n")
import math
class Polygon:
    def getArea(self):
        pass;
  
    def get_attributes(self):
        pass;

class Right_Triangle(Polygon):
    def __init__(self,height,width):
        self.width=width;
        self.height=height;
  
    def getArea(self):
        return 0.5*self.width*self.height;
  
    def get_attributes(self):
        return self.width+self.height+(math.sqrt((self.width*self.width)+(self.height*self.height)));
   
class Square(Polygon):
    def __init__(self,side):
        self.side=side;
  
    def getArea(self):
        return self.side*self.side;
  
    def get_attributes(self):
        return 4*self.side;

class Rectangle(Polygon):
    def __init__(self,length,breadth):
        self.length=length;
        self.breadth=breadth;
  
    def getArea(self):
        return self.length*self.breadth;
  
    def get_attributes(self):
        return 2*(self.length+self.breadth);

print("Right_Triangle");
rt=Right_Triangle(2,3);
print("Area: "+str(rt.getArea()));
print("Perimeter: "+str(rt.get_attributes()));
s=Square(7);
print("Square");
print("Area: "+str(s.getArea()));
print("Perimeter: "+str(s.get_attributes()));
print("Rectangle");
r=Rectangle(23,12);
print("Area: "+str(r.getArea()));
print("Perimeter: "+str(r.get_attributes()));

