def dick(func):

    def wrapper(n):
        print("Происходит подготовка к сложному говну...")
        result = func(n)
        print(f"Сложное говно призошло... {result}")
        return result

    return wrapper


@dick
def mew(n: int):
    #! очень сложная хуита!!! происходит
    return "🐈" * n


print(mew(5))
