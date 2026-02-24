from admin_feature import add_student,get_student,update_student,delete_student,add_tasks,add_class_recording
from students_feature import get_tasks,get_recording_class,update_profile,upload_task,Delete_uploaded_tasks
def admin():     # funtion define as admin
    print("hi, your are in admin portal.........") 
    print("choose your option to proceed to move forward ....--- ")
    print("1. add students details. .")
    print("2. get students  details. .")
    print("3. updating student details..")
    print("4. deleting student details..")
    print("5.  adding tasks..")
    print("6. adding classes recordings..")
    

    
    option = int(input("enter your choice here:-----"))
    if option ==  1:
        add_student()
    elif option == 2:
        get_student()
    elif option == 3:
        update_student()
    elif option == 4:
        delete_student()  
    elif option ==  5:
        add_tasks()
    elif option == 6:
        add_class_recording()
                           

    
#  given below code students credintial access portal..............////////
    
def student():
    print("your are enterd in now students portal.......")   
    print("hey hi...choose option to below to access any one...")
    print("1. get tasks..")
    print("2. get recording class..")
    print("3. update profile..")
    print("4. upload task...")
    print("5. Delete uploaded tasks...")
    
    option = int(input("Enter your option to access..."))
    
    if option == 1:
        get_tasks()
    elif option == 2:
        get_recording_class()
    elif option == 3:
        update_profile()
    elif option == 4 :
        upload_task()
    elif option == 5:
        Delete_uploaded_tasks()                    
    
    
   