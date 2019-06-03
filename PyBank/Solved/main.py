import os
import csv

budget_file_path=os.path.join("Resources","budget_data.csv")
output_file_path=os.path.join("Resources","output_data.txt")

with open(budget_file_path) as budget_file:
    budget_reader=csv.reader(budget_file,delimiter=",")
    print(budget_reader)

    csv_header = next(budget_reader)

    print(f"CSV Header: {csv_header}")
    row_count=0
    netprofitLoss=0
    greatestIncrease=0
    currDiff=0
    previousNumber=0
    greatestDecrease=0
    totalProfit=0
    totalLoss=0
    sum=0
    for row in budget_reader:
        row_count = row_count + 1 
        netprofitLoss=netprofitLoss+int(row[1])
        currDiff=int(row[1])-previousNumber
        sum=sum+currDiff
        previousNumber=int(row[1])
        if currDiff > greatestIncrease:
            greatestIncrease=currDiff
        if currDiff < greatestDecrease:
            greatestDecrease=currDiff
        if int(row[1]) >= 0:
           totalProfit = totalProfit + int(row[1])
        else:
            totalLoss = totalLoss + int(row[1])           
    print("Financial Analysis")
    print("----------------------------")   
    print("Total Months: " + str(row_count))
    print("Average  Change: " )  
    print("Greatest Increase in Profits: ($" + str(greatestIncrease)+ ")")   
    print("Greatest Decrease in Profits: ($" + str(greatestDecrease) + ")")   

    print(netprofitLoss,greatestIncrease,greatestDecrease,totalProfit,totalLoss)   

with open(output_file_path,"w") as output_file:
        # csvwriter=csv.writer(output_file ,delimiter=' ')   
        output_file.write("Financial Analysis\n")
        output_file.write("----------------------------\n")   
        output_file.write("Total Months:" + str(row_count) + "\n")
        output_file.write("Average Change:" + "\n")  
        output_file.write("Greatest Increase in Profits: ($" + str(greatestIncrease)+ ")" + "\n")   
        output_file.write("Greatest Decrease in Profits: ($" + str(greatestDecrease) + ")" + "\n") 