using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{
    internal interface INewMath //interface for existing code in the adaptee class, similar methods
    {
        double ComputeAvgNew(double[] Arr);
        //additional behaviour
        int ComputeAvgRound(double[] Arr);
        double FindMinNew(double[] Arr);
    }
}
