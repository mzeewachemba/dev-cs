using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentApp
{
    internal class Student
    {
        public int Id { get; set; }
        public string FirstName { get; set; } = string.Empty;
        public string LastName { get; set; } = string.Empty;
        
        private int test1;
        public int Test1 
        {
            get { return test1; }
            set { if ((value < 0) || (value > 100))
                    throw new Exception("invalid test1 score");
            test1 = value;
            } 
        }
        public int Test2 { get; set; }

        public string ComputeGrade()
        {
            string grade = " ";
            double avg = 0.4*Test1 + 0.6*Test2;

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
