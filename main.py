# Author: Chang Li cxl5844@psu.edu
# Collaborator:axa6066@psu.edu
# Collaborator:tmd5681@psu.edu
# Section: 1
# Breakout: 14

#include <stdio.h>
#include <readline/readline.h>
#include <stdlib.h>

  char *a = readline("Enter your CMPSC 131 grade: ");
  double g = atof(a);
  if g<60:
    printf("Your letter grade for CMPSC 131 is F.\n");
  }
  elif g<70:
    printf("Your letter grade for CMPSC 131 is D.\n");
  }
  elif g<77:
    printf("Your letter grade for CMPSC 131 is C.\n");
  }
  elif g<80:
    printf("Your letter grade for CMPSC 131 is C+.\n");
  }
  elif g<83:
    printf("Your letter grade for CMPSC 131 is B-.\n");
  }
  elif g<87:
    printf("Your letter grade for CMPSC 131 is B.\n");
  }
  elif g<90:
    printf("Your letter grade for CMPSC 131 is B+.\n");
  }
  elif g<93 :
    printf("Your letter grade for CMPSC 131 is A-.\n");
  
  else :
    printf("Your letter grade for CMPSC 131 is A.\n");
  