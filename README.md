# Termicoder  
View, Code, Debug, Submit, Learn directly from terminal  
Made with :heart: by Divesh Uttamchandani

### The repo will remain private till beta version is completed and released. The repo will then be transfered to termicoder organization account and developement will be carried out from there
  
Planned Platform support(in order of priority):   
[CodeChef](www.codechef.com)  
[Iarcs Opc](http://opc.iarcs.org.in/index.php/problems/)  
Codeforces  
Google Codejam   
Hackerrank  
Hackerearth  


Planned Language Support(in order of priority):  
c/c++  
Python  
Java  
## NOTE TO SELF:
### Basic things to keep in mind
### This should be designed so that it can be later made availible as a package in pip etc.
### This should be able to be extended to other judges easily so modularity is a priority
### The cli should be on similar grounds as git use commands, arguments and optional arguments judiciously
  
# Current Ideas 
## Setup
format:  
setup judge problem code  
setup judge contest code  
setup url  
1) Creates a folder for each problem with data of that problem (url, problem statement(try pdf, html, txt etc), sample I/O, submit status/last time errors)
2) add support for listing all problem folder and status(custom ls), quickly changeing to a unsolved problem folder
3) use git like hidden file approach

### All the following commands work based on folder i am in so no need to remember/type problem code again and again 
  
  
## View  
1) Current contests, trending problems, live problems etc. (Coders Calender)
2) Generating url corresponding to a problem code/name in an easy way for all the supported platform
3) Display the problem in best way possible, try not to leave terminal also be sure to somehow display the important images  
    options:  
    3.1) Use a terminal based browser such as w3m/elinks etc.   
    3.2) open the page in a browser (directly from terminal)   
    3.3) display as text on terminal  
    3.4) display a modified webpage on text based browser 
4) also open the links given in problem description
5) Reminders about contests
  
general format : view --options  
it displays the problem if exist in current folder if more than one than displays a list.
  

## Code
1) most used predesigned but modifiable templates in the supported languages  
2) templates correspnding to various most used algos/functions/tricks.
3) Incorporate compile/build commands.. and autobuild on leaving editor (might need configure a default editor variable (ex. code abc.c executes vim abc.py directly loaded with the defaylt template etc.))  
4) Add author name,problem url and other info to every file
5) Make a generalized file naming schheme
6) Also try version control the code with git

general format : code --options
  
## Debug
1) Check I/O corressponding to sample test cases
2) Test case generator
3) brute force generator for small values
4) calculation of time
5) Integration with existing tools (gdb,, valgrind etc.)

## Submit
1) easy submit directly from terminal
2) retrive status after submit
3) confirm password on submit  
4) first compile and check against sample test case before submit.... Confirm again if error

general format : submit --options  

## Learn
1) assign/retrive categories of problems , open resources related to them
2) Link for editiorial/resources/google search the uncommon words in the problem statement etc.
3) show suggestions to remove errors found using submit status
4) Support for commonly encountered errors
  

# Future Ideas (The feasiblity of ideas hasn't been verified and most ideas are vague/in budding stage)
1) Save encrypted passwords confirm a common master password on submit  
2) Make it advanced enough to handle multiple profiles for the same site . May be by implementing user interface.  
3) Should be a complete guide and reference  
4) Should be simple enough for beginners but compelling enough for advanced users  
5) It should be a learning resource for beginners as well as a great reference for advanced coders  
6) Make user learn new things (but in first version start with only c/c++/stl/linux basics)  
7) Make it availible as a bundle which incorporates various tools such as vim plugins but they should be minimum so work them out   
8) Make Users use good techniques that I have learned also ask competetive coders for suggestions.  
9) It should improve with the user progress. Refer to his profiles and code for the type of coder he is(which language he codes in). Ask him ques like which language he uses does he have knowledge of vim etc. If he is a begginer make him use best tools if advanced user suggest him the tools but try also to support his tools. also ask him to start from basics and then introduce complexity like code templates etc. 
10) Make it as good as a practical guide book for everyone it is a road with check points. One could start form check point confirming to his abilities.
11) make a good website and improving markdowns
12) Somewhere in the future try integrating this with github repositories.... Private repository for current contest Public for old contests etc.
13) Try incorporating a settings webpage run on a local server
14) Incorporate ML/AI to test case generator, problem categoriser, problem template(input output variables, loops etc)
15) Integrating with stopstalk- trending problems, friends etc.
16) Try integrating this with other applications that programmers use.
  
## Make people :heart: this :wink:
