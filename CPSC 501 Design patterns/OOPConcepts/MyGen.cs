using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPConcepts
{
    //generic class
    internal class MyGen<T1,T2>
    {
        public T1 A {  get; set; }
        public T2 B { get; set; }

        public override string ToString()
        {
            return A.ToString() + "  " + B.ToString();
        }
    }
}
