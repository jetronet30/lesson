from copy import deepcopy

progs = ['Python', 'Java', 'C++']

progs.append('JavaScript')
print(progs)

progs.insert(1, 'C#')
print(progs)

numbers = [1, 2, 3, 4, 5]
progs.extend(numbers)
print(progs)


progs.remove('C#')
print(progs)
progs.insert( progs.__len__(), 'C#')

print(progs)

progs.pop(3)
print(progs)
del progs[0]
print(progs)

print(progs.index('C#'))

progs.clear()
print(progs)
print('--------------------------')

boys = ['tom', 'airton', "masrter",[1, 2, 3]]

copy_boys = boys.copy()

print(id(boys))
print(id(copy_boys))

print(boys)
print(copy_boys)

copy_boys[3][0] = 100
print(boys)
print(copy_boys)

copy_boys[2] = 'born'
print(boys)
print(copy_boys)


print('--------------------------')
# deep copy
deep_copy_boys = deepcopy(boys)
print(id(deep_copy_boys))
print(id(boys))

#sort

names = ['Tom', 'Bob', 'Sam']

names.sort()
print(names)

names.sort(reverse=True)
print(names)

print('--------------------------')

nums = [1, -5, 3, -2, 4]
nums.sort(key=abs)
print(nums)
print(len(nums))
print(sorted(nums, key=abs))
numsPos = [i for i in range(1000)]
print(sum(numsPos))
