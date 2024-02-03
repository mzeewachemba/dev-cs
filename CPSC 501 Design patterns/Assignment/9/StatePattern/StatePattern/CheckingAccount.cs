using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Windows.Forms.AxHost;

namespace StatePattern
{
    //context for state
    internal class CheckingAccount : ICheckingActivity
    {
        public CheckingAccount(string cname, int acctNum)
        {
            customerName = cname;
            accountNum = acctNum;
            state = new SilverState(0, this);
        }

        // current state
        BaseState state;
        internal BaseState State
        {
            get { return state; }
            set { state = value; }
        }
        string customerName;
        public string CustomerName
        {
            get { return customerName; }
        }
        int accountNum;
        public int AccountNum
        {
            get { return accountNum; }
        }
        double balance;
        public double Balance
        {
            get { return balance; }
        }
        //methods for checking account
        public void WithDrawMoney(double amt)
        {
            state.WithDrawMoney(amt);
        }
        public void DepositMoney(double amt)
        {
            state.DepositMoney(amt);
        }
        public void AddInterest()
        {
            state.AddInterest();
        }
    }
}
