using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    //base class to allow visitors
    abstract class Element
    {
        public abstract void Accept(IVisitor visitor);
    }
}
