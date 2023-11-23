using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InheritenceApp
{
    internal class Circle:Shape
    {
        public double ComputeArea()
        {
            return Math.PI * Radius * Radius;
        }
    }
}
