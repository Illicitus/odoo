def sort_and_remove(func):
    # This function sort data from function if key not the same,
    # and remove age, gender.

    def decorator():
        check_list = [item[2] for item in func]

        if len(set(check_list)) != 1:
            sort = sorted(func, key=lambda item: item[2])
            result = []
            for item in sort:
                result.append(item[:2])
            return result
        else:
            result = []
            for item in func:
                result.append(item[:2])
            return result

    return decorator()


def add_abbreviation(func):
    # Add abbreviation 'Г-н' or 'Г-жа' to func data.

    def decorator():
        result = func()
        for item in result:
            if item[-1] != 'Ж':
                item.insert(0, 'Г-н')
            else:
                item.insert(0, 'Г-жа')
        return result

    return decorator()


def print_information(func):
    # Print data

    def decorator():
        result = func
        for item in result:
            print('{0} {1}'.format(item[0], item[1]))
        return result

    return decorator()


@print_information
@sort_and_remove
@add_abbreviation
def collect_information():
    # Collecting user data

    while True:
        user_input = input('Input number of persons or full file name with personal data.')

        # Check if input data from file or keyboard
        if '.' in user_input:
            try:
                with open(user_input, 'r') as file:
                    user_list = [line.strip().split(',')[:-1] for line in file]
                    return user_list
            except FileNotFoundError:
                print('Sorry, but you added not correct file name. Please try again.')
            except IsADirectoryError:
                print('Sorry, but you added not correct file name. Please try again.')
        else:
            user_list = []
            try:
                count = int(user_input)

                index = 0
                while index < count:
                    user_list.append(
                        [input('Your name and surname: '),
                         input('Your age is: '),
                         input('Your gender is: ')]
                    )
                    index += 1
                return user_list
            except ValueError:
                print('Sorry, but you added not a number or file name. Please try again.')
