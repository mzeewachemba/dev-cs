using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterBridge
{
    internal class AreaVolLib1
    {
        public double CircleArea(double radius)
        {
            return Math.PI * radius * radius;
        } 

        public double SphereVolume(double r) 
        {
            return Math.PI * 4 / 3.0 * r * r * r;
        }

        public double CylinderVolume(double r ,double length)
        {
            return 2 * Math.PI * r * length;
        }
    }
}
