def make_preety(func):
    def inner():
        print("I am decrated by decorator. # this is run in inner func.")
        func()

    return inner


@make_preety
def oridinary():
    print("i am an oridinary func.")


oridinary()
