using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InheritenceApp
{
    internal class Sphere:VolumeShape
    {
        public override double ComputeVolume()
        {
            return 4/3 * Math.PI * Radius * Radius;
        }
    }
}
