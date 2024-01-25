using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BridgePattern
{
    internal class RefinedAbstraction : Abstraction //adds more methods without affecting the implementation to the abstraction
    {
        public RefinedAbstraction(IBridge br) : base(br)
        {
        }

        public string OperationGreetTime(string nm)
        {
            return "RefinedAbstraction:" + bridge.AnotherOperationImp(nm) + ":" +
                   " Time of call = " + DateTime.Now.ToString();
        }

    }
}
