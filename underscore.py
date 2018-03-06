class Underscore(object):
    def map(self, list, fun):
        new_list = []
        for i in list:
            new_list.append(fun(i))
        return new_list
    def reduce(self, list, fun, *memo):
        result = list[0]
        start = 1
        if len(memo) > 0:
            result = memo[0]
            start = 0
        for i in range(start, len(list)):
            result = fun(result, list[i])
        return result
    def find(self, list, predicate):
        for i in list:
            if predicate(i):
                return i
        return None
    def filter(self, list, predicate):
        result = []
        for i in list:
            if predicate(i):
                result.append(i)
        return result
    def reject(self, list, predicate):
        return self.filter(list, lambda x: not predicate(x))
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print odds
# should return [2, 4, 6] after you finish implementing the code above
