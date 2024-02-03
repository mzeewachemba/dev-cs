using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentApp
{
    //grad student extends student
    internal class GradStudent: Student
    {
        string Thesis {  get; set; }  = string.Empty;

        public string Greet() 
        {
            return "Welcome to graduate school";
        }

        //overriding
        public override string ComputeGrade()
        {
            string grade = " ";
            double avg = 0.5 * Test1 + 0.5 * Test2;

            if (avg > 90)
            {
                grade = "A";
            }
            else if (avg > 85)
            {
                grade = "A-";
            }
            else if (avg > 80)
            {
                grade = "B";
            }
            else
                grade = "C";
            return grade;
        }
    }
}
