using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{
    internal class ExistingMathAdapteeDerived : ExistingAdaptee
    {
        public float FindMax(float a, float b, float c)
        {
            float max = a;
            if (b > max)
                max = b;
            if (c > max)
                max = c;
            return max;
        }
    }
}
