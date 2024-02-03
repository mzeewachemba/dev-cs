using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{
    internal interface IExistingMath
    {
        double ComputeAvg(float a, float b, float c);
        double ComputeAvg(float a, float b, float c, float d);
        double FindMin(float a, float b, float c);
        double FindMin(float a, float b, float c, float d);
    }
}
