using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    internal class BonusVisitor : IVisitor
    {
        #region IVisitor Members
        public void Visit(Element element)
        {
            Employee emp = element as Employee;
            emp.Bonus = emp.Bonus * 1.10;
        }
        #endregion
    }
}
