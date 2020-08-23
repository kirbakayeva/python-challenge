import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

#Data
with open(csvpath, 'r', newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #Header
    csv_header = next(csvreader)

    #Values
    dates = []
    total_rev = 0
    maxProfit = 0
    minProfit = 0
    
    #Looping
    for row in csvreader:
        dates.append(row[0])
        #Revenue
        total_rev += int(row[1])

        #Max Profit
        if(maxProfit<int(row[1])):
            maxProfit = int(row[1])
            maxProfitMonth = row[0]
        
        #Min Profit
        if(minProfit>int(row[1])):
            minProfit = int(row[1])
            minProfitMonth = row[0]
    
    #Printing output
    print("\nFinancial Analysis")
    print(f"Total Month: {len(dates)}")
    print(f"Total Revenue : ${total_rev}")
    print(f"Average Change : ${round(total_rev/len(dates),2)}")
    print(f"Greatest Increase in Profits : {maxProfitMonth} ({maxProfit})")
    print(f"Greatest Decrease in Profits : {minProfitMonth} ({minProfit})")

Budget = open('output.txt','w')

#Writing output
Budget.write("Financial Analysis")
Budget.write("\nTotal Month: " + str(len(dates)))
Budget.write("\nTotal Revenue : $" + str(total_rev))
Budget.write("\nAverage Change : $" + str(round(total_rev/len(dates),2)))
Budget.write("\nGreatest Increase in Profits : " + str(maxProfitMonth) + " (" + str(maxProfit) + ")")
Budget.write("\nGreatest Decrease in Profits : " + str(minProfitMonth) + " (" + str(minProfit) + ")")

Budget.close()

