import argparse
#import clipboard as cp


#Goal: To output an email template with available variables

def write_email(target_info, your_info):
   #Best time: 9am-10am Tuesday, Wednesday, Thursday
   #Need to follow up the 2nd time
   """
   Input: 3 lists - target info [target_name, firm, group, location, common_interest, follow_up_count, responded], 
                    your info [name, position, my_interest, undergrad, PDP] + availabilities[time1, time2, time3] 
   Return: appropriate email based on the follow up count 
   """
   
   #The expected input is a string with variables in an order seperated by commas => changes into columns of a dataframe
   info = str(target_info).split(', ')
   target_name = info[0].split(' ')[0]
   firm = info[1].capitalize() 
   group = info[2].lower() 
   location = info[3].capitalize() 
   target_common_interest = info[4].lower() 
   
   #Checking if they have responded
   follow_up_count = int(info[5])
   
   #Your information + availabilities
   variables = str(your_info).split(', ')
   name = variables[0].capitalize()
   position = variables[1].lower() 
   my_interest = variables[2].lower() 
   undergrad = variables[3].lower()
   PDP = variables[4].capitalize() 
   
   availabilities = variables[5:]


   if follow_up_count == 0:
      print("1st_Template")
      Email = f"""Hello {target_name},
<p>I hope you are having a wonderful week! </p>
<p>My name is {name}, and I’m currently a rising business senior at USC while pursuing a master in {PDP}. {firm} is my top choice for a {position} next year and I hope I can ask you for more advice on the process given our shared interest in {target_common_interest}. I believe I would hit the ground running with my experience in research and leadership. For your convenience, I have listed some of my availabilities below: </p>
<ul>
   <li>{availabilities[0]}</li>
   <li>{availabilities[1]}</li>
   <li>{availabilities[2]}</li>
</ul>
<p>I understand you’re very busy and that these times might not work for you. If that’s the case, please let me know and I’d be happy to work around your schedule. </p>
<p>I have also attached my resume below, which shows the relevant internships I’ve had to date. Thank you for your time and consideration. I look forward to hearing from you and have a wonderful day. </p>

<p>Cheers, </p>
{name}"""
      

   elif follow_up_count == 1:
      print("2nd_Template")
      Email = f"""Hi {target_name},
<p>I hope your week is going well! </p>
<p>I emailed last week and just wanted to reach out again since my email probably got lost in your inbox. I think you're a very accomplished person and feel that I can learn a lot from speaking with you. Please let me know if you have 5-10 minutes for a quick chat. No pressure at all if you’re too busy, but I would really appreciate it and am happy to work around your busy schedule.</p>
<p>Or if it’s easier for you, I’ve also included some of my availabilities below:</p>
<ul>
    <li>{availabilities[0]}</li>
    <li>{availabilities[1]}</li>
    <li>{availabilities[2]}</li>
</ul>
<p>Please feel free to let me know either way. Thanks for your consideration and I look forward to hopefully connecting soon.</p>
<p>Cheers, </p>
{name}"""
      
   elif follow_up_count == 2:
      print("3rd_Template")
      Email = f"""Hi {target_name},
<p>I hope your week is going well! </p>
<p>I reached out over a week ago hoping for a chance to learn more about yourself & your experience at {firm}. I’m sure you can tell I’m very eager to speak with you; however, I wanted to make sure I’m striking the right balance between being persistent and being respectful, so if now is not a good time I will stop reaching out for now.</p>
<p>If you can spare 10 minutes of your time at all, I would really appreciate it. Even if it's just a few minutes, I would be grateful to just get some general career advice from you.</p>
<p>Thank you in advance for your time and have a great day.</p>
<p>Cheers,</p>
{name}"""
   
   return Email 
   

      

def main():
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
   default=["John", "BCG", "chess", "0", "March 5th 2pm", "March 7th 11am", "March 3rd 10am"],  # default if nothing is provided
   )
   
      # parse the command line
   args = CLI.parse_args()
   print(args)
   # access CLI options
   write_email(args.vars, args.info)

if __name__ == "__main__":
   main()
