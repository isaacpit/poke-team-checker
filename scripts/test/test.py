import sys
import json

class Test:

  my_count = 0
  BASE_SAVE_PATH = './mobs/heros/'

  def __init__(self, name_arg):
    self.name = name_arg
    self.attack="a"
    self.defense="b"
    self.speed="c"
    Test.my_count += 1
    print('there are {0} objects'.format(Test.my_count))

  @staticmethod
  def staticMethod():
    # print("static method: ", self.name)
    # print("in static method: ", i)
    print("in static method")

  def classMethod(self, atk_damage):
    print("classMethod: ", self)
    print("classMethod name :", self.name, atk_damage)

  def saveHero(self, attack, defense, speed):
    my_path = Test.BASE_SAVE_PATH + self.name + ".data"
    print(my_path)
    print("saving to my path: ", my_path) 
    # f = open()

  def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


a_isaac = Test("the name")
print(a_isaac)
a_isaac.toJSON()
# print("THIS SHOULD PRINT")
f=open("test.data", 'w')
f.write(a_isaac.toJSON())