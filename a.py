class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def compare_arrays(self, array1, array2):
        if len(array1) != len(array2):
            return False
        
        for i in range(len(array1)):
            print(array1[i], array2[i])
            if array1[i] != array2[i]:
                return False

        return True

p = Person("Alice", 25)
# Tạo mảng array1
array1 = [Person("Alice", 25), Person("Bob", 30)]

# Tạo mảng array2
array2 = [Person("Alice", 25), Person("Bob", 30)]

# So sánh hai mảng
if p.compare_arrays(array1, array2):
    print("Hai mảng bằng nhau.")
else:
    print("Hai mảng không bằng nhau.")