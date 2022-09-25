class FlatIterator:

    def __init__(self,list_):
        self.end = len(list_) - 1
        self.main_list = list_      

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = -1
        return self  
        
    def __next__(self):
        if self.main_list_cursor <= self.end and self.nested_list_cursor == (len(self.main_list[self.main_list_cursor])-1):
            self.main_list_cursor += 1
            self.nested_list_cursor = -1
        if self.main_list_cursor > self.end:
            raise StopIteration  
        if self.nested_list_cursor < len(self.main_list[self.main_list_cursor]):
            self.nested_list_cursor+=1
        return self.main_list[self.main_list_cursor][self.nested_list_cursor]

nested_list = [ ['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

flat_list = []
FlatIter =  FlatIterator(nested_list)
for item in FlatIter:
    flat_list.append(item)
    print(item)
print(flat_list)
     
     

 
    
    
