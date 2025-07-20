from integerFunction import IntFunction
from stringFunction import StringFunction

if __name__ == "__main__":
    func_name = input("Which function do you want to work? ")

    input_values = {
       # "rotate": ([1, 2, 3, 4, 5], 2),
        #"missing_integer": ([1, 2, 0, -1, 3],),
        #"find_odd": ([1, 2, 3, 2, 1],),
        #"binary_gap": (1041,),
        #"tape_equilibrium": ([3, 1, 2, 4, 3],),
        #"char_frequency_map": ("banana",),
        #"first_repeated_char": ("abcade",),
        #"first_non_repeating": ("aabbcdde",),
        "most_frequent": ("aabbcdde",),
    }

    try:
    
        obj = IntFunction()
        obj1 = StringFunction()

        # method
        for cls in [obj, obj1]:
            if hasattr(cls, func_name):
                method = getattr(cls, func_name)
                break
        else:
            print("Function not found.")
            exit()

        args = input_values.get(func_name)
        if args:
            result = method(*args)
            print(f"{func_name} result:", result)
        else:
            print("No input values defined for this function.")

    except AttributeError:
        print("Couldn't find any function.")
