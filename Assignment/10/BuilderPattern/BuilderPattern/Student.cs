using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    internal class Student
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Major { get; set; }
        public int Test1 { get; set; }
        public int Test2 { get; set; }
        public string ComputeGrade()
        {
            string grade = "A";
            double avg = 0.4 * Test1 + 0.6 * Test2;
            if (avg > 90)
                grade = "A";
            else if (avg > 85)
                grade = "A-";
            else if (avg > 80)
                grade = "B+";
            else
                grade = "B";
            return grade;
        }
    }
}
