#!/usr/bin/env python3


class Person: #{

    def __init__( self, name = " unknown " , age = 101 ): #{
        self.name = name;
        self.age = age;
    #}
    def say_hello( self ):#{
        print( self.name + ", who is " + str(self.age) + " says hello! " );

        
        #}
    def __del__( self ): #{
        print( 'RIP ' + self.name + ' who died at the age of ' + str( self.age));
        #pass; #pass is a keyword that will do nothing, it's so you can setup code that you areent using yet and not worry about indention block.
            

        #}
#}

bob = Person();
andrew = Person("Andrew White", 22 );
andrew.say_hello()

