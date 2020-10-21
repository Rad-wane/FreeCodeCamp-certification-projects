# -*- coding: utf-8 -*-
"""
"""
Dev. by: AIT OUHANI Radwane.
Project: FreeCodeCamp 2nd project.

Purpose: README.md

"""

def add_time(start_time,duration,s_day="bla"):
    week=['monday', 'tuesday', 'wednesday','thursday','friday', 'saturday', 'sunday']
    
    #spliting the start time
    s_hour=int(start_time.split(":")[0])
    s_minute=int(start_time.split(":")[1].split(" ")[0])
    s_time =start_time.split(" ")[1]
    d_hour=int(duration.split(":")[0])
    d_minute=int(duration.split(":")[1])
    #inverse AM PM
    def inverse(string):
        
        if string=="AM":
            return "PM"
        else:
            
            return "AM"
    #Calculating the sum
    if (s_minute+d_minute)<60:
        r_minute=s_minute+d_minute
        r_hour = s_hour+d_hour
    else:
        r_minute=(s_minute+d_minute)%60
        r_hour = 1+s_hour+d_hour
        
    
    #if the min is 1 car.:
    if len(str(r_minute))==1:
        r_str_min="0"+str(r_minute)
    else:    
        r_str_min=str(r_minute)
    #converting to standard
    
    rem_hour=r_hour % 24
    if rem_hour>12:
        rem_hour-=12
    num_day=round(r_hour/24)
    hday=int(r_hour/12)
    
    if s_day!="bla" :
        day = s_day.lower()
        index = week.index(day)
        if num_day+index<=6:
            if num_day>=1:
                f_index = index+num_day
            else:
                f_index = index+num_day
        else:
            if num_day>=1:
                f_index = (index+num_day)%7 
            else:
                f_index = (index+num_day)%7
        day = week[f_index]
        day = day[0].upper()+day[1:]
        
    
    
    if num_day>1 and hday%2==0:
        r_string = str(rem_hour)+":"+r_str_min+" "+s_time+" ("+str(num_day)+" days later)"
        if s_day!="bla" :
            r_string = str(rem_hour)+":"+r_str_min+" "+s_time+", "+day+" ("+str(num_day)+" days later)"
    elif num_day>1 and hday%2!=0:
        r_string = str(rem_hour)+":"+r_str_min+" "+inverse(s_time)+" ("+str(num_day)+" days later)"
        if s_day!="bla" :
            r_string = str(rem_hour)+":"+r_str_min+" "+inverse(s_time)+", "+day+" ("+str(num_day)+" days later)"
    elif num_day<=1 and hday%2!=0:
        r_time= inverse(s_time)
        if inverse(s_time)=="AM":
            r_string = str(rem_hour)+":"+r_str_min+" "+r_time+" (next day)"
            if s_day!="bla" :
                r_string = str(rem_hour)+":"+r_str_min+" "+r_time+", "+day+" (next day)"
        else:
            r_string = str(rem_hour)+":"+r_str_min+" "+r_time
            if s_day!="bla" :
                r_string = str(rem_hour)+":"+r_str_min+" "+r_time+", "+day
    else:
       if hday==2:
           r_string = str(rem_hour)+":"+r_str_min+" "+s_time+" (next day)"
           if s_day!="bla" :
               r_string = str(rem_hour)+":"+r_str_min+" "+s_time+", "+day+" (next day)"
       else:
           r_string = str(rem_hour)+":"+r_str_min+" "+s_time
           if s_day!="bla" :
               r_string = str(rem_hour)+":"+r_str_min+" "+s_time+", "+day
    
    
        
        
    return r_string    
    
   



