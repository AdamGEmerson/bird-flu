# -*- coding: utf-8 -*-

import time
import curses
import random
from curses import wrapper


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)

	GREEN_AND_BLACK = curses.color_pair(1)
	WHITE_AND_BLACK = curses.color_pair(2)
	BLACK_AND_WHITE = curses.color_pair(3)
	BLACK_AND_GREEN = curses.color_pair(4)

	middle_fingers = ["╭∩╮ʕ•ᴥ•ʔ╭∩╮", "┌∩┐(◣_◢)┌∩┐", "╭∩╮(ಠ۝ಠ)╭∩╮", "╭∩╮(Ο_Ο)╭∩╮", "┌∩┐(◕◡◉)┌∩┐", "( ° ͜ʖ͡°)╭∩╮", "┌П┐(▀̿Ĺ̯▀̿)", "凸(｀⌒´メ)凸",]

	for i in range(50):
		stdscr.clear()
		color_1 = GREEN_AND_BLACK
		color_2 = WHITE_AND_BLACK
		color_3 = BLACK_AND_GREEN

		if i % 2 == 0:
			color_1 = WHITE_AND_BLACK
			color_2 = GREEN_AND_BLACK
			color_3 = BLACK_AND_WHITE


		stdscr.addstr(0, 0, """
__   __          _                         _               
\\ \\ / /         ( )                       | |              
 \\ V /___  _   _|/__   _____    __ _  ___ | |_             
  \\ // _ \\| | | | \\ \\ / / _ \\  / _` |/ _ \\| __|            
  | | (_) | |_| |  \\ V /  __/ | (_| | (_) | |_   _   _   _ 
  \\_/\\___/ \\__,_|   \\_/ \\___|  \\__, |\\___/ \\__| (_) (_) (_)
                                __/ |                      
                               |____/                       """, color_1 | curses.A_BOLD)

		if i % 10 <= 5:
			stdscr.addstr(9, 0, """	
/$$$$$$$  /$$$$$$ /$$$$$$$  /$$$$$$$        /$$$$$$$$ /$$       /$$   /$$
| $$__  $$|_  $$_/| $$__  $$| $$__  $$      | $$_____/| $$      | $$  | $$
| $$  \\ $$  | $$  | $$  \\ $$| $$  \\ $$      | $$      | $$      | $$  | $$
| $$$$$$$   | $$  | $$$$$$$/| $$  | $$      | $$$$$   | $$      | $$  | $$
| $$__  $$  | $$  | $$__  $$| $$  | $$      | $$__/   | $$      | $$  | $$
| $$  \\ $$  | $$  | $$  \\ $$| $$  | $$      | $$      | $$      | $$  | $$
| $$$$$$$/ /$$$$$$| $$  | $$| $$$$$$$/      | $$      | $$$$$$$$|  $$$$$$/
|_______/ |______/|__/  |__/|_______/       |__/      |________/ \\______/""", color_2)

		if i % 10 >= 5:
			stdscr.addstr(9, 0, """
                                    
                   /´¯/)            
                  /__ /             
                /    /              
          /´¯/'...'/´¯¯`·¸          
       /'/.  /.   /.      /¨¯\\      
     ('(.  ´.   ´.    ¯~/'...')     
      \\.               .'.   /      
       '\\   \\           _.·´        
         \\.             (           
           \\.............\\          
                                    
""", color_3 | curses.A_BOLD)
    

		dots_list = ["   ", ".  ", ".. ", "..."]
		dots = dots_list[i % 4]
		stdscr.addstr(23, 0, f"Middle Fingers Loading{dots}  | {i * 2}%", curses.COLOR_GREEN)
		curses.curs_set(0)

		stdscr.refresh()
		time.sleep(0.10)

	stdscr.clear()
	curses.curs_set(1)
	message = "BIRD FLU INITIALIZED... BEGIN FLIPPENING..."
	for char in message:
		stdscr.addch(char, curses.COLOR_GREEN)
		stdscr.refresh()
		time.sleep(0.1)
	time.sleep(0.3)
	stdscr.clear()
	stdscr.bkgd(' ', BLACK_AND_WHITE)

	stdscr.refresh()
	time.sleep(0.3)

	stdscr.bkgd(' ', GREEN_AND_BLACK)
	stdscr.refresh()

	flippening = True
	while flippening:
		curses.curs_set(0)
		donger = middle_fingers[random.randrange(0, len(middle_fingers) - 1)]

		x_coord = random.randrange(0, 80 - len(donger))
		y_coord = random.randrange(0, 24)
		stdscr.addstr(y_coord, x_coord, donger, curses.COLOR_GREEN)
		stdscr.refresh()
		time.sleep(0.2)

wrapper(main)