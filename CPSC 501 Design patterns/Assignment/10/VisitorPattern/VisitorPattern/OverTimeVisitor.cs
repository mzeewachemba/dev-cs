using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    class OverTimeVisitor : IVisitor2<float>
    {
        #region IVisitor2<float> Members
        public float Visit(Element2 element)
        {
            Employee2 emp2 = element as Employee2;
            float overTime = 0;
            if (emp2.HoursWorked > 40)
                overTime = (float)((emp2.HoursWorked - 40) * emp2.PayRate * 1.5);
            return overTime;
        }
        #endregion
    }
}
