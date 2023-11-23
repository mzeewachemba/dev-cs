using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestInterfaces
{
    internal class Student : IComparable<Student>
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int  Test1 { get; set; }
        public int Test2 { get; set; }

        public int CompareTo(Student? other)
        {
            return this.Test1.CompareTo(other.Test2);
        }

        public override string ToString()
        {
            return Id.ToString() + " " + Test1.ToString() + " " + Test2.ToString();
        }
    }
}
