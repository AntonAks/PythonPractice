# Прості типи
string_variable: str = 'Текст'
integer_variable: int = 10234
float_variable: float = 1324.234
boolean_variable: bool = True
bytes_variable: bytes = b'2134'


# Структурні типи
list_variable: list = [1, 2, 3, 4, 'hello', 3.45, True]
tuple_variable: tuple = (1, 2, 3, 'hello', False)
dict_variable: dict = {"k1": 123, "k2": 'value'}
set_variable: set = {1, 2, 3, 4, 'hello', 'world'}

# None
none_variable: None = None


if __name__ == '__main__':

    vars_tuple = (
        string_variable,
        integer_variable,
        float_variable,
        boolean_variable,
        bytes_variable,
        list_variable,
        tuple_variable,
        dict_variable,
        set_variable,
        none_variable
    )

    for i in vars_tuple:
        print(f"type: {type(i)}, value: {i}")
