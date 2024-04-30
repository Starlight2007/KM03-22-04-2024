def add(x,y):
    return x+y
a=add(4,5)
print(a)

def add_to_list (x):
    list_1 =[1,2,3,4]
    list_1.append(x)
    return list_1
a=add_to_list(5)
print(a)

def add_to_list (x):
    list_1=[{"name":"Kanat","last_name":"Erbol","Age":20 }, 
   {"name":"Askar","last_name":"Erzhanov","Age":15},
   {"name":"Kairat","last_name":"Zhandosov","Age":45}
   ]
    list_1.append(x)
    return list_1
print(add_to_list({"name":"jonbek","last_name":"Erbolat","Age":17}))