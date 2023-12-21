using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{
    internal class ExistingAdaptee //Existing class's existing made available via the interface
    {
        //overaloaded methods
        public double ComputeAvg(float a, float b, float c)
        {
            double sum = (a + b + c);
            return sum / 3.0;
        }
        public double ComputeAvg(float a, float b, float c, float d)
        {
            double sum = (a + b + c + d);
            return sum / 4.0;
        }
        public double FindMin(float a, float b, float c)
        {
            double min = a;
            if (b < min)
                min = b;
            if (c < min)
                min = c;
            return min;
        }
        public double FindMin(float a, float b, float c, float d)
        {
            double min = a;
            if (b < min)
                min = b;
            if (c < min)
                min = c;
            if (d < min)
                min = d;
            return min;
        }
    }
}
