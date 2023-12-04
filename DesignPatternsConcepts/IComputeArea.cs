using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal interface IComputeArea
    {
        double ComputeReactangleArea(double width, double height);
        double ComputeCircleArea(double radius);
    }
}
