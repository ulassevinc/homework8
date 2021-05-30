import datetime
userResponse = input("Do you want to load an account or open a new one ?\nPress 1 key to load an account.\nPress 2 key to open a new one.\n")
if(userResponse == 1):
    accountName =  input("Enter the account name: ")
    fileName = accountName+".txt"
    fhandler = open(fileName)
    if(fhandler == None):
        print("Error: The file not exist!")
else:
    newAccountName = input("Enter the new account name:")
    newAccountName += ".txt"
    fhandler = open(newAccountName,"w")
    lines = []
    lines.append("AccountName\tAccountNumber\tDate\tDescriptionOfTheEntry\tPostingReference\tDebit\tCredit\tDebitBalance\tCreditBalance\n")
    for x in range(3):
        print("Row"+str(x+1))
        AccountName = newAccountName[:-4]
        AccountNumber = "12345678"
        Date = datetime.date.today()
        DescriptionOfTheEntry = input("Description:")
        PostingReference = input("Posting Reference:")
        Debit = input("Debit:")
        Credit = input("Credit:")
        DebitBalance = input("Debit Balance:")
        CreditBalance = input("Credit Balance:")
        lines.append(str(AccountName)+"\t"+str(AccountNumber)+"\t"+str(Date)+"\t"+str(DescriptionOfTheEntry)+"\t"+str(PostingReference)+"\t"+str(Debit)+"\t"+str(Credit)+"\t"+str(DebitBalance)+"\t"+str(CreditBalance)+"\n")
    fhandler.writelines(lines)
    print("New account is created successfully!")
    fhandler.close()