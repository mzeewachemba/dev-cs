using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics
{
    internal class MyGen<T1,T2>
    {
        T1 a;
        public T1 A
        {
            get { return a; }
            set { a = value; }
        }
        T2 b;
        public T2 B
        {
            get { return b; }
            set { b = value; }
        }
        public override string ToString()
        {
            return a.ToString() + " : " + b.ToString();
        }
    }
}
