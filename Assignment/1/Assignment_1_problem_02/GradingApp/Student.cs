using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GradingApp
{
    abstract class Student //parent class
    {
        //public constructor
        public Student(int id, string fname, string lname, int test1, int test2)
        { 
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
        public abstract string ComputeGrade(); //to be implemented by child classes
    }
}
