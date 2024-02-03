using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal interface IComputeNew
    {
        double ComputeAvg(double[] data);
        double FindMin(int[] data);
    }
}
