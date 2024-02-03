using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterBridge
{
    internal class ComputeBridge : IAreaVolumeOur
    {
        IAreaVolumeOur _iav;
        public ComputeBridge(IAreaVolumeOur iav) { _iav = iav; }
        public double ComputeCircleArea(double radius)
        {
            return _iav.ComputeCircleArea(radius);
        }

        public double ComputeCylinderVolume(double radius, double length)
        {
            return _iav.ComputeCylinderVolume(radius,length);
        }

        public double ComputeSphereVolume(double radius)
        {
            return _iav.ComputeSphereVolume(radius);
        }
    }
}
