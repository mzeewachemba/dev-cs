using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestInterfaces
{
    internal class MyCompute : ICompute, IComputePay
    {

        public double ComputeArea(int width, int height)
        {
            return width * height;
        }

        public double ComputePay(double hoursWorked, double payrate)
        {
            return hoursWorked * payrate;
        }

        public double ComputeSphereVolume(double radius)
        {
            return 4/3*Math.PI*radius * radius * radius;
        }
    }
}
