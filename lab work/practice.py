queue=[]
def insert():
    item = int(input("Enter a item :"))
    queue.append(item)
    print(item,"inserted into queue")
def delete():
    if len(queue)==0:
        print("the queue is empty,cannot delete")
    else:
        removed_item = queue.pop(0)
        print("element removed", removed_item)
def traversal():
    if len(queue)==0:
        print("The queue is empty")
    else:
        print("Queue elements are:")
        for elemets in queue:
            print(elemets)

while True:
    print("\n Queue Operations")
    print("1. Insert")
    print("2. delete")
    print("3. traversal")
    print("4. Exit")
    choice = int(input("Enter your choice :"))

    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        traversal()
    elif choice == 4:
        print("Exiting Programe")
        break
    else:
        print("invalid choice, please try again")
# queue = []

# def insert():
#     item = int(input("Enter an item: "))
#     queue.append(item)
#     print(item, "inserted into queue")

# def delete():
#     if len(queue) == 0:
#         print("The queue is empty, cannot delete")
#     else:
#         removed_item = queue.pop(0)
#         print("Element removed:", removed_item)

# def traversal():
#     if len(queue) == 0:
#         print("The queue is empty")
#     else:
#         print("Queue elements are:")
#         for element in queue:
#             print(element)

# while True:
#     print("\nQueue Operations")
#     print("1. Insert")
#     print("2. Delete")
#     print("3. Traversal")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         insert()
#     elif choice == 2:
#         delete()
#     elif choice == 3:
#         traversal()
#     elif choice == 4:
#         print("Exiting Program")
#         break
#     else:
#         print("Invalid choice, please try again")