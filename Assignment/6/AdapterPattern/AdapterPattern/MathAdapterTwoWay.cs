using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{   //implementing both interfaces for compatibility of old methods and new methods
    internal class MathAdapterTwoWay : INewMath,IExistingMath
    {
        ExistingAdaptee ema = new ExistingAdaptee();
        ExistingMathAdapteeDerived emad = new ExistingMathAdapteeDerived();
        //existing methods
        public double ComputeAvg(float a, float b, float c)
        {
            return ema.ComputeAvg(a, b, c);
        }

        public double ComputeAvg(float a, float b, float c, float d)
        {
            return ema.FindMin(a, b, c, d);
        }

        public double FindMin(float a, float b, float c)
        {
            return ema.FindMin(a, b, c);
        }

        public double FindMin(float a, float b, float c, float d)
        {
            return ema.FindMin(a, b, c, d);
        }
        //new methods
        public double ComputeAvgNew(double[] Arr)
        {
            if (Arr.Length == 3)
                return ema.ComputeAvg((float)Arr[0], (float)Arr[1], (float)Arr[2]);
            else if (Arr.Length == 4)
                return ema.ComputeAvg((float)Arr[0], (float)Arr[1], (float)Arr[2], (float)Arr[3]);
            else
                throw new Exception("Array size is not currently supported for ComputeAvg");
        }

        public int ComputeAvgRound(double[] Arr)
        {
            if (Arr.Length == 3)
                return (int)Math.Round(ema.ComputeAvg((float)Arr[0], (float)Arr[1], (float)Arr[2]));
            else if (Arr.Length == 4)
                return (int)Math.Round(ema.ComputeAvg((float)Arr[0], (float)Arr[1], (float)Arr[2], (float)Arr[3]));
            else
                throw new Exception("Array size is not currently supported for ComputeAvg");
        }

        public double FindMinNew(double[] Arr)
        {
            // implementing findmin while reusing the code
            if (Arr.Length == 3)
                return ema.FindMin((float)Arr[0], (float)Arr[1], (float)Arr[2]);
            else if (Arr.Length == 4)
                return ema.FindMin((float)Arr[0], (float)Arr[1], (float)Arr[2], (float)Arr[3]);
            else
                throw new Exception("Array size is not currently supported for FindMin");
        }
        //Iexisting meth derived execution while reusing the code
        public double FindMax(double[] Arr)
        {
            if (Arr.Length == 3)
                return emad.FindMax((float)Arr[0], (float)Arr[1], (float)Arr[2]);
            else
                throw new Exception("Array size > 3 not supported");
        }
    }
}
