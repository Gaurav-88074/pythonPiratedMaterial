def computeCommission(sales):
    if sales<=50000:
        return 0
    else:
        return 0.05*sales
def remark(sales):
    if sales>=80000:
        return "Excellent"
    elif sales>=60000 and sales<80000:
        return "Good"
    elif sales>=40000 and sales<60000:
        return "Average"
    else:
        return "Word Hard"

if __name__ == '__main__':
    totalSales = []

    week1 = int(input("Sales in first  week : "))
    totalSales.append(week1)
    week2 = int(input("Sales in second week : "))
    totalSales.append(week2)
    week3 = int(input("Sales in third  week : "))
    totalSales.append(week3)
    week4 = int(input("Sales in fourth week : "))
    totalSales.append(week4)

    salesManData={}

    salesManData["totalSales"] = sum(totalSales)
    salesManData["commission"] = computeCommission(sum(totalSales))
    salesManData["remarks"]    = remark(sum(totalSales))

    print()
    print("Total Sales : {0}".format(salesManData["totalSales"]))
    print("Commission  : {0}".format(salesManData["commission"]))
    print("Remarks     : {0}".format(salesManData["remarks"]))
    
    