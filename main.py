# Author: Chang Li cxl5844@psu.edu
# Collaborator:axa6066@psu.edu
# Collaborator:tmd5681@psu.edu
# Section: 1
# Breakout: 14
def get_LetterGrade(g):
  if g<60 :
    print(f"Your letter grade for CMPSC 131 is F.")
  elif g<70 :
    print(f"Your letter grade for CMPSC 131 is D.")
  elif g<77 :
    print(f"Your letter grade for CMPSC 131 is C.")
  elif g<80 :
    print(f"Your letter grade for CMPSC 131 is C+.")
  elif g<83 :
    print(f"Your letter grade for CMPSC 131 is B-.")
  elif g<87 :
    print(f"Your letter grade for CMPSC 131 is B.")
  elif g<90 :
    print(f"Your letter grade for CMPSC 131 is B+.")
  elif g<93 :
    print(f"Your letter grade for CMPSC 131 is A-.")
  else :
    print(f"Your letter grade for CMPSC 131 is A.")

if __name__ =="__main__":
  a = float(input("Enter your CMPSC 131 grade: "))
  get_LetterGrade(a)