# Notes on the Curses Python Library

import curses
from curses import wrapper
from time import process_time_ns
import os


def main(stdscr):       # curses runs a screen over the top of the terminal and that is where the changes are made and refreshed

    size = os.get_terminal_size()

    stdscr.clear()      # clears the screen
    print(size)
    # stdscr.addstr(size)
# co-ordinates are added to allow you to place output to a screen position;
    stdscr.addstr(
        10, 10, "This is how you output a message to the screen", curses.A_BOLD)
# there a various attributes to make text bold underlined etc

# to add colours you must first declare colour pairs then call them as follows;

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_MAGENTA)

    stdscr.addstr(15, 15, "This is a coloured text example",
                  curses.color_pair(1))
    stdscr.addstr(20, 15, "THIS IS ANOTHER COLOURED TEXT EXAMPLE",
                  curses.color_pair(2))
    
    rows1, cols2 = stdscr.getmaxyx()
    stdscr.addstr(1, 0, " " * cols2, curses.color_pair(1))

    stdscr.refresh()

    while True:
        stdscr.refresh()
        key = stdscr.getkey()
        if key == "KEY_RESIZE":
            rows, cols = stdscr.getmaxyx()
            stdscr.addstr(0, 0, " " * cols, curses.color_pair(1))
        elif key == "q":
            break

    stdscr.refresh()    # refreshes the screen to display any changes
    stdscr.getch()      # Get character from input


wrapper(main)
