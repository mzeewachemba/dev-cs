using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{
    abstract class LoanFactory //base for all concrete factory classes
    {
        //each method returns an interface
        public abstract ICreditCheck CreateCreditCheck();
        public abstract IBalanceCheck CreateBalanceCheck();

    }
}
