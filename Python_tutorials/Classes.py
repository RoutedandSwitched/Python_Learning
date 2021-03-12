#!/usr/bin/env python3

class Person: #{
    def put_name(self, name_to_be_set_as ): #{
        self.name = name_to_be_set_as;
    #}

    def say_hello(self):#{
        print( self.name + ' says hello!' );
    #}
#}

doug = Person();
kevin = Person();

kevin.put_name("Kevin Smith");

doug.put_name("Doug Peterson");

doug.say_hello();

kevin.say_hello();
