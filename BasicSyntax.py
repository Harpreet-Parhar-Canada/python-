# x = 5;
# print(x)
# y = "hello world"
# print(y)
#
# i = input("Enter the value")
# val =int(i)
# if type(val) == int:
#     print("Integer")
# else:
#     print("Something Complex")   
#
# print("All Done")
# arryList =["Ian","Marcela","Harpreet"]
# j = input("Enter the position:")
# value = int(j)
# arryList.insert(value,"Harleen")
# print(arryList)          
#
# print("Deletion")
# k = input("Enter postion for deletion ")
# value1= int(k)
# print(arryList[value1])
# element=arryList[value1]
# arryList.remove(element)
# print(arryList);

# print("Updation")
# k = input("Enter postion for Updation: ")
# value1= int(k)
# elemt = input("Enter element:")
# arryList[value1] = elemt;
# print(arryList[value1])
# print(arryList);

def personage():
    age = 18;
    if age>=18:
                print("person can vote")
    else:
                print("person cannot vote")
personage()

def email(parameter1,parameter2):
    element1 = parameter1;
    element2 = parameter2;
    element3 = "@evolveu.com"
    element4 =  element1+"."+element2+element3;
    return element4;

print(email("Larry","Shumlich"))
print(email("Heiko","Peters"))

dictionaryExample = {
"name":"Harpreet",
"age": 20,
}
print(dictionaryExample)
x = dictionaryExample.get("name")
print(x)

counter = 1
while counter <=10:
    print(counter)
    counter+=1
