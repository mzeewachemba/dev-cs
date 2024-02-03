using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{//loan service implementation for canada
    internal class LoanFactoryCanada : LoanFactory
    {
        public override ICreditCheck CreateCreditCheck()
        {
            return new CreditCheckCanada();
        }
        public override IBalanceCheck CreateBalanceCheck()
        {
            return new BalanceCheckCanada();
        }
    }
}
