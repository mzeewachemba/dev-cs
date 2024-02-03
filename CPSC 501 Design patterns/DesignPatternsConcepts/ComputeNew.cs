using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal class ComputeNew : IComputeNew
    {
        //compsition ,creating one object of the compute class
        Compute compute = new Compute();
        public double ComputeAvg(double[] data)
        {
            if (data.Length != 3)
                throw new Exception("Input size other than 3 not supported");

            return compute.ComputeAvg(data[0], data[1], data[2]);
        }

        public double FindMin(int[] data)
        {
            if (data.Length != 3)
                throw new Exception("Input size other than 3 not supported");

            return compute.FindMin(data[0], data[1], data[2]);
        }
    }
}
