
d={"9247":{"age":20,
           "grades":{"math":15,
                     "chem":14},
           "year":1397
           },
   "9248":{"age":21,
           "grades":{"math":18,
                     "chem":13},
           "year":1396
           }
   }

id=input("Enter the student ID :")
print("age : ",d[id]["age"])
print("grade math : ",d[id]["grades"]["math"])
print("grade chem : ",d[id]["grades"]["chem"])
print("year : ",d[id]["year"])

d["9247"]["grades"]["physics"]=10
d["9248"]["grades"]["physics"]=20
print("9247 grade physics : ",d["9247"]["grades"]["physics"])
print("9248 grade physics : ",d["9248"]["grades"]["physics"])

