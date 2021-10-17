# Machine_learning_rules

The project is part of the UI curriculum. It contains an example of using simple rules in terms of machine learning to create a knowledge base and operate with rules, process the input data and execute instructions based on templates stored in the program or created by user. 

### Algorithm
In the beginning, the program goes through all the existing facts for all the rules and finds for each of the facts of their condition that have the appropriate knowledge, if they meet the patterns of the conditions. Next, it goes through each rule separately and selects from the appropriate facts, such as pairs or triplets that form the fulfilled condition, and writes the result, consequently adding the action to the list of possibly executable.
Then all actions are filtered: those, which add a fact that is already there or delete a fact that is not there, are deleted from the list.
Next, the program selects the first action from the list and performs it. After performing one action, the rules will be reviewed.
The rule itself is processed in the way that we get a list of all the conditions to be met, the program deletes all substrings containing ‘?‘. Further in the facts, it looks for the occurrence of all the other substrings. And the facts that have gone through this condition remain. The program compares the data among the remaining conditions in the places where ‘?‘ occurs. If these conditions are also met, the method generates the resulting action from the data of these facts.

### Program
The main part of the program is written as a GUI using the pyqt5 tool in Python.
The program can load facts and rules from a file. Two knowledge bases are now ready: Family Relationships and Work created by me.
The program can show execution after one step or run all possible actions to the end. It displays a list of facts that are currently current in the system, a list of all rules, actions that will be performed in the initial steps and are calculated from the current facts, and a list of listed messages.
The user can add a fact at the moment when the system is now. After adding the fact, all actions will be processed again. A fact that is already in the system will not be added to the list.

![Image alt](https://github.com/AdaVarts/Machine_learning_rules/blob/main/Example.png)
