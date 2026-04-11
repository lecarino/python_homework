# Task 1: Diary
import traceback
#Open a file called diary.txt for appending.
count = 0
try:
    with open('diary.txt', 'a') as file:
        #In a loop, prompt the user for a line of input. The first prompt should say, "What happened today? ". All subsequent prompts should say "What else? "
        while True:
            if count == 0:  #inital question is different from subsequent questions
                user_input = input('What happened today?\n')
                file.write(f"{user_input}\n") #write to file with new line
                count +=1
            else:
                user_input = input("what else?\n")
                file.write(f"{user_input}\n") #write to file with new line

            if user_input == "done for now": #When the special line "done for now" is received, write that to diary.txt. Then close the file and exit the program (you just exit the loop).
                break
#Copy Pasted Exception from Homework
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")