using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BridgePattern
{
    internal class ImplementationA : IBridge
    {
        //implementing Ibridge
        public string OperationImp()
        {
            return "result from ImplementationA operation";
        }
        public string AnotherOperationImp(string msg)
        {
            return "Greetings " + msg;
        }
    }
}
