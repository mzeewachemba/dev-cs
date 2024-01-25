using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DecoratorPattern
{
    //enhancements by time
    internal class DecoratorTime : Decorator
    {
        //aggregation
        public DecoratorTime(IComponent cmp) : base(cmp)
        {
        }
        public override string Welcome()
        {
            return icmp.Welcome() + "\nTime = " + DateTime.Now.ToString();//addding time component as well
        }
        public override string Welcome(string name)
        {
            return icmp.Welcome(name) + "\nTime = " + DateTime.Now.ToString();//addding time component as well
        }
    }
}
