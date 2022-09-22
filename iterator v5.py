class FlatIterator:

    def __init__(self,list_):
        self.start = -1
        self.end = len(list_) - 1
        self.list_ = list_
        self.current_result = []        

    def __next__(self):
        while self.start < self.end :
            self.start += 1
            self.current_result = self.list_[self.start] 
            return self.current_result 
        raise StopIteration
        
    def __iter__(self):        
        return self

nested_list = [ ['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]


FlatIter =  FlatIterator(nested_list)
for item in FlatIter:
    for item2 in FlatIter.current_result:
         print(item2)
     
     

 
    
    
