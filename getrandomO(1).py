import random
class RandomizedSet:#[1,2,4,6,7,3]
    def __init__(self):
        self.list = []
        self.dict = {}
    def insert(self,val):
        if val in self.dict:
            return False
        else:
            self.list = self.list + [val]
            self.dict[val] = self.list[len(self.list)]
        return True
    def remove(self,val):
        if val not in self.dict:
            return False
        indexofremovingelement = self.dict[val]

        self.list[-1] = self.list[indexofremovingelement]
        self.list = self.list[0:len(self.list)-1]
        del self.dict[val]
        return True

    def getRandom(self):
        return random.choice(self.list)


    
obj = RandomizedSet()
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())

        
# 🛠 Required Functionalities:
# insert(val: int) -> bool
# Insert a value into the set.

# If the value is not already present, insert it and return True.

# If the value already exists, return False.

# remove(val: int) -> bool
# Remove a value from the set.

# If the value exists, remove it and return True.

# If the value does not exist, return False.

# getRandom() -> int
# Return a random element from the current set.

# Each element must have the same probability of being returned.

# It's guaranteed that there will be at least one element in the set when this function is called.

# list = [1,2]
# list = list - [2]
# print (list)