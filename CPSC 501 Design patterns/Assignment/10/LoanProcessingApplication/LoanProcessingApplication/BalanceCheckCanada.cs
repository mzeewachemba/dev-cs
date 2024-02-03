using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{//balance check implementation for canada
    internal class BalanceCheckCanada : IBalanceCheck
    {
        public double GetCurrentBalances(List<BankInfo> BInfoList)
        {
            // call each banks service to obtain info
            double bal = 0;
            if (BInfoList.Count > 0)
            {
                if ((BInfoList[0].FirstName.ToUpper() == "MARK") &&
                (BInfoList[0].LastName.ToUpper() == "MATHEWS"))
                    bal = 6520;
                if ((BInfoList[0].FirstName.ToUpper() == "NANCY") &&
                (BInfoList[0].LastName.ToUpper() == "ADAMS"))
                    bal = 5875;
            }
            return bal;
        }
        public double GetCurrentLoans(List<BankInfo> BInfoList)
        {
            // call each banks service to obtain info
            double loanamt = 0;
            if (BInfoList.Count > 0)
            {
                if ((BInfoList[0].FirstName.ToUpper() == "NANCY") &&
                (BInfoList[0].LastName.ToUpper() == "ADAMS"))
                    loanamt = 200;
                if ((BInfoList[0].FirstName.ToUpper() == "MARK") &&
                (BInfoList[0].LastName.ToUpper() == "MATHEWS"))
                    loanamt = 7000;
            }
            return loanamt;
        }
    }
}
