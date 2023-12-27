using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{
    internal class BalanceCheckUS : IBalanceCheck
    {//implementation of balance check for the US
        public double GetCurrentBalances(List<BankInfo> BInfoList)
        {
            // call each banks service to obtain info
            double bal = 0;
            if (BInfoList.Count > 0)
            {
                if ((BInfoList[0].FirstName.ToUpper() == "BILL") &&
                (BInfoList[0].LastName.ToUpper() == "BAKER"))
                    bal = 5728;
                if ((BInfoList[0].FirstName.ToUpper() == "SALLY") &&
                (BInfoList[0].LastName.ToUpper() == "SIMPSON"))
                    bal = 14455;
            }
            return bal;
        }
        public double GetCurrentLoans(List<BankInfo> BInfoList)
        {
            // call each banks service to obtain info
            double loanamt = 0;
            if (BInfoList.Count > 0)
            {
                if ((BInfoList[0].FirstName.ToUpper() == "BILL") &&
                (BInfoList[0].LastName.ToUpper() == "BAKER"))
                    loanamt = 10000;
                if ((BInfoList[0].FirstName.ToUpper() == "SALLY") &&
                (BInfoList[0].LastName.ToUpper() == "SIMPSON"))
                    loanamt = 5000;
            }
            return loanamt;
        }
    }
}
