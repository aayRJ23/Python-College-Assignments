def calculate_efficiency(marksheet_list) :
    count=0
    total_marks=0
    for i in range(0 , len(marksheet_list)) : 
        count+=1
        total_marks+=marksheet_list[i]
    
    return float(total_marks/count)

def main() : 
    n=int(input("Enter the number of marksheet : "))

    list=[]
    for i in range(1,n+1) :
        marks =float(input(f"Enter the marks {i} : "))
        list.append(marks)

    ans = calculate_efficiency(list)
    print(f"The average efficiency of the student is : {ans}")

if __name__ == '__main__' : 
    main()
    