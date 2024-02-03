using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace OOPConcepts
{
    internal static class MyExtension //all fn are static
    {
        public static double ComputeOverTimePay(this Employee emp,double overtimeRate)
        {
            double overtimePay = 0;
            if (emp.HoursWorked > 40) {
                var overtimeHours = emp.HoursWorked - 40;

                overtimePay = overtimeHours * overtimeRate * emp.PayRate;
            }

            return overtimePay;
        }
    }
}
