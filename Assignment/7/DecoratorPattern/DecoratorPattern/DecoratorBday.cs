using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecoratorPattern
{
    //enhancements by day
    internal class DecoratorBday : Decorator
    {
        //aggregation
        public DecoratorBday(IComponent cmp) : base(cmp)
        {
        }
        public override string Welcome()
        {
            return icmp.Welcome() + "\nHappy Birthday ";
        }
        public override string Welcome(string name)
        {
            return icmp.Welcome(name) + "\nHappy Birthday";
        }
    }
}
