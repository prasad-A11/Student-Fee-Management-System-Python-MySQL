
from db_connection import db_connection_funt
a = db_connection_funt()
curObj= a.cursor()   # cursor object is used to execute sql querys and fetch the data
  
  
  
def add_tasks():
    print("adding the new tasks....")
    task_id = int(input("Enter your task number:---"))
    task_topic = input ("Enter your topic here:---")
    task_doc = input("Enter your doc links here:----")
    task_issued_date = input("enter your issued date (yyyy-mm-dd):--")
    query = "insert into tasks (task_id,task_topic,task_doc,task_issued_date ) values (%s,%s,%s,%s)"
    curObj.execute(query,(task_id,task_topic,task_doc,task_issued_date))
    a.commit()
    print("uploaded sucessfully tasks......")


def add_class_recording():
    print("addding the recording class upto date")
    recording_id = int(input("Enter your class id:-----"))
    class_name = input("Enter the recorded class course name:--")
    recorded_date = input("Enter the record date (yyyy-mm-dd):---")
    video_link = input("enter your recorded class link:----")
    query = "insert into recordings (recording_id,class_name,recorded_date,video_link) values (%s,%s,%s,%s)"
    curObj.execute(query,(recording_id,class_name,recorded_date,video_link))
    a.commit()
    print("uploaded recording class sucessfully by you.......")    
    
       
                 
def delete_student():     #delete students details
    print("your are deleting the students details... ")  
    print("your are update the student details.... .")                  
    s_id = int(input("Enter your student id for updating his details..."))
    query = "delete from students where stu_admNo = %s"
    curObj.execute(query,(s_id,))
    a.commit()
    print("you sucessfully delete the student....")              
                 
                 
def update_student():       # update
    print("your are update the student details.... .")                  
    s_id = int(input("Enter your student id for updating his details..."))
    s_y = int(input("Enter your year of student to updated.."))
    query = "update students set stu_year = %s where stu_admNo = %s"
    curObj.execute(query,(s_y,s_id))
    a.commit()
    print("you sucessfully update the student....")
   
   
def get_student():  #get the details
    print("your are in the getting student feature..... ") 
    print("you want all students or few students:--")
    option = input("Enter your option all or few:--- ")
    if option == "all":
        query = "select * from students"
        curObj.execute(query)
        allStuData =  curObj.fetchall()
    else:
        ceriteria = int(input("Enter your year:--"))
        ceriteria2 = input("Enter your student dept:---")
        query = "select * from students where stu_year= %s  and stu_dept = %s"
        curObj.execute(query,(ceriteria,ceriteria2))
        few = curObj.fetchall()
        print(few,"few")
                  
                  
                  
def add_student():      # add details 
    s_adNo = int(input("Enter your admission number:------"))
    s_Name =  input("Enter your name here:------")
    s_age =  int(input("Enter your age here:----"))
    s_year = int(input("Enter which year student :--------"))
    s_dept =  input("Enter which department :--------")
    
    query = "insert into students (stu_admNo,stu_name,stu_age,stu_year,stu_dept) values(%s,%s,%s,%s,%s)"
    curObj.execute("insert into students (stu_admNo,stu_name,stu_age,stu_year,stu_dept) values(%s,%s,%s,%s,%s)",(s_adNo,s_Name,s_age,s_year,s_dept))
    a.commit()
    print("addedd sucessfully to db")