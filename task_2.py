def calculation(x_list, y_list):
    # Print answer

    for item in y_list:
        print(x_list.count(item))


def collect_data():
    # Collecting user data

    x_list = []
    y_list = []

    while True:
        user_input = input('Input number of x elements or full file name with data.')

        # Check if input data from file or keyboard
        if '.' in user_input:
            try:
                with open(user_input, 'r') as file:
                    user_list = [line.strip().split(',')[:-1] for line in file]
                    x_list = user_list[1]
                    y_list = user_list[3]
                    return calculation(x_list, y_list)

            except FileNotFoundError:
                print('Sorry, but you added not correct file name. Please try again.')
            except IsADirectoryError:
                print('Sorry, but you added not correct file name. Please try again.')
        else:
            try:
                x_element = int(user_input)
                for item in range(x_element):
                    x_list.append(input('Input your data: '))

                y_element = int(input('Input number of y elements: '))
                for item in range(y_element):
                    y_list.append(input('Input your data: '))

            except ValueError:
                print('Sorry, but you added not a number or file name. Please try again.')
                collect_data()

            return calculation(x_list, y_list)


if __name__ == '__main__':
    collect_data()
