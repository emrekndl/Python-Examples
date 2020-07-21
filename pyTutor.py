class Selam(object):
    def __init__(self, isim):
        self.isim = isim

    def merhaba(self, yuksek=False):
        if yuksek:
            print(f"MERHABA {self.isim.upper()}")
        else:
            print(f"Merhaba {self.isim}")


s = Selam("arch")
s.merhaba()
s.merhaba(yuksek=True)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


print(quicksort([3, 6, 8, 10, 1, 2, 1]))


s = "hello"
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l', '(ell)'))
print(' world '.strip())

nums = list(range(5))
print(nums)
print(nums[2:4])

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))


def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'
    for x in [-1, 0, 1]:
        print(sign(x))

