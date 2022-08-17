import os
from subprocess import os
import pyttsx3
import termcolor
pyttsx3.speak('Welcome to Virtual Assistance world of Agent Voice of haa nyaa')
print(termcolor.colored('\n\t\t\t *********************************\n\t\t\t Welcome to AI world of Agent ARVI',"aqua"))
pyttsx3.speak('Please select one of the provided option given below\n')
print('\n\t\t\t *********************************')
os.system("cls")
print('\n\t\t\t Please select one of the provided option given below')
print('\n\t\t\t ***************************************************\n')
print(" \n\t\t\t Notepad\n\n\t\t\t Open Zoom\n\n\t\t\t Open Paint \n\n\t\t\t Start Minikube \n\n\t\t\t Get Pods \n\n\t\t\t Stop Minikube \n\n\t\t\t Start Minishift \n\n")
  
pyttsx3.speak("Type your application task to be done ")

while True :
     print("\n\t\t\t Type your application task to be done:" ,end="")

     choice = input()

     if (("run" in choice) or ("open" in choice) or ("launch" in choice) or ("execute" in choice)) and (("notepad" in choice) or ("editor" in choice)or ("1" in choice)):
        os.system("notepad")
        break
     
     elif (("run" in choice) or ("open" in choice) or ("launch" in choice) or ("execute" in choice)) and (("zoom" in choice) or ("ZOOM"in choice) or ("2" in choice)):
        os.system("zoom")
        break

     elif (("run" in choice) or ("open" in choice) or ("launch" in choice) or ("execute" in choice)) and (("paint" in choice) or ("Paint"in choice) or ("3" in choice)):
        os.system("mspaint")
        break

     elif (("open" in choice) or ("start" in choice) or ("launch" in choice)) and (("Minikube" in choice) or ("minikube"in choice)):
        os.system("minikube start --driver=virtualbox")
        

     elif (("get" in choice) or("GET" in choice) or ("retrive" in choice)) and (("pods" in choice) or ("PODS"in choice)):
         os.system("minikube stop")
         print('\n\t\t\t')
         os.system("minikube start --driver=virtualbox")
         print('\n\t\t\t')
         os.system("cls")
         os.system("kubectl get pods")
        
        

     elif (("stop" in choice) or ("end" in choice) or ("terminate" in choice)) and (("Minikube" in choice) or ("minikube"in choice)):
        os.system("minikube stop")
        

     elif (("begin" in choice) or ("start" in choice)) and (("Minishift" in choice) or ("minishift"in choice)):
        os.system("minishift.exe start --vm-driver virtualbox --network-nameserver 8.8.8.8")
        break
     else:
      os.system('cls')
      print(termcolor.colored("\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!! \n\t\t\t ERROR \n\t\t\t Enter only available options !!!!","red"))
