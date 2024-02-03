using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal class ComputeFast : IComputeArea
    {
        public double ComputeCircleArea(double radius)
        {
            return 3.14 * radius * radius;
        }

        public double ComputeReactangleArea(double width, double height)
        {
            return width * height;
        }
    }
}
