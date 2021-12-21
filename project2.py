'''------------------------------------------------------
                 Import Modules 
---------------------------------------------------------'''
import dna_tool as dna

'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
print("===============")
print("\nDNA Analyzer and Patient Management Tool")
print("===============")
L=dna.initialize()
#k=""
# closed loop, keep executing until user press enter
while True:
    dna.display_menu()   #menu that contains all the options
    command=input("Enter Command (Enter to exit): ")
    
    if command=="":   #if enter the program ends
        print("Thanks for using this tool\nCome back soon!")
        break

    elif command=="1":   #displays list of patients and attributes
        print("Name","Age","DNA-strand (20 length)",sep="\t")
        print("---------------------------------------------")
        dna.display(L)   #calls display function
        
    elif command=="2":   #displays age category and mean 
        print("#Patients ",len(L))
        dna.info(L)   #calls info function

    elif command=="3":   #removes patient
        index=int(input("Which polynomial would you like to remove? "))   #user chooses patient they would like to remove
        if not(1<=index<=len(L)):   #has to be in range
            continue
        del(L[index-1])

    elif command=="4":   #adds new patient
        L=dna.add_new_patient(L)   #updates list of patients

    elif command=="5":   #comapres dna strands 
        p1=int(input("First patient (enter number): "))
        p2=int(input("Second patient (enter number): "))
        C=dna.compare(L[p1-1],L[p2-1])
        compared_strand=C   #calls return statment of dna.compare
        F=dna.check_completeness(C)
        similiar_per=F   #calls return statement of check_completeness
        if not(1<=p1 and p2<=len(L)):   #has to be in range
            continue
        print("Patient",p1,"and",p2,"common strand is",compared_strand)
        dna.check_completeness(C)   #calls check completeness function
        print("They are similiar at",similiar_per,"%")
        

    elif command=="6":   #comapres all patients dna strands and returns similiarites above 33%
        dna.compare_all(L)   #calls compare_all function

    ########sorry i was not able to finsih this function
    #elif command=="7":
        #k=input("Which condition are you looking for:")
        #r=input("Enter sequence:")
        #dna.find_pattern(L,r)
        #print("Patients with "+str(k)+" condition:"+str(counter/len(L))+"%")
       
    
    
        
    
