using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GraddingAppAssignment2
{
    abstract class Student : IComparable<Student> //parent class
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

        public int CompareTo(Student? other)
        {
            int retVal = 0;
            if (other != null)
                //comparing grades
                retVal = GetGradePoints(this.ComputeGrade()).CompareTo(GetGradePoints(other.ComputeGrade()));
            return retVal;
        }

        double GetGradePoints(string grade)
        {
            double points = 0;
            switch (grade)
            {
                //for A to stay at the stop, start with smaller value
                case "A":
                    points = 1;
                    break;
                case "A-":
                    points = 2;
                    break;
                case "B+":
                    points = 3;
                    break;
                case "B":
                    points = 4;
                    break;
                case "B-":
                    points = 5;
                    break;
                case "C+":
                    points = 6;
                    break;
                case "C":
                    points = 7;
                    break;
                default:
                    points = 10;
                    break;
            }
            return points;
        }


        public abstract string ComputeGrade(); //to be implemented by derivatives
    }
}
