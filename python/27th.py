a = "harry potter "
print(a.endswith("p"))
print(a.startswith("h"))


b= "  **** ....,,,,, haryy potter "
print(b)
print(a.strip(". * ,"))


c = " ****#####WWWMMMMCCCQQQ!!"
print(a.split('#'))



d ="harry potter "
x = d.rjust(20)
print(x,"is my fav movie")


e ="my name is suman"
print(e.replace("suman", "suvo"))



##the  position index

f = "harry potter is my favourit movie "
print(f.rindex("potter"))
print(f.rindex("harry"))