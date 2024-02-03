using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyPattern
{
    internal class QuickSortStrategy : IStrategySort<Student>
    {
        public void DoSort(List<Student> TList)
        {
            TList.Sort(); // Quick sort from .Net library
        }
    }
}
