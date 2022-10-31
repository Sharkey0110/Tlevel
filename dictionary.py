k = ["Ten","Twenty","Thirty"]
v = [10,20,30]

print(dict(zip(k,v)))


school = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
                }
            }
        }
    }

print(school["class"]["student"]["marks"]["history"])




cv = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
    }


cv["Location"] = cv.pop("city")


cv.pop("name")
cv.pop("salary")

print(dict(reversed(list(cv.items()))))




