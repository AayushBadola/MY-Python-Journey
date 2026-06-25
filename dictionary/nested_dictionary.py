# nested dictionary is adding multiple dictionary inside of a main dictionary 
# For storing more information and also correlating info 
# ALTERNATE THINKING : nested dictionary is a  subquery for complex data storage instead of retriva

Master_dict = {
    "student1" : {
        "Class" : "CSE",
        "Enrollment" : 58,
        "Name": "Aayush"
    },

    "student2" : {
        "Class" : "CSE",
        "Enrollment" : 59,
        "Name" : "Andrew"
    }  

    
}

#master dictionary still needs key value pairs
#hence master dictionary has key student 1 and student 2
#with student 1 and student 2 having values in the form of dictionaries

# ACCESSING NESTED DICETIONARY -> dict_name[dict1][attribute]
print(Master_dict["student1"]["Name"])

