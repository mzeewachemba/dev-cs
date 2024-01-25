using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ObserverPattern
{
    internal class ConcreteSubjectGoog : StockSubject //concrete publisher extending stocksubject
    {
        //extending stocksubject the publisher class to feed stock information
        //setup delegated to parent constructor
        public ConcreteSubjectGoog() : base(new StockInfo("Goog", 585))
        {
        }

    }
}
