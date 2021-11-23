"""
Chapitre 11.3
"""


import math
from inspect import *

from game import *


def simulate_battle():
	ch1 = Character('mico', 100, 5, 10, 15)
	ch2 = Magician('Jacques', 100, 35, 3, 15, 7, 17)

	while ch1.hp > 0 or ch2.hp > 0:
		print('yo')



def main():
	simulate_battle()

if __name__ == "__main__":
	main()

