using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryPattern
{
    internal class MyCompute : ICompute //retired version using 3.14
    {
        public double ComputeCylinderVolume(float radius, float height)
        {
            return 2 * 3.1415 * radius * height;
        }
        public double ComputeSphereVolume(float radius)
        {
            return 4 / 3.0 * 3.1415 * radius * radius * radius;
        }
    }
}
