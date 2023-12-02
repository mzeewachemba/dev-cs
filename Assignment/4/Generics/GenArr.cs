using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics
{
    internal class GenArr<T>
    {
        public static T FindMax<T>(T[] Arr)
            where T : IComparable<T>
        {
            T max = Arr[0];
            if (Arr[1].CompareTo(max) == 1)
                max = Arr[1];
            return max;
        }
        public static T[] InitArray<T>(int size)
            where T : new()//this line indicates that T has to be created with a new keyword
        {
            T[] Arr = new T[size];
            for (int i = 0; i < size; i++)
                Arr[i] = new T();
            return Arr;
        }
    }
}
