using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal class Compute
    {
        public double ComputeAvg(double num1, double num2 ,double num3) 
        {
            double sum = num1 + num2 + num3;
            return sum/3.0;
        }

        public int FindMin(int a, int b ,int c) 
        {
            int min = a;
            if (b < min)
            {
                min = b;
            }
            if (c < min)
            {
                min = c;
            }
            return min;
        }
    }
}
