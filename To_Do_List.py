import requests

# BASE_URL = 'https://jsonplaceholder.typicode.com/todos'
BASE_URL = 'http://localhost:3000/todos'

# Get All tasks
def get_tasks():
    r = requests.get(BASE_URL)
    if r.status_code == 200:
        tasks = r.json()
        print("Tasks Retrieved Successfully!")
        for task in tasks[:5]:
            print(task)
    else:
        print("Failed to retrieve tasks:",r.status_code)

# Get Single task 
def get_task(id):
    r = requests.get(f'{BASE_URL}/{id}')
    if r.status_code == 200:
        task = r.json()
        print("Task Retrieved Successfully!")
        print(task)
    else:
        print("Failed to retrieve task:",r.status_code)
        
# Create New task
def create_task(title,completed):
    payLoad = {
        'title':title,
        'completed':completed
    }
    r = requests.post(BASE_URL,json=payLoad)
    if r.status_code == 201:
        create_task = r.json()
        print("New Task created Successfully!",create_task)
        print("Your ID is : ",create_task['id'])
    else:
        print("Failed to create a task:",r.status_code)
    
# Update existing task
def update_task(id,title,completed):
    payLoad = {
        'title':title,
        'completed':completed
    }
    r = requests.put(f'{BASE_URL}/{id}',json=payLoad)
    if r.status_code == 200:
        update_task = r.json()
        print("Task updated Successfully!",update_task)
    else:
        print("Failed to update a task:",r.status_code)

# Delete particular task
def delete_task(id):
    r = requests.delete(f'{BASE_URL}/{id}')
    if r.status_code == 200:
        delete_task = r.json()
        print("Task Deleted Successfully!",delete_task)
    else:
        print("Failed to delete a task:",r.status_code)


while True:
    print('--Enter TO DO--')
    print('''1.GET All Tasks
2.GET Task with ID
3.POST Create New Task
4.PUT Update Task with ID
5.DELETE Task with ID
0.Exit''')
    
    userInput = int(input())

    match userInput:
        case 1:
            get_tasks()
        case 2:
            user_id = input("Enter user_ID :")
            get_task(user_id)
        case 3:
            title = input("Enter Task Title :")
            status = input("Enter Task Status: ")
            create_task(title,status)
        case 4:
            user_id = input("Enter user_ID :")
            title = input("Enter Task Title :")
            status = input("Enter Task Status: ")
            update_task(user_id,title,status)
        case 5:
            user_id = input("Enter user_ID :")
            print('Are you sure you want to delete this Task ?(y/n)')
            confirmation = input().strip().lower()
            if confirmation in ['y','1']:
                delete_task(user_id)
            else:
                break
        case 0:
            print("Exiting")
            break
        case _:
            print("Invalid Choice")



