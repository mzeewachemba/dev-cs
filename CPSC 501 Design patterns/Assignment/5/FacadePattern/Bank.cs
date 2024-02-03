using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FacadePattern
{
    internal class Bank
    {
        public double GetCurrentCheckingBalance(int accountNum)
        {
            if (accountNum == 12345)
                return 1250;
            else if (accountNum == 12346)
                return 230;
            else
                return 0;
        }
        public double GetSavingBalance(int accountNum)
        {
            if (accountNum == 12345)
                return 35870;
            else if (accountNum == 12346)
                return 230;
            else
                return 0;
        }
    }
}
