using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{
    internal interface IMathTarget
    {
        double ComputeAvgNew(double[] Arr);
        int ComputeAvgRound(double[] Arr);
        double FindMinNew(double[] Arr);
    }
}
