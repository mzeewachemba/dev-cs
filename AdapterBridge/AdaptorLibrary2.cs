using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterBridge
{
    internal class AdaptorLibrary2 : IAreaVolumeOur
    {
        IComputeAreaVolume av2 = new AreaVolumeLIbrary2();
        public double ComputeCircleArea(double radius)
        {
            return av2.GetCircleArea(radius);
        }

        public double ComputeCylinderVolume(double radius, double length)
        {
            return av2.GetCylinderVolume(radius,length);
        }

        public double ComputeSphereVolume(double radius)
        {
            return av2.GetSphereVol(radius);
        }
    }
}
