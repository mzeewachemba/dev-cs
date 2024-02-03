using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyPattern
{
    internal class ShellSortStrategy : IStrategySort<Student>
    {
        public void DoSort(List<Student> TList)
        { // Shell Sort
            int i, j, increment;
            Student temp;
            increment = 3;
            while (increment > 0)
            {
                for (i = 0; i < TList.Count; i++)
                {
                    j = i;
                    temp = TList[i];
                    while ((j >= increment) && (TList[j -
                   increment].CompareTo(temp) > 0))
                    {
                        TList[j] = TList[j - increment];
                        j = j - increment;
                    }
                    TList[j] = temp;
                }
                if (increment / 2 != 0)
                {
                    increment = increment / 2;
                }
                else if (increment == 1)
                {
                    increment = 0;
                }
                else
                {
                    increment = 1;
                }
            }
        }
    }
}
