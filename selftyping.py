import sys
import time as t

def _print(text:str, delay:int = 2):
	interval = delay/len(text)
	for char in text:
		if text.index(char) == len(text)-1:
			print(char, flush=True)
			break
		print(char, end='', flush=True)
		t.sleep(interval)



if __name__ == '__main__':
	print("Start")
	_print("It's self-typed text!")
	print("End")
	input()