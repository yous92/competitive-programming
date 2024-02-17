if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
    lowest_score = sorted_students[0][1]
    for i in range(1, len(sorted_students)):
        if sorted_students[i][1] > lowest_score:
            second_lowest_score = sorted_students[i][1]
            break
      
    for element in sorted_students:
        if element[1] == second_lowest_score:
            print(element[0])
        
