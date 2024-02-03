using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterBridge
{
    internal class AreaVolumeLIbrary2 : IComputeAreaVolume
    {
        public double GetCircleArea(double radius)
        {
            return Math.PI * radius * radius;
        }

        public double GetCylinderVolume(double radius, double length)
        {
            return 2 * Math.PI * radius * length;
        }

        public double GetSphereVol(double radius)
        {
            return Math.PI * 4 / 3.0 * radius * radius * radius;
        }
    }
}
