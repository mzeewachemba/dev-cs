using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestInterfaces
{
    internal interface IComputePay
    {
        double ComputePay(double hoursWorked, double payrate);
    }
}
