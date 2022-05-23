# Dictionaries

data_eng_37 = {
    "course name" : "Data Eng 37",
    "client": "Home Office",
    "trainer": "David"


}
print(data_eng_37, type(data_eng_37))

print(data_eng_37["client"]) # Dictionary Name [ key ]

data_eng_37["trainer"] = "David Harvey"
data_eng_37["trainees"] = ["Munir", "Darnell", "Abhi", "Ahmed"]

print(data_eng_37)

print(data_eng_37["client"])

print(data_eng_37["trainer"])

print(data_eng_37.get("missing"))

data_eng_37.update({"course_length": "8 weeks"})

movies = {
    "Batman" : "Action",
    "Shrek" : "Comedy",
    "Romeo and Juliet":"Romance",
    "Pinnochio": "Animation"

}
print(movies)

print(movies["Batman"])

print(movies, type(movies))

print(movies.keys())

print(movies.values())

print(movies.items())

print(f"Adz fav movie is {}. It has a runtime of {} minutes and directed by {}.")