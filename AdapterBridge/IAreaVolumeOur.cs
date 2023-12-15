using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterBridge
{
    internal interface IAreaVolumeOur
    {
        double ComputeCircleArea(double radius);
        double ComputeSphereVolume(double radius);
        double ComputeCylinderVolume(double radius, double length);
    }
}
