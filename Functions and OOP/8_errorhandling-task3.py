"""
Bank ATM
This exception handling scenario deails with the exceptional cases that arise in the ATM of a bank.

About the ATM:
This is a special kind of ATM that takes three integer inputs from the user, one-by-one.
They are:
1. balance - Current Balance of the account.
2. choice - Choice of purpose, that is, Deposit(1) or Withdraw(2).
3. amount - Amount of Deposit or Withdrawal.

Write the function definition for the function 'Bank_ATM', that takes 3 parameters, which are the above 3 inputs.
As per the minimum balance policy of the bank, the balance amount must be at least 500.
1. Raise ValueError exception if the input for the current balance is less than '500' and Print the Message.
The message to the user must be, "As per the Minimum Balance Policy, Balance must be at least 500".

The input for the option 'choice' will be either '1' or '2', '1' for Deposit and '2' for Withdrawl.

The minimum amount for deposit in this ATM is 2000.

2. Raise a User-Defined exception "MinimumDepositError" if the input for the deposit amount is less than '2000', and Print the Message.
This message to the user must be, "The Minimum amount of Deposit should be 2000."
else
'Add' the deposit amount to the 'Balance'.

As per the minimum balance policy of this bank, the balance amount must be at least 500.
So in case of withdrawal:
3. Raise a User-Defined exception "MinimumBalanceError",
if the balance amount after withdrawal is less than '500' and Print the Message.
The message to the user must be, "You cannot withdraw this amount due to Minimum Balance Policy".
else
'Subtract' the withdrawn amount from the 'Balance'.

If any transaction has taken place:
4. Print the updated balance as "Updated Balance Amount: 5500".

"""


class MinimumDepositError(Exception):
    def __init__(self):
        print("The Minimum amount of Deposit should be 2000.")


class MinimumBalanceError(Exception):
    def __init__(self):
        print("You cannot withdraw this amount due to Minimum Balance Policy")


def Bank_ATM(balance, choice, amount):
    # Write your code here
    try:
        if balance < 500:
            raise ValueError(
                "As per the Minimum Balance Policy, Balance must be at least 500"
            )
    except ValueError as e:
        print(e)
    else:
        # deposit
        if choice == 1:
            try:
                if amount < 2000:
                    raise MinimumDepositError
            except:
                pass
                # print("There are other errors with deposits")
            else:
                balance += amount
                print(f"Updated Balance Amount:  {balance}")

        # withdraw
        elif choice == 2:
            try:
                if balance - amount < 500:
                    raise MinimumBalanceError
            except:
                pass
                # print("There are other errors with withdrawals")
            else:
                balance -= amount
                print(f"Updated Balance Amount:  {balance}")
