
# name = input("Name: ")
# department = input("Course: ")
# level = int(input("level: "))

# print(f"{name}, {department}, {level}")

def main():
    form()

def form():
    name = input("Name: ")
    department = input("Course: ")
    level = int(input("level: "))
    print(f"Name:{name}\nDepartment:{department}\n{level} level")

main()