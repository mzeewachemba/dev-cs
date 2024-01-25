using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{
    internal interface INewMath //interface that will extend existing code-additional behavior can be added here
    {
        double ComputeAvgNew(double[] Arr);
        //additional behaviour-below method
        int ComputeAvgRound(double[] Arr);
        double FindMinNew(double[] Arr);
    }
}
