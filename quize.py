note="""

Welcome to my quize game..

This is a General Knowlade Base quize 

in this quize you will get 10 qution and each qution having 2 points

let's see how much POIN You should socre out of 20
"""
print (note)
class quize:
    scor=0
    qno=0
    def __init__(self,qution,opt1,opt2,opt3,opt4,ans,):
    
        self.qution=qution
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        self.opt4 = opt4
        self.ans = ans

    def check(self):

        quize.qno+=1
        print("\nQution",quize.qno ,"->",self.qution +"\n")
        print("option 1 is",self.opt1)
        print("option 2 is",self.opt2)
        print("option 3 is",self.opt3)
        print("option 4 is",self.opt4)
  
        selct=int(input("\nselect option number :- "))
        
        if self.ans == selct:
            print("\ncorrect!!!!")
           
            quize.scor+=2

        else:
            print("ops..wrong")
        

            
q1=quize("What color does yellow and green make?",'Lime','Maroon','Ocean mist','Tangerine',1)
q1.check()

q2=quize("MS-Word is an example of _____","An operating system",'A processing device',
'Application software',	 'An input device',3)
q2.check()

q3=quize("Ctrl, Shift and Alt are called .......... keys.",'modifier','function','alphanumeric','adjustment',1)
q3.check()

q4=quize('Among the following the maximum covalent character is shown by the compound','MgCl2','FeCl2','SnCl2','AlCl3',4)
q4.check()

q5=quize('National Income estimates in India are prepared by','Planning Commission','Reserve Bank of India',
'Central statistical organisation',	'Indian statistical Institute',3)
q5.check()

q6=quize('The staple food of the Vedic Aryan was','Barley and rice', 'Milk and its products','Rice and pulses','Vegetables and fruits',2)
q6.check()

q7=quize('A computer cannot "boot" if it does not have the _____','Compiler','Loader','Operating system','Assembler',3)
q7.check()

q8=quize('The tropic of cancer does not pass through which of these Indian states ?','Madhya Pradesh','West Bengal','Rajasthan', 'Odisha',4)
q8.check()

q9=quize('Fathometer is used to measure','Earthquakes','Rainfall','Ocean depth','Sound intensity',3)
q9.check()

q10=quize('The purest form of iron is', 'wrought iron','steel','pig iron','nickel steel',1)
q10.check()


print("your Score",quize.scor, "out of 20")






