school ={
    "Favour": {"score":[40, 77, 85]},
    "Blessing": {"score": [79, 58, 36]},
    "Peace": {"score": [55, 89, 43]},
    "Nicole": {"score": [38, 19, 26]}
}

def calculate_result(score):
    Total = 0
    for num in score:
        Total += num
    Average = Total / len(score)
    return Total, Average
    
for student in school:
    print(" ")
    print(student)
    Total, Average = calculate_result(school[student]["score"])
    print(f"Total: {Total}")
    print(f"Average: {Average:.2f}")
    if Average >= 50:
        print("status: PASS")
    else:
        print("status: FAIL")


