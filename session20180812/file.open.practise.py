
import datetime
current_date=open("newtxt with current date.txt","w")
datenow=str(datetime.datetime.now())
current_date.write("this is the new date "+datenow)
current_date.close() 
