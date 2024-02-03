using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecoratorPattern
{
    //class with improvements
    abstract class Decorator : IComponent //abstract to allow implementation by decorators
    {
        //aggregating IComponent
        protected IComponent icmp = null;
        public Decorator(IComponent cmp)
        {
            icmp = cmp;
        }
        //abstract because we dont know the implementation, will be done by concrete decorators
        abstract public string Welcome();
        abstract public string Welcome(string name);
    }
}
