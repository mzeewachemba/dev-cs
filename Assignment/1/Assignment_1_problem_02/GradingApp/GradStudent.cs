using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GradingApp
{
    internal class GradStudent : Student
    {
        //constructor initialization by a child class
        public GradStudent(int id, string fname, string lname, int test1, int test2) : base(id, fname, lname, test1, test2)
        {
        }

        public override string ComputeGrade()
        {
            throw new NotImplementedException();
        }
    }
}
