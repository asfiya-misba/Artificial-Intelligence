Name: Asfiya Misba
Student ID: 1002028239

CSE - 5360 - Assignment 1

**********************************************************************
Language: Python
Version: 3.10

***********************************************************************
Contents:
->README.txt
->main.py
->start.txt
->goal.txt
->dump_file.txt

*********************************************************************
Code Structure:
1. File is created in the global space in write mode and flag is set as False.
2. In the Class Node, the following methods are defined, 
	# Method to find the path to the root
	# Method to expand the node
	# Method to find the children
	# Method to list the moves that make up the solution
	# method to compare 2 nodes based on their pathCost attribute
3. In the Class EightPuzzle, the following methods are defined,
	# Method to find the empty tile
	# Method to find the path cost
	# Method to check if the current state is the goal state
	# Method to find the next move to be performed
	# Method to find the sequence of moves leading to the goal state
4. Heuristic methods are defined and a method to read the contents of the start and goal state are defined.
5. Methods for each of the algorithms are defined.


***********************************************************************
Steps to execute:
1. Copy all the files into a folder
2. Run the code using,
				python main.py start.txt goal.txt bfs true
3. This will also create a dump file
4. To run without dump file use,
				python main.py start.txt goal.txt bfs false
5. Giving python main.py start.txt goal.txt, will execute the method a* and will not generate any dump file.


Note: 
1. The dump file is created but it is only written when the last command line argument is true.
2. Use the following to give the method names as command line arguments,
	bfs, dfs, ucs, ids, dls, greedy, a*



**************************************************************************
Sample Output:

(venv) PS C:\Users\asfiy\PycharmProjects\ai_assignment1_new> python main.py start.txt goal.txt bfs true
Nodes Popped =  1531
Nodes Expanded =  1395
Nodes Generated =  2573
Max Fringe Size =  1041
Solution found at depth =  12
Steps: 
['Move 7 RIGHT', 'Move 8 DOWN', 'Move 4 LEFT', 'Move 1 UP', 'Move 5 RIGHT', 'Move 3 UP', 'Move 2 LEFT', 'Move 8 LEFT', 'Move 3 DOWN', 'Move 6 DOWN', 'Move 7 RIGHT', 'Move 8 RIGHT']
(venv) PS C:\Users\asfiy\PycharmProjects\ai_assignment1_new> 


*********************************************************************************
References:
https://www.omnicalculator.com/math/manhattan-distance
https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/
https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288
https://www.javatpoint.com/8-puzzle-problem-in-python

