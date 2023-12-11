using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal class ComputeFactory
    {
        public static IComputeArea CreateObject(ComputeCriteria criteria)
        {
            if (criteria == ComputeCriteria.FAST)
            {
                return new ComputeFast();
            }
            else if (criteria == ComputeCriteria.ACCURATE)
            {
                return new ComputeAccurate();
            }
            else
            {
                return null;
            }
        }
    }
}
