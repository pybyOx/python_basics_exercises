def singleton(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if not instance:
            instance['instance'] = cls(*args, **kwargs)
        return instance['instance']
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
