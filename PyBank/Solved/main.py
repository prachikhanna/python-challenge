import os
import csv

budget_file_path=os.path.join("Resources","budget_data.csv")
output_file_path=os.path.join("Resources","output_data.txt")

with open(budget_file_path) as budget_file:
    budget_reader=csv.reader(budget_file,delimiter=",")
    csv_header = next(budget_reader)

    row_count=0
    row_sum=0
    netprofitLoss=0
    greatestIncrease=0
    currDiff=0
    previousNumber=0
    greatestDecrease=0
    totalProfit=0
    totalLoss=0
    increaseDate=""
    decreaseDate=""
    sum=0
    for row in budget_reader:
        row_count = row_count + 1 
        row_sum=row_sum+ int(row[1])
        if row_count == 1 :
           previousNumber=int(row[1])
           continue
        netprofitLoss=netprofitLoss+int(row[1])
        currDiff=int(row[1])-previousNumber
        sum=sum+currDiff
        previousNumber=int(row[1])
        if currDiff > greatestIncrease:
            greatestIncrease=currDiff
            increaseDate=row[0]
        if currDiff < greatestDecrease:
            greatestDecrease=currDiff
            decreaseDate=row[0]
        if int(row[1]) >= 0:
           totalProfit = totalProfit + int(row[1])
        else:
            totalLoss = totalLoss + int(row[1]) 
    print("Financial Analysis")
    print("----------------------------")   
    print("Total Months: " + str(row_count))
    print("Total : $" + str(row_sum))
    print("Average  Change: $" + str(round(sum/(row_count-1),2)) )  
    print("Greatest Increase in Profits: " + increaseDate + " ($" + str(greatestIncrease)+ ")")   
    print("Greatest Decrease in Profits: " + decreaseDate +" ($" + str(greatestDecrease) + ")")   

with open(output_file_path,"w") as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("----------------------------\n")   
        output_file.write("Total Months:" + str(row_count) + "\n")
        output_file.write("Total : $" + str(row_sum) + "\n")    
        output_file.write("Average Change: $" + str(round(sum/(row_count-1),2)) + "\n")  
        output_file.write("Greatest Increase in Profits: " + increaseDate + " ($" + str(greatestIncrease)+ ")" + "\n")   
        output_file.write("Greatest Decrease in Profits: " + decreaseDate + " ($" + str(greatestDecrease) + ")" + "\n") 