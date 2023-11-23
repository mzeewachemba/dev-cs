using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestInterfaces
{
    internal interface ICompute
    {
        double ComputeArea(int  width, int height);
        double ComputeSphereVolume(double radius);
    }
}
