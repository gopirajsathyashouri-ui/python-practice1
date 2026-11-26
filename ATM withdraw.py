def withdraw_money(balance, amount):
    try:
        amount = float(amount)
        if amount > balance:
            return "Error: Insufficient balance."
        remaining_balance = balance - amount
        return remaining_balance
    except ValueError:
        return "Error: Please enter a valid withdrawl.amount"
    except TypeError:
        return "Error: Balance and amount must be numeric."
    except:
        return "Error: Something unexpected happened while processing the withdrawal."

print(withdraw_money(10000, "2500"))
print(withdraw_money(10000, "two thousand"))
print(withdraw_money("10000", 2500))
print(withdraw_money(10000, 3000))
print(withdraw_money("Ten thousand", 2000))