using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    static class OverTimeExtension
    {
        public static double ComputeOverTime(this Employee2 e2)
        {
            double overTimePay = 0;
            if (e2.HoursWorked > 40)
            {
                overTimePay = (e2.HoursWorked - 40) * 1.5 * e2.PayRate;
            }
            return overTimePay;
        }
    }
}
