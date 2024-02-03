using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyPattern
{
    internal class SortContext// abstraction for Strategy or Algorithm classes
    {
        IStrategySort<Student> istrat = null;
        //agregation to allow defining sorting algorithm
        public SortContext(IStrategySort<Student> ist)
        {
            istrat = ist;
        }
        // algorithm interface
        public void DoSort(List<Student> TList)
        {
            istrat.DoSort(TList);
        }
    }

}
