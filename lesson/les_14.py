import timeit

mn = {3.5, "hello", (1, 2, 3), 100, 100, 100}
print(mn)
print(
    type(mn)
)  # <class 'set'>  set - არალაგებული, უნიკალური ელემენტების კოლექცია მეორენაირად

mn_1 = set("hello")
print(mn_1)

mn_2 = {i for i in range(10) if i % 2 == 0}
print(mn_2)


print("------------------")

mn_3 = {"a", "b", "c", "d", 34, 82}
mn_3.add(100)
print(mn_3)
mn_3.update(
    [200, 300, 400]
)  # რამდენიმე ელემენტის დამატება, ასევე შეიძლება სხვა კოლექციების დამატება
print(mn_3)
mn_3.remove(34)
print(mn_3)
mn_3.pop()  # განუსაზღვრელი ელემენტის წაშლა
print(mn_3)
mn_3.discard(82)  # ელემენტის წაშლა, თუ არ არსებობს, არ გამოიტანს შეცდომას
print(mn_3)

mn_4 = mn_3.copy()  # კოპირება
print(id(mn_3))
print(id(mn_4))
print(len(mn_3))
print("b" in mn_3)
mn_3.clear()  # ყველა ელემენტის წაშლა
print(mn_3)
del mn_3  # ცვლის წაშლა
# print(mn_3)  # NameError: name 'mn_3' is
print("------------------")
nums_set = {5, 2, 9, 1, 5, 6}
print(nums_set)
print(sorted(nums_set))


print("------------------")

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
result_union = set_1.union(set_2)  # გაერთიანება
print(result_union)
result_union = set_1 | set_2  # გაერთიანება სხვა სინტაქსით
print(result_union)
result_union = set_1 & set_2  # თანაკვეთა
print(result_union)
result_union = set_1 - set_2  # სხვაობა
print(result_union)

result_union = set_1 ^ set_2  # სიმეტრიული სხვაობა
result_union = set_1.symmetric_difference(set_2)  # სიმეტრიული სხვაობა სხვა სინტაქსით
print(result_union)


print("------------------")

a = {1, 2, 3, 4}
b = {3, 4}

print(a.issubset(b))  # a-ს ყველა ელემენტი შედის b-ში?
print(b.issubset(a))  # b-ს ყველა ელემენტი შედის a-ში?
print(a.issuperset(b))  # a-ს ყველა ელემენტი შედის b

c = frozenset(a)  # frozenset - უცვლელი (immutable) ნაკრები, რომელიც არ შეიძლება შეიცვალოს
#c.add(5)  # შეცდომა, რადგან frozenset არ შეიძლება შეიცვალოს