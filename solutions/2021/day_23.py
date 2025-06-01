from aocd import get_data

input = get_data(day=23, year=2021)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    """
    ### State 0
    #############
    #...........#
    ###B#A#A#D###
      #D#C#B#C#
      #########

    ### State 1 : 5 + 6 + 50 + 600
    #############
    #A........BA#
    ###B#.#.#D###
      #D#.#C#C#
      #########

    ### State 2 : 30 + 40 + 2000 + 500
    #############
    #A........DA#
    ###.#B#C#.###
      #D#B#C#.#
      #########

    ### State 3 : 10000 + 2000 + 3 + 3
    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #########
    """

    return 15237


def part_2(lines):
    """Proposition incorrecte
    ### State 0
    #############
    #...........#
    ###B#A#A#D###
      #D#C#B#A#
      #D#B#A#C#
      #D#C#B#C#
      #########


    ### State 1 : 5 + 5 + 700 + 70 + 40 + 700 = 1520
    #############
    #AB.B...C.CA#
    ###B#.#.#D###
      #D#.#.#A#
      #D#.#A#C#
      #D#.#B#C#
      #########

    ### State 2 :  50 + 60 + 50 + 8 + 70 = 238
    #############
    #AA.....C.CA#
    ###.#B#.#D###
      #D#B#.#A#
      #D#B#.#C#
      #D#B#.#C#
      #########


    ### State 3 500 + 600 + 4000 + 3 + 700 + 700 = 6503
    #############
    #AA...D...AA#
    ###.#B#C#.###
      #D#B#C#.#
      #D#B#C#.#
      #D#B#C#.#
      #########

    ### State 4 7000 + 11000 + 11000 + 11000 = 40000
    #############
    #AA.......AA#
    ###.#B#C#D###
      #.#B#C#D#
      #.#B#C#D#
      #.#B#C#D#
      #########

    ### State 5  5 + 5 + 9 + 9 = 28
    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #A#B#C#D#
      #A#B#C#D#
      #########
    """
    return None


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# print(f'My answer is {part_2(input)}')
