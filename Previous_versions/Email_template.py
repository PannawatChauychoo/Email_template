import argparse
#import clipboard as cp


#Goal: To output an email template with available variables

def write_email(variables, info, availabilities):
   #Best time: 9am-10am Tuesday, Wednesday, Thursday
   #Need to follow up the 2nd time
   """
   Input: previous_meetings, follow_up, identity,  
   Return: appropriate email for the given scenario
   """
   
   
   variables = variables.split(', ')
   name = variables[0].capitalize()
   position = variables[1].lower() 
   my_interest = variables[2].lower() 
   PDP = variables[3].capitalize() 
   
   #The expected input is a string with variables in an order seperated by commas => changes into columns of a dataframe
   info = info.split(', ')
   target_name = info[0].capitalize() 
   firm = info[1].capitalize() 
   target_common_interest = info[2].lower() 
   follow_up_count = int(info[3])
   
   
   availabilities = availabilities.split(', ')

   if follow_up_count == 0:
      print("1")
      Email = f"""Hello {target_name}, 
      I hope you are having a wonderful week! 
      My name is {name}, and I’m currently a rising business senior at USC while pursuing a master in {PDP}. 
      {firm} is my top choice for a {position} next year and I hope I can ask you for more advice on the process given our shared interest in {target_common_interest}. 
      I believe I would hit the ground running with my experience in research and leadership. For your convenience, I have listed some of my availabilities below:
      
      · {availabilities[0]}
      · {availabilities[1]}
      · {availabilities[2]}
      
      I understand you’re very busy and that these times might not work for you. If that’s the case, please let me know and I’d be happy to work around your schedule. 
      I have also attached my resume below, which shows the relevant internships I’ve had to date. Thank you for your time and consideration. I look forward to hearing from you and have a wonderful day. 

      Cheers,
         {name}"""
      

   elif follow_up_count == 1:
      print("2")
      Email = f""" Hi {target_name}, 
      I hope your week is going well. I emailed last week and just wanted to reach out again since my email probably got lost in your inbox. I think you're a very accomplished person and feel that I can learn a lot from speaking with you. Please let me know if you have 5-10 minutes for a quick chat. No pressure at all if you’re too busy, but I would really appreciate it and am happy to work around your busy schedule.
      Or if it’s easier for you, I’ve also included some of my availabilities below:
      
      · {availabilities[0]}
      · {availabilities[1]}
      · {availabilities[2]}
      
      Please feel free to let me know either way. Thanks for your consideration and I look forward to hopefully connecting soon.
      
      Cheers,
      {name}"""
      
   elif follow_up_count == 2:
      print("3")
      Email = f"""Hi {target_name},
      I hope your week is going well. I emailed last week and just wanted to reach out again since my email probably got lost in your inbox. 
      I think you're a very accomplished person and feel that I can learn a lot from speaking with you. Please let me know if you have 5-10 minutes for a quick chat. No pressure at all if you’re too busy, but I would really appreciate it and am happy to work around your busy schedule.

      Or if it’s easier for you, I’ve also included some of my availabilities below:
      · {availabilities[0]}
      · {availabilities[1]}
      · {availabilities[2]}
      
      Please feel free to let me know either way. Thanks for your consideration and I look forward to hopefully connecting soon.
      
      Cheers,
      {name}"""
   
   elif follow_up_count == 3:
      print("4")
      Email = f"""Hi {target_name},
      I hope your week is going well. I reached out over a week ago hoping for a chance to learn more about yourself & your experience at Barclays. 
      I’m sure you can tell I’m very eager to speak with you; however, I wanted to make sure I’m striking the right balance between being persistent and being respectful, so if now is not a good time I will stop reaching out for now.
      If you can spare 10 minutes of your time at all, I would really appreciate it. Even if it's just a few minutes, I would be grateful to just get some general career advice from you.

      Thanks in advance for your time and have a great day.

      Cheers,
      {name} """        
   
   #cp.copy(str(Email))
   
   return print(Email) #, print("\n Copied into your clipboard! You can paste this anywhere now.")  
      
def read_arguments(filename):
   
   with open(filename, 'r') as f:
      arguments = [line.strip() for line in f if not line.startswith('#') and line.isspace() == False]
   return arguments


def main():
   arguments = read_arguments('Inputs.txt')
   print(arguments)
   
   # defined command line options/this also generates --help and error handling
   CLI = argparse.ArgumentParser(description="Email template based on inputted variables")
   
   CLI.add_argument(
   "vars",  # name on the CLI - drop the `--` for positional/required parameters
   type=str,
   default=["Pannawat", "consultant", "data science", "Applied Data Science"],  # default if nothing is provided
   )
   
   CLI.add_argument(
   "info",  # name on the CLI - drop the `--` for positional/required parameters
   #nargs="*",  # 0 or more values expected => creates a list
   type=str,
   default=["John", "BCG", "chess", "0"],  # default if nothing is provided
   )
   
   CLI.add_argument(
   "time",  # name on the CLI - drop the `--` for positional/required parameters
   type=str,
   default=["March 5th 2pm", "March 7th 11am", "March 3rd 10am"] # default if nothing is provided
   )
   
   # parse the command line
   args = CLI.parse_args(arguments)
   print(args)
   # access CLI options
   write_email(args.vars, args.info, args.time)

if __name__ == "__main__":
   main()
