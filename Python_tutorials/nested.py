#!/usr/bin/env python3


print("Hello World!")

def email_is_valid( email ):
    if ("@" in email):
        if ("." in email):

            print("This email looks good to me, Good Job!!")
            return True;


        else:
            print("This emial seems to be missing a . shithead!!")
            return False;
    else:
     print("Email seems to be missing an @ symbol!!")
     return False;

     

 
email = str(input("Please enter a valid email: " ))


if (email_is_valid(email) ):
 print("    Success!!")
 

else:
    print("Failed Dummy, You don't know what an email address consist of?");

    
