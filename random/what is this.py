# what is this?
 
s = input('show me something to look at ')

print('i think this is...',
      
        '\nnumeric:            {}' .format(s.isnumeric()),
        '\nAlpha:              {}' .format(s.isalpha())  ,
        '\nalpha numeric:      {}' .format(s.isalnum())  ,
        '\nhave a lower case:  {}' .format(s.islower())  ,
        '\nHave a upper case:  {}' .format(s.isupper())  ,
        '\nHave a Space        {}' .format(s.isspace())  ,
        '\nis a digit:         {}' .format(s.isdigit())  ,
        '\ntype is:       {}'      .format(type(s))      
        
        )
