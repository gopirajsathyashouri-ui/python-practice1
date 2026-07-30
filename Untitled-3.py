
# Build a Late Fee Calculator 

def caluculate_late_fee(borrowed_days, allowed_days, daily_late_fee):
    print("Borrowed Days:", borrowed_days)
    print("Aloowed Days:", allowed_days)
    print("Daily Late Fee: ₹" + str(daily_late_fee))
    if borrowed_days > allowed_days :
        late_days = borrowed_days - allowed_days
        total_late_fee = late_days * daily_late_fee
        print("Total Late Fee: ₹" + str(total_late_fee))
        print("Return status: Late Return.Please collect the late fee.")
        return total_late_fee
    else :
        print("Total Late Fee: ₹0")
        print("Return Status: On-time return.")
        return 0 
    
def solve():
    borrowed_days = int(input())
    allowed_days = int(input())
    daily_late_fee = int(input())
    caluculate_late_fee(borrowed_days, allowed_days, daily_late_fee)

solve()


