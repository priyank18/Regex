#------------------------------------------------------
# It's a programs that extracts email address from a text file
#
# Author: Priyank Srivastava
#-------------------------------------------------------

import re

try:
   # Opening the file and reading it.
   buffer = open("Testfile")
   text = buffer.read()

   #Regular Expression to extract phone numbers
   #numberRegex = '^\w\d|\d+-\d+-\d+|\d+'
   numberRegex = '\d\d\d\d\d\d\d\d\d\d|\d\d\d-\d\d\d-\d\d\d\d'
   pattern2 = re.findall(numberRegex,text)
   
   #Regular Expression to find email addresses. 
   emailRegex = "[\w.-]+@[\w.-]+[\w-]"
   pattern3 = re.findall(emailRegex,text)

   #Printing the output
   print pattern2
   print "\n","Phone Numbers:\n"
   for number in pattern2:
      print number
   print "\n","Email Addresses:\n"
   for email in pattern3:
      print email

except:
   print "\n An error occured please try again later\n"
