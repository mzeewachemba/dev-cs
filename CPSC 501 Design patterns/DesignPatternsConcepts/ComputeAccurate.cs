using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal class ComputeAccurate : IComputeArea
    {
        public double ComputeCircleArea(double radius)
        {
            return Math.PI * radius * radius;
        }

        public double ComputeReactangleArea(double width, double height)
        {
            return width * height;
        }
    }
}
