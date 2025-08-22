class MyDict(dict):
    def get(self, __key):
        if __key not in self:
            return 0


# my_dict = MyDict()
# print(my_dict.get('wtf'))
