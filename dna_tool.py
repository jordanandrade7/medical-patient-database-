#Import modules
from Patient import Patient
import random

#initialize global variable
random.seed(5) # random seed used for reproducibility
LENGTH_DNA=20

########################
##### Functions ########
########################

def display_menu():   #displays options
    """ Display all the options, no input, no output """
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")


def random_base():   #returns bases
    """select the letter A,C,G,T at random, output (String) """
    bases=["A","C","G","T"]
    return random.choice(bases)

def initialize():   #list of all patients attributes
    name="Andrea"
    age=37
    strand=random_strand()   #gives teh random strand
    patient1=Patient(name,age,strand)   #of class Patient

    name="Bob"
    age=28
    strand=random_strand()
    patient2=Patient(name,age,strand)   #of class Patient

    name="Brooke"
    age=34
    strand=random_strand()
    patient3=Patient(name,age,strand)   #of class Patient


    name="Connor"
    age=27
    strand=random_strand()
    patient4=Patient(name,age,strand)   #of class Patient

    name="James"
    age=25
    strand=random_strand()
    patient5=Patient(name,age,strand)   #of class Patient


    name="Jenna"
    age=44
    strand=random_strand()
    patient6=Patient(name,age)   #of class Patient


    name="John"
    age=45
    strand=random_strand()
    patient7=Patient(name,age,strand)   #of class Patient


    name="Julie"
    age=37
    strand=random_strand()
    patient8=Patient(name,age,strand)   #of class Patient


    name="Kate"
    age=48
    strand=random_strand()
    patient9=Patient(name,age,strand)   #of class Patient


    name="Kieth"
    age=28
    strand=random_strand()
    patient10=Patient(name,age,strand)   #of class Patient


    name="Kelly"
    age=25
    strand=random_strand()
    patient11=Patient(name,age,strand)   #of class Patient
    
    name="Luke"
    age=33
    strand=random_strand()
    patient12=Patient(name,age,strand)   #of class Patient
    
    name="Mark"
    age=34
    strand=random_strand()
    patient13=Patient(name,age,strand)   #of class Patient

    name="Pat"
    age=26
    strand=random_strand()
    patient14=Patient(name,age,strand)   #of class Patient

    name="Taylor"
    age=30
    strand=random_strand()
    patient15=Patient(name,age,strand)   #of class Patient

    name="Tony"
    age=55
    strand=random_strand()
    patient16=Patient(name,age,strand)   #of class Patient

    patients=[patient1,patient2,patient3,patient4,patient5,patient6,patient7,patient8,patient9,patient10,patient11,patient12,patient13,patient14,patient15,patient16]   #list of patients
    return patients

def display(L):   #prints each attribute of the patients in class Patient
    patient_info=len(L)
    for i in range(patient_info):
          print(L[i].name,L[i].age,L[i].strand,sep="\t")   #scans list and prints all the patients

def random_strand():   #creates random strand
    strands=""   #intialize an empty string
    for i in range(LENGTH_DNA):
        strands=strands+random_base()
    return strands   #returns strand of dna

def info(L):
    n=0   #counter for under 20
    t=0   #counter for 20s
    r=0   #counter for 30s
    f=0   #counter for 40s
    g=0   #counter for 50s
    s=0   #counter for above 60
    age_total=0   #adds all patients ages
    (p_under20,p_20,p_30,p_40,p_50,p_60)=0,0,0,0,0,0
    
    patients_total=len(L)
    for i in range(patients_total):
        age_total=age_total+L[i].age
        if L[i].age<20:
            n=n+1   #adds one to n everytime if condition is true
            p_under20=(n/patients_total)*100   #percent=(n/total)*100
            
        elif L[i].age>=20 and L[i].age<=29:
            t=t+1
            p_20=(t/patients_total)*100

        elif L[i].age>=30 and L[i].age<=39:
            r=r+1
            p_30=(r/patients_total)*100
            

        elif L[i].age>=40 and L[i].age<=49:
            f=f+1
            p_40=(f/patients_total)*100

        elif L[i].age>=50 and L[i].age<=59:
            g=g+1
            p_50=(g/patients_total)*100

        elif L[i].age>=60:
            s=s+1
            p_60=(s/patients_total)*100
    
        
    print("<20:"+str(p_under20)+"%")   #print statements for each age category
    print("20's:"+str(p_20)+"%")
    print("30's:"+str(p_30)+"%")
    print("40's:"+str(p_40)+"%")
    print("50's:"+str(p_50)+"%")
    print(">=60:"+str(p_60)+"%")
    print("Age Mean:",age_total/patients_total)
    return (p_under20,p_20,p_30,p_40,p_50,p_60,age_total,patients_total)

def add_new_patient(L):   #adds new patient to list
    entry_name=input("Enter Name: ")
    entry_age=input("Enter Age: ")
    entry_strand=input("Enter DNA strand: ")
    if len(entry_strand)!=20:   #if the entry is not a length of 20
        print("DNA strand needs to be 20 characters, try again.")
        entry_strand=input("Enter DNA strand: ")   #gives user another try
    else:
        name=entry_name
        age=entry_age
        strand=entry_strand
        new_patient=Patient(name,age,strand)
        L=L+[new_patient]   #adds patient to the list
    return L

def compare(p1,p2):   #compares two dna strands
    compared_strand=""   #intialize an empty string
    for i in range(20):   
        if p1.strand[i]==p2.strand[i]:   #if dna base matches it is equal to that specific base
            s=p1.strand[i]
            compared_strand=compared_strand+s
        else:
            s="x"   #if dna base is not equal, adds an "x"
            compared_strand=compared_strand+s
    return compared_strand


def check_completeness(C):    #returns the similiarity percentage of the dna strands
    counter=0
    compared_strand=[C]   #calls return statement of compare function
    for i in range(20):
        if C[i]=="x":   #if "x" counter increases
            counter=counter+1
        else:
            counter=counter+0
    similiar_per=(((20-counter)/20)*100)   #similiar percent equals (20-"x"=amount of similiar bases), (similiar_bases/20)*100 equals percent similiar
    return similiar_per

######this function was working, im not sure why it isnt anymore

def compare_all(L):   #compares all patients dna strand and returns similiarities above 33%
    total_patients=len(L)
    for i in range(total_patients):   #scans through first patients then moves onto the next
        for j in range(i,total_patients): #scans through all the patients
            C=compare(L[i],L[j])
            P=check_completeness(C)
            similiar_per=(P)
            if P>33 and L[i].name!=L[j].name:   #percentage has to be above 33% and name=name
                print(str(L[i].name)+" vs "+str(L[j].name)+" "+str(similiar_per)+"%")

########sorry i was not able to finsih this function
#def find_pattern(L,r):   #finds the condition in every patient
    #cc=len(r)  #len of the user input
    #counter=0  #counts the amount of patients
    #for i in L:
        #for j in range(LENGTH_DNA-cc+1):   #20-cc
            #if i.strand[j:j+n]==r:   #from j to j+cc-1
                #i.has_condition="True"
                #counter=counter+1
                #break
            #else:   #when the condition is not found in the patient
                #i.has_condition="False"
    #return counter
          
    






##########################
########## Main Function #  to uncomment step by step fo testing
##########################
                
def main():
    ##################### TEST FOR OPTION 1
    print("\n****TEST the random_strand function****")
    print(random_strand())

    ##################### TEST FOR OPTION 1
    print("\n****TEST the class Patient****")
    patient=Patient("Tom",20,random_strand())
    print(patient.name,patient.age,patient.strand)
    
    ##################### TEST FOR OPTION 1
    print("\n****TEST the display function****")
    patients=[patient,Patient()]
    patients[1].name="Lucy"
    patients[1].age=25
    patients[1].strand="TCTTGTAAACTCGGAAACTG"
    display(patients)

    ##################### TEST FOR OPTION 2
    print("\n****TEST the info function****")
    info(patients)

    ###################### TEST for OPTION 4
    print("\n****TEST the add_new_patient function****")
    patients=add_new_patient(patients)
    display(patients)
    
    ###################### TEST for OPTION 5
    print("\n****TEST the compare function****")
    common_strand=compare(patients[0],patients[1])
    print(common_strand)

    ###################### TEST for OPTION 5
    print("\n****TEST the check_completness function****")
    print(check_completeness(common_strand))

    
    
if __name__=="__main__":
    main()
    
