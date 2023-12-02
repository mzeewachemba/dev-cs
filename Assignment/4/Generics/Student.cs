using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics
{
    internal class Student : IComparable
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public int Id { get; set; }
        public int Test1Score { get; set; }
        public int Test2Score { get; set; }

        public int CompareTo(object? obj)
        {
            int res = 0;
            Student st = null;
            if (obj is Student)
            {
                st = (Student)obj;
                res = this.Test1Score.CompareTo(st.Test1Score);
            }
            return res;
        }

        public override string ToString()
        {
            return FirstName + " " +
            LastName + " " + Id.ToString() +
            " " + Test1Score.ToString() +
           " " + Test2Score.ToString();
        }

    }
}
