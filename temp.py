# a = [10, 20, 30]
# print(id(a))
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))

# # a[2] = a[2] + 1
# a[2] += 1
# print(id(a))
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))


# b = [10, 20, [30, 40]]
# print(id(b))
# print(id((b[0])))
# print(id(b[1]))
# print(id(b[2]))

# # b[2] = b[2] + 50
# b[2] += [50]
# print(id(b))
# print(id((b[0])))
# print(id(b[1]))
# print(id(b[2]))

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[::-2])

