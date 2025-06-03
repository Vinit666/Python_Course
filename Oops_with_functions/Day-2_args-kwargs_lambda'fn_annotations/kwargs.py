def sum_of(**kwargs):
    print(kwargs)  # gives output in dict.[str,any..]


sum_of(
    name="vinit", age=21, gender="male"
)  # output-->{'name': 'vinit', 'age': 21, 'gender': 'male'}


def check_of(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


check_of(
    name="vinit", age=21, gender="male"
)  # output-->{'name': 'vinit', 'age': 21, 'gender': 'male'}
