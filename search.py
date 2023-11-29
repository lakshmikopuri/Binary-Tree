    def search(self, data):
        if self.key == data:
            print("node is found")
            return
        if self.key > data:
            if self.lchaild:
                self.lchild.search(data)
            else:
                print("node is not present in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present in tree")
