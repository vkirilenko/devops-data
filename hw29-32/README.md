## _Task 1_

- "Self-study input() function. Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers and prints these objects as-is (just print(list) without any formatting)."  
  
  [My input](Python/myinput.py)

  
## _Task 2_

- "Develop a procedure to print all even numbers from a numbers list which is given as an argument. Keep the original order of numbers in list and stop printing if a number 254 was met. Don't forget to add a check of the passed argument type."  
  
    [Even numbers](Python/even.py)

  
## _Task 3_

- "Something old in a new way :). Self-study positional arguments for Python scripts (sys.argv). Write a script that takes a list of words (or even phrases)aScript should ask a user to write something to stdin until user won't provide one of argument phrases."  
   
    [Word guess](Python/wordguess.py)
	
	
## _Task 4_

- "We took a little look on os module. Write a small script which will print a string using all the types of string formatting which were considered during the lecture with the following context: This script has the following PID: <ACTUAL_PID_HERE>. It was ran by <ACTUAL_USERNAME_HERE> to work happily on <ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>."  
   
    [Information](Python/info.py)
	
	
## _Task 5_

- "Develop a function that takes a list of integers (by idea not in fact) as an argument and returns list of top-three max integers. If passed list contains not just integers collect them and print the following error message: You've passed some extra elements that I can't parse: [<"elem1", "elem2" .... >]. If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, but some list should be returned in any case."  
   
    [Max Ints list](Python/max_ints.py)	


## _Task 6_

- "Create a function that will take a string as an argument and return a dictionary where keys are symbols from the string and values are the count of inclusion of that symbol."  
   
    [Dictionary of strings](Python/dict_count.py)
 
 
## _Task 7_

- "Develop a procedure that will have a size argument and print a table where num of columns and rows will be of this size. Cells of table should contain numbers from 1 to n \** 2 placed in a spiral fashion. Spiral should start from top left cell and has a clockwise direction (see the example below)."  
   
    [Spiral table](Python/spiral.py)
	
	

## _Task 9_

- "For this task you need to have docker daemon installed and running.  The task is to create a python script, that has following functions:  1. connects to docker API and print a warning message if there are dead or stopped containers with their ID and name. 2. containers list, similar to docker ps -a  3. image list, similar to docker image ls 4. container information, like docker inspect  Connection function must accept connection string for example 'http://192.168.56.101:2376' and connect to it or use string from environment if no connection string is given.    In order to connect to docker, you can use either Unix socket or reconfigure daemon to use a network socket (https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option) "  
   
    [Docker info](Python/docker_info.py)