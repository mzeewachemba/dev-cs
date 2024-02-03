using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{
    internal class BankInfo
    {
        string firstName;
        public string FirstName
        {
            get { return firstName; }
            set { firstName = value; }
        }
        string lastName;
        public string LastName
        {
            get { return lastName; }
            set { lastName = value; }
        }
        string bankName;
        public string BankName
        {
            get { return bankName; }
            set { bankName = value; }
        }
        long checkingAccountNum;
        public long CheckingAccountNum
        {
            get { return checkingAccountNum; }
            set { checkingAccountNum = value; }
        }
        long savingAccountNum;
        public long SavingAccountNum
        {
            get { return savingAccountNum; }
            set { savingAccountNum = value; }
        }
    }
}
