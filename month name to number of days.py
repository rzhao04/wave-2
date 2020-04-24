month = str
month = raw_input ("what is month: ")
if (month in ["january", "march", "may", "july", "august", "october", "december"]):
    print ("31 days") 
if (month in ["april", "june", "september", "november"]):
    print ("30 days")
if (month == "february"):
    print ("28 or 29 days")