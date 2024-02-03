using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    internal class ComputePayVisitor : IVisitor2<double>
    {
        #region IVisitor2 Members
        public double Visit(Element2 element)
        {
            Employee2 emp2 = element as Employee2;
            return (emp2.HoursWorked * emp2.PayRate); //computing payrate
        }
        #endregion
    }
}
