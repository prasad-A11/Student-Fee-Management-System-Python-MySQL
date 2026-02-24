from db_connection import db_connection_funt
a = db_connection_funt()
curObj= a.cursor()   # cursor object is used to execute sql querys and fetch the data



# this delecting the task which uploded by students.........
def Delete_uploaded_tasks():
    print("hey....your going to deleting the uploaded task.....")
    option = int(input("Enter your option to accesss........"))
    if option ==  1:
        upload_id = int(input("Enter your uploded ID to delete here:----"))
        query =  "delete from student_uploaded_tasks  where upload_id = %s"
        curObj.execute(query,(upload_id,))
        a.commit()
        print("hey...your sucessfully deleted the uploaded tasks in portal.....")
        
    elif option == 2:    
        stu_admNo  = int(input("Enter your uploded ID to delete here:----"))
        query =  "delete from student_uploaded_tasks  where stu_admNo = %s"
        curObj.execute(query,(stu_admNo,))
        a.commit()
        print("hey...your sucessfully deleted the uploaded tasks in portal.....")
    elif option == 3:
        task_id  = int(input("Enter your uploded ID to delete here:----"))
        query =  "delete from student_uploaded_tasks  where task_id = %s"
        curObj.execute(query,(task_id,))
        a.commit()
        print("hey...your sucessfully deleted the uploaded tasks in portal.....")
    else:
        print("invalid upload_id/admNo/task_id.....please check again...")




# uploading the student task in table
def upload_task():
    print("hoo...your going to uploading the new tasks here...... ")
    stu_id = int(input("Enter your Admission Number: "))
    task_id = int(input("Enter the Task ID you want to upload: "))
    upload_link = input("Enter your submission link: ")
    upload_date = input("Enter upload date (yyyy-mm-dd): ")
    query = "insert into student_uploaded_tasks (stu_admNo, task_id, upload_link, upload_date) values (%s, %s, %s, %s)"
    curObj.execute(query,(stu_id, task_id, upload_link, upload_date))
    a.commit()
    print("hey..sucessfully your upload yoour task in portal..........")
    
    




# this update the student profile there details 
def update_profile():
    print("now you can able to update your profile.....")
    print("1. update name:--")
    print("2. update age:--")
    print("3. update both name and age:-")
    
    option = int(input("Enter your above option to access:---"))
    if option == 1:
        stu_name = input("Enter a students name to update:--")
        stu_admNo = int(input("Enter the student admission numbers :---"))
        query = "update students set stu_name = %s where stu_admNo = %s"
        curObj.execute(query,(stu_name,stu_admNo,))
        a.commit()
        print("sucessfully updated your name in portal................. ")
    elif option == 2:
        stu_age = int(input("Enter your updated age here:---"))
        stu_admNo = int(input("Enter your admission ID here:---"))
        query = "update students set stu_age = %s where stu_admNo = %s"
        curObj.execute(query,(stu_age,stu_admNo,))
        a.commit()
        print("sucessfully updated your age in portal now.........")
    elif option == 3:
        stu_name = input("Enter a students name to update:--")
        stu_age = int(input("Enter your updated age here:---"))
        stu_admNo = int(input("Enter your admission ID here:---"))
        query = "update students set stu_name = %s, stu_age = %s where stu_admNo = %s"
        curObj.execute(query,(stu_age,stu_admNo,))
        a.commit()
        print("sucessfully updated your both NAME and AGE in portal now.........")   
    else:
        print("invalid id or age/name")        




# it get recording classes data from portal by student 
def get_recording_class():
    print("1. view all tasks")
    print("2 view by only id")
    
    option = int(input("Enter your options....."))
    
    if option == 1:
        query = "select recording_id,class_name,recorded_date,video_link from recordings"
        curObj.execute(query)
        tasks = curObj.fetchall() 
        print(tasks)
    elif option == 2:
        task_id = int(input("Enter your task ID:---"))
        query = " select recording_id,class_name,recorded_date,video_link from recordings where recording_id  = %s"
        curObj.execute(query,(task_id,))
        task = curObj.fetchone()
        print(task)
    else:
        print("No task found with that ID.")
    



# student getting the details of tasks from portal......
def get_tasks():
    print("1. view all tasks")
    print("2 view by only id")
    
    option = int(input("Enter your options....."))
    
    if option == 1:
        query = "select task_id, task_topic, task_doc, task_issued_date from tasks"
        curObj.execute(query)
        tasks = curObj.fetchall() 
        print(tasks)
    elif option == 2:
        task_id = int(input("Enter your task ID:---"))
        query = "select task_id, task_topic, task_doc, task_issued_date from tasks where task_id = %s"
        curObj.execute(query,(task_id,))
        task = curObj.fetchone()
        print(task)
    else:
        print("No task found with that ID.")



