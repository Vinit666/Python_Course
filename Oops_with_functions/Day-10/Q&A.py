def create_multiplier(factor):
    def multilplier(a):
        return a * factor

    return multilplier


mul = create_multiplier(5)
result = mul(2)
print(result)
