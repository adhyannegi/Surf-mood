##########################################################################
#    Computer Project #5
#    Algorithm
#        Prompt to input a year.
#        3 functions defined.
#        Main function to call all defined functions wherever needed.
#        Calls function and returns value based on user input.
##########################################################################

def open_file():
     ''' 
     Tries to open file based on user input and returns file pointer.
     Value: Takes no value.
     Returns: File pointer.
     '''
     ans = True
     while ans:
         year = input("Input a year: ")    #user input
         file_name = "wave_data_" + year + ".txt"    #creates file name
         try:
             f1 = open(file_name, "r")    #tries to open file
             return f1
             ans = False
         except FileNotFoundError:
             print("File does not exist. Please try again.")    #loop continues
            
            
def get_month_str(mm):
     ''' 
     Converts numeric string into a 3-character string month abbreviation.
     Value: String.
     Returns: String.
     '''
     #Returns values based on month number
     if mm == "01":
         return "Jan"
     elif mm == "02":
         return "Feb"
     elif mm == "03":
         return "Mar"
     elif mm == "04":
         return "Apr"
     elif mm == "05":
         return "May"
     elif mm == "06":
         return "Jun"
     elif mm == "07":
         return "Jul"
     elif mm == "08":
         return "Aug"
     elif mm == "09":
         return "Sep"
     elif mm == "10":
         return "Oct"
     elif mm == "11":
         return "Nov"
     elif mm == "12":
         return "Dec"

def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
     ''' 
     To determine which day and time had the best surf.
     Values: str, str, int, float, float, str, str, int, float, float
     Returns: str, str, int, float, float
     '''
     if 6 < hr < 19:    #best surfing time
         if wvht > best_wvht:    #updates best values based on conditions
             best_mm = mm
             best_dd = dd
             best_hr = hr
             best_wvht = wvht
             best_dpd = dpd
         elif wvht == best_wvht and dpd > best_dpd:
             best_mm = mm
             best_dd = dd
             best_hr = hr
             best_wvht = wvht
             best_dpd = dpd
         else:
             best_wvht = best_wvht
     return best_mm, best_dd, best_hr, best_wvht, best_dpd

def main():  
     
     #intializing best values
     best_mm = ""
     best_dd = ""
     best_hr = 0
     best_wvht = 0.0
     best_dpd = 0.0
     
     print("Wave Data")
     fp = open_file()
     fp.readline()    #skips two header lines
     fp.readline()
     
     #initializing values 
     max_wvht = 0
     min_wvht = 10**6
     total = 0
     count = 0
     
     for line in fp:
         if line[30:36] == "99.00" or line[37:42] == "99.00":
             continue    #spurious values
         mm = line[5:7]    #assigning values 
         dd = line[8:10]
         hr = int(line[11:13])
         wvht = float(line[30:36])
         dpd = float(line[37:42])
         
         #best_surf() function call
         best_mm, best_dd, best_hr, best_wvht, best_dpd = best_surf(mm, dd,\
                hr, wvht, dpd, best_mm, best_dd, best_hr, best_wvht, best_dpd)
         
         total += wvht    #updating variables
         count += 1
         
         if wvht > max_wvht:
             max_wvht = wvht

         elif wvht < min_wvht:
             min_wvht = wvht
     
         average_wvht = total/count    #calculates average
     
     #print statements for final output
     print("\nWave Height in meters.")
     print("{:7s}: {:4.2f} m".format("average", average_wvht))
     print("{:7s}: {:4.2f} m".format("max", max_wvht))
     print("{:7s}: {:4.2f} m".format("min", min_wvht))
     print("\nBest Surfing Time:")
     print("{:3s} {:3s} {:2s} {:>6s} {:>6s}".format("MTH","DAY","HR","WVHT",\
                                                    "DPD"))
     print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s".format(\
                get_month_str(best_mm), best_dd, best_hr, best_wvht, best_dpd))
                #get_month_str() function call
     
     

 # These two lines allow this program to be imported into other code
 # such as our function_test code allowing other functions to be run
 # and tested without 'main' running.  However, when this program is
 # run alone, 'main' will execute.  
if __name__ == "__main__": 
     main()

