using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    internal class VacationVisitor : IVisitor
    {
        #region IVisitor Members
        public void Visit(Element element)
        {
            Employee e1 = element as Employee;
            e1.VacationDays += 2; //adding behavior to vacation days
        }
        #endregion
    }
}
