#!/usr/bin/env python
import time
import os
flag = False
#options = [1,2,3] #future use for command line interpreter selection
default_command = "adb shell dumpsys battery"
#default_command will be the actual command that is run in cmd in my case I wanted a script that would repeat the battery of a connected Android device
cmd_inter = 'cmd /c \"{}\"'.format(default_command)
#power_inter = 'powershell \"{}\"'.format(default_command) #powershell version
#by default this script was written for cmd but its use can be expanded easily


while not flag:
	print("How long would you like the script to run(min)?")
	run_time = input()
	try:
		int(run_time)
	except ValueError:
		flag = False
	else:
		flag = True
	
	print("In how many seconds would you like the command to repeat?")
	sleep_time = input()
	try:
		int(sleep_time)
	except ValueError:
		flag = False
	else:
		flag = True
	
	if flag == False or int(run_time) <= 0 or int(sleep_time) <= 0:
		print("One of the two inputs are either not integer number or they are lesser than zero.")
		flag = False

	#print(run_time)
i_rt = int(run_time)
i_st = int(sleep_time)
iterations =int((i_rt * 60)) / i_st

#print("\n")
#while int(interpreter) not in options:
#	print("Please select what command line interpreter you are using: shell(1), cmd(2), powershell(3)")
#	interpreter = input()

for i in range(int(iterations)):
	os.system(cmd_inter) #replace cmd_inter with power_inter for powershell 
	time.sleep(i_st) #how long till the command is ran again (seconds)
	os.system('cmd /c \"cls\"') #clears the screen so that it will be easy to monitor that window if necesary
	#if the above line is commented it will show each output consecutively. 
