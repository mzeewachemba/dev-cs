using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FactoryPattern
{
    internal interface ICompute
    {
        double ComputeCylinderVolume(float radius, float height);
        double ComputeSphereVolume(float radius);
    }
}
