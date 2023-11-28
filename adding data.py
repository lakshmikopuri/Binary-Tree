class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return 
        if self.key==data:
            return
        if self.key > data:
            if self.lchild:#checking weather its contain left child node present or not
                self.lchild.insert(data)
            else:
                self.lchild=bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=bst(data)
                
            
        
root=bst(10)
l1=[20,34,56]
for i in l1:
    root.insert(i)
