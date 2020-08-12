from data import us_state_abbrev,states_list 
"""
data.py can be found on:
https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/07-09-data-structures/code/data.py

"""
cnt=0
cnt_key=0
cnt_value=0
for state,abber in us_state_abbrev.items():
    cnt += 1
    if(cnt==10):
        print(f"{state}'s abberivation is {abber}, and they are 10th key/value pair in a dictionary. :)")
        print(f"{states_list[cnt-1]} is 10th item in list of US states. ")

for state in us_state_abbrev.keys():
    cnt_key+=1
    if(cnt_key==45):
        print(f"{state} is the 45th key in a dictionary.")

for abber in us_state_abbrev.values():
    cnt_value+=1
    if(cnt_value==27):
        print(f"{abber} is the 27th value in a dictionary.")

