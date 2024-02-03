using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractFactoryPattern
{//implementation of credit check for the us
    internal class CreditCheckUS : ICreditCheck
    {
        public int GetCreditScore(string firstName, string lastName)
        {
            // call Equifax, Transunion etc.. services
            int score = 0;
            if ((firstName.ToUpper() == "BILL") && (lastName.ToUpper() == "BAKER"))
                score = 630;
            if ((firstName.ToUpper() == "SALLY") && (lastName.ToUpper() == "SIMPSON"))
                score = 720;
            return score;
        }
    }
}
