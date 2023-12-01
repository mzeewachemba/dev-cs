using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Abstraction
{
    internal class AreaVolume : IAreaVolume
    {
        public double ComputeCircleArea(double radius)
        {
            return Math.PI * radius * radius;
        }

        public double ComputeRectangleArea(double length, double width)
        {
            return length * width;
        }

        public double ComputeSphereVolume(double radius)
        {
            return 4 / 3.0 * Math.PI * Math.Pow(radius, 3);
        }

        public double CylinderVolume(double radius, double length)
        {
            return 2 * Math.PI * radius * length;
        }
    }
}
