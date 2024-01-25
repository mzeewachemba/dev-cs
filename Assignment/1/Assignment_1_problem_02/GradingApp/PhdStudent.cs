using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GradingApp
{
    internal class PhdStudent : Student
    {
        public PhdStudent(int id, string fname, string lname, int test1, int test2 , string dissertetion , string advisor) : base(id, fname, lname, test1, test2)
        {
        }
        //additional variables for this class
        public string Dissertation { get; set; } 
        public string Advisor { get; set; }
        public override string ComputeGrade()
        {
            double avg = 0.4 * Test1 + 0.6 * Test2;
            string grade = "";
            if (avg > 95) 
                grade = "A";
            else if (avg > 90)
                grade = "A-";
            else if (avg > 87)
                grade = "B+";
            else if (avg > 80)
                grade = "B";
            else
                grade = "C";
            return grade;
        }
    }
}
