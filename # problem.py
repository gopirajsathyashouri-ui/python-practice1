# problem

support_message = input()
print("Support Message:",support_message)
if "Indentation" in support_message :
    if "if" or "else" in support_message:
      print("Issue Type: Indentation and Conditional Support" )
      print("Priority: High Practice Priority ")  
    else:
      print("Issue Type: Indentation Support")
      print("Priority: Medium Practice Priority")
elif "loop" or "loops" in support_message :
  print("Issue Type: Loop Support")
  print("Priority: Medium Practice Priority")
else :
  print("Issue Type: General Support")
  print("Priority: Normal Priority")