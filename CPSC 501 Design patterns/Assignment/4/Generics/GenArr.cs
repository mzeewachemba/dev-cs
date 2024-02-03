using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics
{
    internal class GenArr<T>
    {
        public static T FindMax<T>(T[] Arr) //find maximum for any object T
            where T : IComparable<T> //indicates that T has to implement IComparable
        {
            T max = Arr[0];
            if (Arr[1].CompareTo(max) == 1) //compareTo returns 1 when 1st no is greater than the second number
                max = Arr[1];
            return max;
        }
        public static T[] InitArray<T>(int size) //inintialize an array of any type T
            where T : new() //this line indicates that T has to be created with a new keyword
        {
            T[] Arr = new T[size];
            for (int i = 0; i < size; i++)
                Arr[i] = new T();
            return Arr;
        }
    }
}
