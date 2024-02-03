using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FacadePattern
{
    internal class MortgageApplicant
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public int BankAccountNum { get; set; }
        public int LoanAccountNum { get; set; }
        public string SSNum { get; set; }
        public double LoanAmountAsked { get; set; }
    }
}
