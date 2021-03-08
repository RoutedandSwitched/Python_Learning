#!/usr/bin/env python3


def main():#{
    new_list = [ "John", "Doug", "Tucker", "Josh", "Tony",]

    

    counter = 0;
    limit = len( new_list);

    while (counter < limit ):
        print( new_list[counter] + "says hi!!" )

        counter += 1;
    
    '''
    while ( counter < limit ): #{
        print (new_list[conter] + " says hi!" ):
        counter += 1:
        #}
    for item in new_list:#{
        item = "Poopface";
  
    print( item + " says hi! ")
    '''            #}
    print( limit )
#}

main();

#tuples are similar to list but they use () instead of [], but they cannot be altered. They can be added to but you can't change the value inside.
