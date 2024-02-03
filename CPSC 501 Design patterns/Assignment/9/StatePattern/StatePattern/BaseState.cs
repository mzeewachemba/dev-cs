using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StatePattern
{
    abstract class BaseState : ICheckingActivity
    {
        CheckingAccount account; // context
        public CheckingAccount Account
        {
            get { return account; }
            set { account = value; }
        }
        double balance; // so that state change can be determined
        public double Balance
        {
            get { return balance; }
            set { balance = value; }
        }
        // ICheckingActivity members
        public abstract void WithDrawMoney(double amt);
        public abstract void DepositMoney(double amt);
        public abstract void AddInterest();
        public void CheckStateChange()
        {
            // decide what the next state will be
            if (balance < 0)
                account.State = new OverDrawState(this);
            if ((balance >= 0) && (balance < 1000))
                account.State = new SilverState(this);
            if ((balance >= 1000) && (balance < 5000))
                account.State = new GoldState(this);
            if (balance >= 5000)
                account.State = new PlatinumState(this);
        }
    }
}
