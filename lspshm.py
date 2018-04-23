def create_list():    #  defines the create_list function
	
	return input("Enter list items, seperated by a ','\n > ").split(",")
	
if __name__ == "__main__":    #  when the program is run
	new_list = create_list()    #  create a new list
	print(new_list)

list1=[]
for a in range(0,10):
    a=int(input("Entrer th number: "))
    list1.append(a)
print(list1[::])
try:
    x=int(input("Enter the starting index: "))
    y=int(input("Enter the Ending index: "))
    z=int(input("Enter the jumping values index: "))
    print(list1[x:y:z])
except:
    print("Enter the values correctly")
q=int(input("Enter the index: "))
w=int(input("Enter the another value for index: "))
list1[q]=w
print(list1)