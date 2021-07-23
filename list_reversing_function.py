def list_rev_fun(n):
    class stack:
        def __init__(self):
            self.__stack_list = []
        
        def push(self,val):
            self.__stack_list.append((val))
        
        def pop(self):
            value = self.__stack_list[-1]
            del self.__stack_list[-1]
            return value
    

    stack_object = stack()
    stack_object_1 = stack()

    for i in range(n):
        i = input("entre a element of the list: ")
        stack_object.push(i)
    print(stack_object._stack__stack_list)    
        

    for i in range(n):
        stack_object_1.push(stack_object.pop())

    print(stack_object_1._stack__stack_list)


n = int(input("entre a number of element that you want to add:"))
list_rev_fun(n)

