using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    abstract class Element2
    {
        public abstract T Accept<T>(IVisitor2<T> visitor);
    }
}
