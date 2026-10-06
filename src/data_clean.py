import pandas as pd

data = {
    "Student_ID": [
        "S001","S002","S003","S004","S005","S006","S007","S008","S009","S010",
        "S011","S012","S013","S014","S015","S016","S017","S018","S019","S020",
        "S021","S022","S023","S024","S025","S026","S027","S028","S029","S030",
        "S031","S032","S033","S034","S035","S036","S037","S038","S039","S040",
        "S041","S042","S043","S044","S045","S046","S047","S048","S049","S050"
    ],

    "Name": [
        "Aarav","Ananya","Rohan","Diya","Arjun","Mehak","Kunal","Simran","Aditya","Neha",
        "Yash","Ishita","Manav","Riya","Dev","Tanya","Harsh","Palak","Vivek","Anjali",
        "Akash","Shreya","Varun","Nidhi","Rahul","Priya","Sahil","Muskan","Ayush","Komal",
        "Abhishek","Khushi","Naman","Saloni","Varun","Nidhi","Rahul","Priya","Sahil","Muskan",
        "Armaan","Isha","Rajat","Pooja","Deepak","Avni","Rishabh","Shivani","Varun","Neha"
    ],

    "Age": [
        20,21,20,19,21,20,22,19,20,21,
        20,19,21,20,22,19,20,21,20,19,
        21,20,22,19,20,21,20,19,21,20,
        22,19,20,21,22,19,20,21,20,19,
        20,21,20,19,21,20,22,19,22,21
    ],

    "Gender": [
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female",
        "Male","Female","M","F","Male","Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male","Female","Male","Female","male","Female"
    ],

    "Study_Hours": [
        5,4,6,3,7,5,2,6,4,5,
        3,7,4,5,2,6,5,4,3,7,
        5,4,6,3,5,None,5,6,3,5,
        2,7,5,4,6,3,5,4,5,6,
        4,5,3,6,4,5,2,7,6,5
    ],

    "Attendance": [
        88,82,91,75,95,87,68,92,80,85,
        72,94,83,89,65,90,86,78,74,96,
        84,81,89,77,88,83,90,93,70,86,
        64,97,85,80,89,77,88,83,90,93,
        81,86,73,91,79,87,66,95,89,85
    ],

    "Previous_Marks": [
        72,68,81,60,85,76,55,79,65,73,
        61,88,70,77,52,82,74,67,59,91,
        75,69,80,63,71,66,78,None,58,74,
        50,89,72,68,80,63,71,66,78,82,
        69,76,58,84,65,75,51,87,80,73
    ],

    "Assignments": [
        8,7,9,6,10,8,5,9,7,8,
        6,10,7,8,4,9,8,6,5,10,
        8,7,9,6,8,7,9,10,5,8,
        4,10,8,7,9,6,8,7,9,10,
        7,8,6,9,7,8,5,10,9,8
    ],

    "Internet": [
        "Yes","Yes","Yes","No","Yes","Yes","No","Yes","Yes","Yes",
        "No","Yes","Yes","Yes","No","Yes","Yes","Yes","No","Yes",
        "Yes","Yes","Yes","No","Yes","Yes","Yes","Yes","No","Yes",
        "No","Yes","Yes","Yes","Yes","No","Yes","Yes","Yes","Yes",
        "Yes","Yes","No","Yes","Yes","Yes","No","Yes","Yes","Yes"
    ],

    "Final_Marks": [
        78,74,86,65,91,82,58,88,70,79,
        64,93,76,84,55,89,80,72,62,95,
        81,73,87,67,77,71,85,90,60,80,
        53,94,79,73,87,67,77,71,85,90,
        74,81,61,88,70,82,56,92,87,79
    ]
}
#Missing values
df = pd.DataFrame(data)
print(df.isnull().sum())  #cheching missing values
df["Study_Hours"]=df["Study_Hours"].fillna(df["Study_Hours"].mean())  #filling issing values
df["Previous_Marks"]=df["Previous_Marks"].fillna(df["Previous_Marks"].mean()) 
print(df.isnull().sum())

#duplicate rows
print(df.duplicated().sum())

#datatypes
print(df.dtypes)

#verifying shape
print(df.shape)

