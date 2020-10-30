
"""
Dev. by: AIT OUHANI Radwane.
Project: FreeCodeCamp first project.

Purpose:
Students in primary school often arrange arithmetic problems vertically 
to make them easier to solve.This is a program that receives a list of 
strings that are arithmetic problems and returns the problems arranged 
vertically and side-by-side. This program optionally displays the answers
to the problem. 
For example : 
    Input : ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    Output (with results set to True) : 
           32      3801      45      123    
        + 698    -    2    + 43    +  49    
        -----    ------    ----    -----    
          730      3799      88      172    
"""


def arithmetic_arranger(test_list,res=False):
    
  #Declarations
  operation_space ="    "
  first_line = ""
  second_line = ""
  third_line =""
  fourth_line = ""
   
  #verification
  if len(test_list)>5:
    return "Error: Too many problems."
  for string_op in test_list:
    #separating the input
    first_num_s = string_op.split(" ")[0] 
    second_num_s = string_op.split(" ")[2]
    operator = string_op.split(" ")[1]
    diff= max(len(first_num_s),len(second_num_s))-min(len(first_num_s),len(second_num_s))
    #verifications
    try:
      int(first_num_s)
    except:
      return "Error: Numbers must only contain digits."
    try:
      int(second_num_s)
    except:
      return "Error: Numbers must only contain digits."
    if len(first_num_s)>4 or len(second_num_s)>4:
      return "Error: Numbers cannot be more than four digits."
    #the greater len
    first_g =False
    second_g=False
    if len(first_num_s)>len(second_num_s):
      first_g=True
    elif len(first_num_s)<len(second_num_s):
      second_g= True
    else: 
      equal_g =True
    #spaces
    space = ""
    for i in range(diff):
      space += " "
      #operation line
    line = "-"
    for i in range(max(len(first_num_s),len(second_num_s))+1):
      line += "-"
    
    #finding the results
    if operator =="+":
      result = int(first_num_s)+int(second_num_s)
    elif operator =="-":
      result = int(first_num_s)-int(second_num_s)
    else:
      return "Error: Operator must be '+' or '-'."
            
    #output
    if first_g :
      first_out="  "+first_num_s
      second_out=space+second_num_s
    elif second_g:
      first_out="  "+space+first_num_s
      second_out=second_num_s
    else:
      first_out="  "+first_num_s
      second_out=second_num_s
    
    
    first_line += first_out+operation_space
    second_line += operator+' '+second_out+operation_space
    third_line += line+operation_space
    if res:
      space_res=""
      for i in range(len(line)-len(str(result))):
        space_res += " "
      fourth_line += space_res+str(result)+operation_space
   
  if res:
    arranged_problems= first_line[:-4]+'\n'+second_line[:-4]+'\n'+third_line[:-4]+'\n'+fourth_line[:-4]
  else :
    arranged_problems= first_line[:-4]+'\n'+second_line[:-4]+'\n'+third_line[:-4]
    
  return arranged_problems



    