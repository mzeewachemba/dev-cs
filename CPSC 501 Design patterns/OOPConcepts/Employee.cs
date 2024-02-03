using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPConcepts
{
    internal class Employee
    {
        public string Name { get; set; }

        public int Id {  get; set; }
        
        public double HoursWorked { get; set; }

        public double PayRate {  get; set; }

        public double ComputePay() {  
            return PayRate * HoursWorked; 
        }
    }
}
