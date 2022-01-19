#Functions with Outputs 

def format_name(f_name,l_name):
  """Take a first and last name and format it to return the title case version of the name."""
  if f_name=="" or l_name=="":
    return 
  #모든 단어가 대문자로 시작하고 소문자로 연결되도록 하기 위해서 .title() 사용 
  formatted_f_name=f_name.title()
  formatted_l_name=l_name.title()
  
  return f"{formatted_f_name} {formatted_l_name}"
  
print(format_name(input("what is your first name?"),input("What is your last name?"))