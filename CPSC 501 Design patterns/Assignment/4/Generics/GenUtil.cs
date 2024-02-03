using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics
{
    internal class GenUtil // Generic method
    {
        //public static void Exchange<T>(ref int a, ref int b)
        //{
        //    int temp = a;
        //    a = b;
        //    b = temp;
        //}

        //public static void Exchange<T>(ref double a, ref double b)
        //{
        //    double temp = a;
        //    a = b;
        //    b = temp;
        //}

        //public static void Exchange<T>(ref string a, ref string b)
        //{
        //    string temp = a;
        //    a = b;
        //    b = temp;
        //}
        

        //Generic method below solves a problem for line 11 to 30 ,copying different methods for different datatypes
        public static void Exchange<T>(ref T a, ref T b)
        {
            T temp = a;
            a = b;
            b = temp;
        }
    }
}
