import math

class MyClass:
  pass

a = MyClass()
b = MyClass()

print (a)
print (b)

# You can set all atributes with dot notation

a.x = 1
a.y = 2

print (a.x)
print (a.y)

class Point:
    def reset(self):
        self.x = 0
        self.y = 0
p = Point()
p.reset()
#this should print 0 0
print (p.x, p.y)

p1 = Point()
Point.reset(p1)
#this should print 0 0
print (p1.x, p1.x)


#import math

class Pointer:
    def __init__(self, x, y):
        self.move(x,y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0, 0)
    def calculateDistance(self, otherPoint):
        return math.sqrt(
                         (self.x - otherPoint.x)**2 +
                         (self.y - otherPoint.y)**2
                        )
# Make two pointer objects
pointer1 = Pointer(0,0)
pointer2 = Pointer(0,0)
# Pointer1 initialized with 0,0
pointer1.reset()
# Pointer2 initialized with 5,0
pointer2.move(5,0)
distanceP1ToP2 = pointer1.calculateDistance(pointer2)
distanceP2ToP1 = pointer2.calculateDistance(pointer1)
print (distanceP2ToP1)
print (distanceP1ToP2)
assert (distanceP1ToP2 == distanceP2ToP1)

class SecretString:
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
    def decrypt(self, pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return '>.<'

secretString = SecretString("ACME: Top Secret", "qwerty")
print (secretString.decrypt("qwerty"))








