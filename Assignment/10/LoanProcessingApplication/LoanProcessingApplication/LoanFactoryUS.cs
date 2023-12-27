using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{
    internal class LoanFactoryUS : LoanFactory //concrete factory
    {
        public override ICreditCheck CreateCreditCheck()
        {
            return new CreditCheckUS();
        }
        public override IBalanceCheck CreateBalanceCheck()
        {
            return new BalanceCheckUS();
        }
    }
}
