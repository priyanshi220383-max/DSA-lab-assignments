#Experimant-1  Stack ADT (Design + Use)
# Stack ADT implementation using Python list.
# Supports basic operations: push, pop, peek, isEmpty, size, and display.
# Push and Pop operations work in O(1) time.
class StackADT:
    def __init__(self):
        self.data = []  
    def push(self, x):
        self.data.append(x)
    def pop(self):
        if self.is_empty():
            return None  
        return self.data.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]
    def is_empty(self):
        return len(self.data) == 0
    def size(self):
        return len(self.data)
    def display(self):
        return self.data
def main():
    st = StackADT()
    while True:
        print("\n--- STACK ADT MENU ---")

        # printing menu options
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Size")
        print("6. Display Stack")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            val = input("Enter value to push: ")
            st.push(val)
            print("Pushed:", val)
        elif choice == "2":
            removed = st.pop()
            if removed is None:
                print("Underflow! Stack is empty, cannot pop.")
            else:
                print("Popped:", removed)
        elif choice == "3":
            top = st.peek()
            if top is None:
                print("Stack is empty, nothing to peek.")
            else:
                print("Top element:", top)
        elif choice == "4":
            print("isEmpty:", st.is_empty())
        elif choice == "5":
            print("Size:", st.size())
        elif choice == "6":
            print("Stack (bottom -> top):", st.display())
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":

    # calling main() to start the program
    main()