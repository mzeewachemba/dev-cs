using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;

namespace AdapterBridge
{
    internal class AdapterLibrary1 : IAreaVolumeOur
    {
        AreaVolLib1 av1 = new AreaVolLib1();
        public double ComputeCircleArea(double radius)
        {
            return av1.CircleArea(radius);
        }

        public double ComputeCylinderVolume(double radius, double length)
        {
            return av1.CylinderVolume(radius,length);
        }

        public double ComputeSphereVolume(double radius)
        {
            return av1.SphereVolume(radius);
        }
    }
}
