#!/usr/bin/env python3



class Person: #{

    def __init__( self ):#{
        self.name = "Chaz Smith";
        #}
    def __del__( self ):#{
        print(self.name + " has died. ");
        #}

#}

andrew = Person();
del andrew
