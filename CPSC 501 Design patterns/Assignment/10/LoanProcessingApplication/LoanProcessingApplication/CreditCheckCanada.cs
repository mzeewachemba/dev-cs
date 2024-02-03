using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;

namespace AbstractFactoryPattern
{//credit check implementation for canada
    internal class CreditCheckCanada : ICreditCheck
    {
        public int GetCreditScore(string firstName, string lastName)
        {
            // call Trans Union or other Canadian credit check services
            // A Canadian company's CREDIT INFO SCORE can range from 0-70,
            //details as follows;
            //C.I. Range: Risk Factor
            //0 - 11 Minimal
            //12 - 23 Average
            //24 - 35 Marginal
            //36 - 47 High
            //48 - 59 Very High
            //60 - 70 Poor
            int score = 0;
            if ((firstName.ToUpper() == "MARK") && (lastName.ToUpper() == "MATHEWS"))
                score = 32;
            if ((firstName.ToUpper() == "NANCY") && (lastName.ToUpper() == "ADAMS"))
                score = 8;
            return score;
        }
    }
}
