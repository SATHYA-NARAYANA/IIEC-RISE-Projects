import os
import pyttsx3
pyttsx3.speak("Welcome to my tools")

print("Welcome to AI world of Agent ARVI")

print("notepad \n firefox \n chrome \n VScode \n eclipse \n VirtualBox \n VLCmedia \n Microsoft Edge \n Anaconda \n git-bash")
pyttsx3.speak("What's your choice")
while True :
     
     print("enter your choice:" ,end="")

     
     p = input()

     if (("run" in p) or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")
     
     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("firefox" in p) or ("mozilla"in p)):
        os.system("firefox")

     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p) or ("google" in p)):
        os.system("chrome")

     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("VScode" in p) or ("visualstudio" in p) or ("code" in p)):
        os.system("code")
   
     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("eclipse" in p) or ("ide" in p)):
        os.system("eclipse")

     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("VirtualBox" in p) or ("virtual" in p)):
        os.system("VirtualBox")
     
     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("VLCmedia" in p) or ("vlc" in p) or ("media" in p)):
        os.system("vlc")

     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("Microsoft" in p) or ("edge" in p) or ("msedge" in p)):
        os.system("msedge")

     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and ("Anaconda3" in p):
        os.system("Anaconda3")

     elif ("run" in p or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("git-bash" in p) or ("git" in p) or ("bash" in p)):
        os.system("git-bash")

     
     else:
        print("dont support")
