#!/usr/bin/env python3

"""
Stars Without Number - Interface Tool
Written By: Tyler Thune

This program as it stands will serve to provide both the Game Master
and the players of a group for the tabletop game Stars Without Number
a convenient and interactive dashboard from which they can streamline and 
improve their Stars Without Number experience.
"""

import random
import sys
import math
#import pygtk
#pygtk.require('2.0')
#import gtk

def main():
	num_of_hex = int(input('Number of hexes in the spike jump: '))
	chart_age = float(input('Enter the age of the relevant navigational charts in years: '))
	drive_rating = int(input("Enter your lead ship's spike drive rating: "))
	nav_skill = int(input('Enter your nav skill rating: '))

	int_mod = int(input('Enter your Intelligence Modifier: '))
	tech_med_skill = int(input('Enter your Tech/Medical skill level: '))

	spike_difficulty(num_of_hex,chart_age,drive_rating,nav_skill)
	tech_med_healing(int_mod,tech_med_skill)


"""
def health_roll:
	if char_class == 'Psychic':
		new_max_hp= max_hp
		while max_hp > new_max_hp:
			new_max_hp = roll_dice(char_level,4)+char_level*con_mod
			return new_max_hp
	elif char_class == 'Expert':
		new_max_hp= max_hp
		while max_hp > new_max_hp:
			new_max_hp = roll_dice(char_level,6)+char_level*con_mod
			return new_max_hp
	elif char_class == 'Warrior':
		new_max_hp= max_hp
		while max_hp > new_max_hp:
			new_max_hp = roll_dice(char_level,8)+char_level*con_mod
			return new_max_hp
	else
		print("Error: Character Class Not Recognized")
"""

def spike_difficulty(num_of_hex,chart_age,drive_rating,nav_skill):
	
	# Determines the modifier given to a Nav check from chart age/existence
	# Existence is poorly handled TODO
	if chart_age >= 0 and chart_age < 1:
		chart_mod = 0
	elif chart_age > 1 and chart_age < 5:
		chart_mod = 1
	elif chart_age > 5:
		chart_mod = 2
	else:
		chart_mod = 4

	# Determines modifier given by traveling a certain distance
	dist_mod = math.floor(num_of_hex/2)

	# Lists a series of options based on optional trim levels
	for counter in range(nav_skill+1):
		jump_difficulty = 7 + chart_mod + dist_mod + counter
		spike_time = round(((48 + (6*24*num_of_hex))/(drive_rating + counter)),2)
		print("At trim level ", counter)
		print("The difficulty of the spike is: ", jump_difficulty)
		print("and it will take", spike_time, "hours")
		print(" ")

def tech_med_healing(int_mod,tech_med_skill):
	heal_mod = int(int_mod + tech_med_skill)
	heal_roll = sum(roll_dice(2,6)) + heal_mod

	print(heal_mod)

	print(heal_roll)

	if heal_roll > 6 and heal_roll < 12:
		regen = heal_roll - 6
	elif heal_roll > 11 and heal_roll < 16:
		regen = 2*(heal_roll-11) + 5
	elif heal_roll > 15:
		regen = 3*(heal_roll-15) + 5 + 8
	else:
		print("failed to calculate Tech/Medical healing") 

	print(regen)

def roll_dice(num_of_dice, sides):
	return [random.randint(1,sides) for i in range(num_of_dice)]

	

if __name__ == '__main__':
	sys.exit(main())