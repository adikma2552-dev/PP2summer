def total(*args):
    print(sum(args))

total(1, 2, 3, 4)


def show_subjects(*subjects):
    for subject in subjects:
        print(subject)

show_subjects("Math", "Python", "English")


def student_info(**kwargs):
    print(kwargs)

student_info(name="Adlet", age=19, university="KBTU")


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Adlet", city="Almaty")