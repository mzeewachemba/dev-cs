using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace VisitorPattern
{//generic interface 
    internal interface IVisitor2<T>
    {
        T Visit(Element2 element);
    }
}
