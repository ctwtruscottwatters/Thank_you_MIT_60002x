import random
# MIT 6.0002

# Charles Truscott

"""
Use search tree to allocate 750 calories
Taking item: wine: <89, 123>
Take the LB
beer: <90, 154>
pizza: <95, 258>
burger: <100, 354>
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: beer: <90, 154>
Take the LB
pizza: <95, 258>
burger: <100, 354>
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: pizza: <95, 258>
Take the LB
burger: <100, 354>
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Max cost reached, set is
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Neglecting burger: <100, 354>
Max cost reached, set is
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Neglecting fries: <90, 365>
Taking item: cola: <79, 150>
Take the LB

...

...

...
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 50 withoutVal: 10
Is 50 greater than 10 of
apple: <50, 95>
The list of items at this stage of recursive call is:
cola: <79, 150>
withVal: 79 withoutVal: 50
Is 79 greater than 50 of
cola: <79, 150>
Taking fries: <90, 365> and subtracting 365 from the parameter
avail: 231
Take the RB
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: cola: <79, 150>
Take the LB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 156
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 351
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 251
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
Taking cola: <79, 150> and subtracting 150 from the parameter
avail: 446
Take the RB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 306
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 501
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 401
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
The list of items at this stage of recursive call is:
cola: <79, 150>
withVal: 139 withoutVal: 60
Is 139 greater than 60 of
donut: <10, 195>
apple: <50, 95>
cola: <79, 150>
The list of items at this stage of recursive call is:
fries: <90, 365>
withVal: 169 withoutVal: 139
Is 169 greater than 139 of
cola: <79, 150>
fries: <90, 365>
The list of items at this stage of recursive call is:
burger: <100, 354>
withVal: 179 withoutVal: 169
Is 179 greater than 169 of
cola: <79, 150>
burger: <100, 354>
The list of items at this stage of recursive call is:
pizza: <95, 258>
withVal: 224 withoutVal: 179
Is 224 greater than 179 of
apple: <50, 95>
cola: <79, 150>
pizza: <95, 258>
Taking beer: <90, 154> and subtracting 154 from the parameter
avail: 596
Take the RB
pizza: <95, 258>
burger: <100, 354>
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: pizza: <95, 258>
Take the LB
burger: <100, 354>
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: burger: <100, 354>
Take the LB
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Max cost reached, set is
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Neglecting fries: <90, 365>
Max cost reached, set is
apple: <50, 95>
donut: <10, 195>
Neglecting cola: <79, 150>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Max cost reached, set is
Neglecting donut: <10, 195>
Reached the end of a set
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 43
Take the RB
donut: <10, 195>
Max cost reached, set is
Neglecting donut: <10, 195>
Reached the end of a set
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 50 withoutVal: 0
Is 50 greater than 0 of
apple: <50, 95>
Taking burger: <100, 354> and subtracting 354 from the parameter
avail: 138
Take the RB
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: fries: <90, 365>
Take the LB
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Max cost reached, set is
apple: <50, 95>
donut: <10, 195>
Neglecting cola: <79, 150>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Max cost reached, set is
Neglecting donut: <10, 195>
Reached the end of a set
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 32
Take the RB
donut: <10, 195>
Max cost reached, set is
Neglecting donut: <10, 195>
Reached the end of a set
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 50 withoutVal: 0
Is 50 greater than 0 of
apple: <50, 95>
Taking fries: <90, 365> and subtracting 365 from the parameter
avail: 127
Take the RB
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: cola: <79, 150>
Take the LB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 52
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 247
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 147
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
Taking cola: <79, 150> and subtracting 150 from the parameter
avail: 342
Take the RB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 202
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 397
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 297
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
The list of items at this stage of recursive call is:
cola: <79, 150>
withVal: 139 withoutVal: 60
Is 139 greater than 60 of
donut: <10, 195>
apple: <50, 95>
cola: <79, 150>
The list of items at this stage of recursive call is:
fries: <90, 365>
withVal: 140 withoutVal: 139
Is 140 greater than 139 of
apple: <50, 95>
fries: <90, 365>
The list of items at this stage of recursive call is:
burger: <100, 354>
withVal: 150 withoutVal: 140
Is 150 greater than 140 of
apple: <50, 95>
burger: <100, 354>
Taking pizza: <95, 258> and subtracting 258 from the parameter
avail: 492
Take the RB
burger: <100, 354>
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: burger: <100, 354>
Take the LB
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: fries: <90, 365>
Take the LB
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Max cost reached, set is
apple: <50, 95>
donut: <10, 195>
Neglecting cola: <79, 150>
Max cost reached, set is
donut: <10, 195>
Neglecting apple: <50, 95>
Max cost reached, set is
Neglecting donut: <10, 195>
Reached the end of a set
Taking fries: <90, 365> and subtracting 365 from the parameter
avail: 31
Take the RB
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: cola: <79, 150>
Take the LB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Max cost reached, set is
Neglecting donut: <10, 195>
Reached the end of a set
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 151
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 51
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 50 withoutVal: 10
Is 50 greater than 10 of
apple: <50, 95>
Taking cola: <79, 150> and subtracting 150 from the parameter
avail: 246
Take the RB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 106
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 301
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 201
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
The list of items at this stage of recursive call is:
cola: <79, 150>
withVal: 129 withoutVal: 60
Is 129 greater than 60 of
apple: <50, 95>
cola: <79, 150>
The list of items at this stage of recursive call is:
fries: <90, 365>
withVal: 90 withoutVal: 129
Neglecting
apple: <50, 95>
cola: <79, 150>
Taking burger: <100, 354> and subtracting 354 from the parameter
avail: 396
Take the RB
fries: <90, 365>
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: fries: <90, 365>
Take the LB
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: cola: <79, 150>
Take the LB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Max cost reached, set is
Neglecting donut: <10, 195>
Reached the end of a set
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 140
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 40
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 50 withoutVal: 10
Is 50 greater than 10 of
apple: <50, 95>
Taking cola: <79, 150> and subtracting 150 from the parameter
avail: 235
Take the RB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 95
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 290
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 190
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
The list of items at this stage of recursive call is:
cola: <79, 150>
withVal: 129 withoutVal: 60
Is 129 greater than 60 of
apple: <50, 95>
cola: <79, 150>
Taking fries: <90, 365> and subtracting 365 from the parameter
avail: 385
Take the RB
cola: <79, 150>
apple: <50, 95>
donut: <10, 195>
Taking item: cola: <79, 150>
Take the LB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 310
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 505
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 405
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
Taking cola: <79, 150> and subtracting 150 from the parameter
avail: 600
Take the RB
apple: <50, 95>
donut: <10, 195>
Taking item: apple: <50, 95>
Take the LB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 460
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
Taking apple: <50, 95> and subtracting 95 from the parameter
avail: 655
Take the RB
donut: <10, 195>
Taking item: donut: <10, 195>
Take the LB
Reached the end of a set
Taking donut: <10, 195> and subtracting 195 from the parameter
avail: 555
Take the RB
Reached the end of a set
The list of items at this stage of recursive call is:
donut: <10, 195>
withVal: 10 withoutVal: 0
Is 10 greater than 0 of
donut: <10, 195>
The list of items at this stage of recursive call is:
apple: <50, 95>
withVal: 60 withoutVal: 10
Is 60 greater than 10 of
donut: <10, 195>
apple: <50, 95>
The list of items at this stage of recursive call is:
cola: <79, 150>
withVal: 139 withoutVal: 60
Is 139 greater than 60 of
donut: <10, 195>
apple: <50, 95>
cola: <79, 150>
The list of items at this stage of recursive call is:
fries: <90, 365>
withVal: 219 withoutVal: 139
Is 219 greater than 139 of
apple: <50, 95>
cola: <79, 150>
fries: <90, 365>
The list of items at this stage of recursive call is:
burger: <100, 354>
withVal: 229 withoutVal: 219
Is 229 greater than 219 of
apple: <50, 95>
cola: <79, 150>
burger: <100, 354>
The list of items at this stage of recursive call is:
pizza: <95, 258>
withVal: 245 withoutVal: 229
Is 245 greater than 229 of
apple: <50, 95>
burger: <100, 354>
pizza: <95, 258>
The list of items at this stage of recursive call is:
beer: <90, 154>
withVal: 314 withoutVal: 245
Is 314 greater than 245 of
apple: <50, 95>
cola: <79, 150>
pizza: <95, 258>
beer: <90, 154>
The list of items at this stage of recursive call is:
wine: <89, 123>
withVal: 353 withoutVal: 314
Is 353 greater than 314 of
cola: <79, 150>
pizza: <95, 258>
beer: <90, 154>
wine: <89, 123>
Total value of items taken = 353
    cola: <79, 150>
    pizza: <95, 258>
    beer: <90, 154>
    wine: <89, 123>

[Program finished]


"""
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'
                 
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
        print("Reached the end of a set")
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        print("Max cost reached, set is ")
        for q in toConsider[1:]:
        	print(q)
        print("Neglecting {}".format(toConsider[0]))
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        print("Taking item: {}".format(nextItem))
        #Explore left branch
        print('Take the LB ')
        for val in toConsider[1:]:
         	print(val)
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        print("Taking {} and subtracting {} from the parameter".format(nextItem, nextItem.getCost()))
        print("avail: {}".format(avail - nextItem.getCost()))
        #Explore right branch
        print('Take the RB ')
        for val in toConsider[1:]:
        	print(val)
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        L = []
        L.append(nextItem)
        print("The list of items at this stage of recursive call is:\t")
        for x in L:
        	print(x)
        print("withVal: {} withoutVal: {}".format(withVal, withoutVal))
        #Choose better branch
        if withVal > withoutVal:
            print('Is {} greater than {} of'.format(withVal, withoutVal))
            
            result = (withVal, withToTake + (nextItem,),)
            for q in result[1]:
            	print(q)
            
        else:
            result = (withoutVal, withoutToTake)
            print("Neglecting ")
            for q in result[1]:
            	print(q)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

def main():
	names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
	values = [89,90,95,100,90,79,50,10]
	calories = [123,154,258,354,365,150,95,195]
	foods = buildMenu(names, values, calories)
	testMaxVal(foods, 750)
	
if __name__ == "__main__": main()