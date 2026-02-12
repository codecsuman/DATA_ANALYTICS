a = ("oneplus","nokia","readme")
print("before conversion", type(a))


a = list(a)
print("ater conversion", type(a))
a.append("vivo")
print(a)
a= tuple(a)
print(type(a))
print(a)