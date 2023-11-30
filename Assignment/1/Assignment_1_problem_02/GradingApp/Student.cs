using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GradingApp
{
    abstract class Student // base or parent class for different student types
    {
        public Student(int id, string fname, string lname, int test1, int test2)
        { // constructor
            this.ID = id;
            this.FirstName = fname;
            this.LastName = lname;
            this.Test1 = test1;
            this.Test2 = test2;
        }
        public int ID { get; set; }
        public string FirstName { get; set; } = string.Empty;
        public string LastName { get; set; } = String.Empty;
        public int Test1 { get; set; }
        public int Test2 { get; set; }
        public abstract string ComputeGrade(); // abstract method-derived class will provide the code
    }
}
