using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterBridge
{
    internal interface IComputeAreaVolume
    {
        double GetCircleArea(double radius);
        double GetSphereVol(double radius);
        double GetCylinderVolume(double radius , double length);
    }
}
