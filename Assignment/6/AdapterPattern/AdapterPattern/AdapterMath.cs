using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterPattern
{   //adapter class itself
    //wrapper class for adaptee , implements INewMath ,s to use the existing code, but provide a new interface to it
    internal class AdapterMath : ExistingAdaptee, INewMath 
    {
        public double ComputeAvgNew(double[] Arr)
        {
            if (Arr.Length == 3)
                return ComputeAvg((float)Arr[0], (float)Arr[1],
               (float)Arr[2]);
            else if (Arr.Length == 4)
                return ComputeAvg((float)Arr[0], (float)Arr[1],
               (float)Arr[2], (float)Arr[3]);
            else
                throw new Exception("Array size is not currently supported for ComputeAvg");
        }

        public double FindMinNew(double[] Arr)
        {
            // exercise – Implementing findmin
            //throw new NotImplementedException();
            if (Arr.Length == 3)
                return FindMin((float)Arr[0], (float)Arr[1],(float)Arr[2]);
            else if (Arr.Length == 4)
                return FindMin((float)Arr[0], (float)Arr[1],(float)Arr[2], (float)Arr[3]);
            else
                throw new Exception("Array size is not currently supported for FindMin");
        }
        //implementing additional behavior rounding up
        public int ComputeAvgRound(double[] Arr)
        {
            if (Arr.Length == 3)
                return (int)Math.Round(ComputeAvg((float)Arr[0], (float)Arr[1], (float)Arr[2]));
            else if (Arr.Length == 4)
                return (int)Math.Round(ComputeAvg((float)Arr[0], (float)Arr[1], (float)Arr[2], (float)Arr[3]));
            else
                throw new Exception("Array size is not currently supported for ComputeAvg");
        }

    }
}
