using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    internal class VicePresident : Employee
    {
        public VicePresident(string nm, int vacDays, double pay) : base(nm, vacDays, pay)
        {
        }
    }
}
