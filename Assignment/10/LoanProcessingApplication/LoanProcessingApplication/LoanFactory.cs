using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{
    abstract class LoanFactory
    {
        //each method returns an interface
        public abstract ICreditCheck CreateCreditCheck();
        public abstract IBalanceCheck CreateBalanceCheck();

    }
}
