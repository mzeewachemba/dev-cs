using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InheritenceApp
{
    internal class Cylinder:VolumeShape
    {
        //public double Radius { get; set; }
        public double Height { get; set; }
        public override double ComputeVolume()
        {
            return Math.PI * Radius * Radius *Height ;
        }
    }
}
