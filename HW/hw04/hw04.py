HW_SOURCE_FILE = __file__


def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> s1 = [1, 3, 5]
    >>> s2 = [2, 4, 6]
    >>> merge(s1, s2)
    [1, 2, 3, 4, 5, 6]
    >>> s1
    [1, 3, 5]
    >>> s2
    [2, 4, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    >>> merge([2, 3, 4], [2, 4, 6])
    [2, 2, 3, 4, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    # elif lst1[0] == lst2[0]:
    #     [lst1[0], lst2[0]] + merge(lst1[1:], lst2[1:])
    elif lst1[0]< lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

    



def remove_odd_indices(lst, odd):
    """Remove elements of lst that have odd indices. Use recursion!

    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    >>> remove_odd_indices([9, 8, 7, 6, 5, 4, 3], False)
    [8, 6, 4]
    >>> remove_odd_indices([2], False)
    []
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'remove_odd_indices',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if not lst:
        return []
    elif len(lst) == 1:
        if odd:
            return lst
        else:
            return []
    elif len(lst) == 2:
        if odd:
            return [lst[0]]
        else:
            return [lst[1]]
    elif len(lst) == 3:
        if odd:
            return [lst[0], lst[2]]
        else:
            return [lst[1]]
    else:
        if odd:
            return [lst[0]] + remove_odd_indices(lst[2:], odd)
        else:
            return [lst[1]] + remove_odd_indices(lst[3:], not odd)






class SmartFridge:
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Oh no, we need more Mayo!'
    >>> fridgey.add_item('Eggs', 12)
    'I now have 12 Eggs'
    >>> fridgey.use_item('Eggs', 15)
    'Oh no, we need more Eggs!'
    >>> fridgey.add_item('Eggs', 1)
    'I now have 1 Eggs'
    """

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        orgin = self.items.get(item, 0)
        self.items[item] = orgin  + quantity
        a = self.items[item]
        b = item
        return f'I now have {a} {b}'

    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        b = item
        if self.items[item] - quantity < 0:
            self.items[item] = 0
            return f'Oh no, we need more {b}!'
    
        self.items[item] = self.items[item] - quantity
        a = self.items[item]
        b = item
        if self.items[item] > 0:
            return f'I have {a} {b} left'
        else:
            return f'Oh no, we need more {b}!'



class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please update your balance with $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please update your balance with $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    fund = 0

    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.stock = 0
    

    def restock(self, amount):
        self.stock += amount
        return f'Current {self.item} stock: {self.stock}'
        
    def add_funds(self, amount):
        if self.stock == 0:
            return f'Nothing left to vend. Please restock. Here is your ${amount}.'
        VendingMachine.fund += amount
        return f'Current balance: ${VendingMachine.fund}'

    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        else:
            if VendingMachine.fund < self.price:
                x = self.price - VendingMachine.fund
                return f'Please update your balance with ${x} more funds.'
            elif VendingMachine.fund == self.price:
                VendingMachine.fund = 0
                self.stock -= 1
                return f'Here is your {self.item}.'
            else:
                x = VendingMachine.fund - self.price
                self.stock -= 1
                VendingMachine.fund = 0
                return f'Here is your {self.item} and ${x} change.'

     




        
