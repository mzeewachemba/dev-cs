using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;
using static System.Net.Mime.MediaTypeNames;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Abstraction
{
    internal class Student : ICloneable, IComparable<Student>
    {
        //constructors
        public Student() { }

        public Student(string fnm, string lnm, int id) 
        {
            Fname = fnm;
            Lname = lnm;
            Id = id;
        }
        //constructor overloading
        public Student(string fnm, string lnm, int id, int test1, int test2) 
        {
            Fname = fnm;
            Lname = lnm;
            Id = id;
            TestScores[0] = test1;
            TestScores[1] = test2;
        }
        //class attributes
        public int[] TestScores { get; set; } = new int[2]; //fixing to 2 items
        protected string Fname { get; set; }
        protected string Lname { get; set; }
        public int Id { get; set; }
        public Address Addr { get; set; } = new Address();

        public override string ToString()
        {
            return "Fname=" + Fname +
            " Lname=" + Lname + " ID=" + Id.ToString() +
            " Test1=" + TestScores[0].ToString() + " Test2=" +
            TestScores[1].ToString() + "\n" + Addr.Street + "," + Addr.City;
        }

        public virtual string GetGrade()
        {
            string grade = "";
            double avg = 0.4 * TestScores[0] + 0.6 * TestScores[1];
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
        //clone method implementation from IClonable
        public object Clone()
        {
            Student snew = new Student();
            snew = (Student)this.MemberwiseClone(); //implementing memberwise clone
            //memberwise clone present in every class as they extend from object class but the array and address for test score will point to the same memory
            //to solve that have totally independent memories for each object since array is a referance type as below
            
            snew.TestScores = (int[])this.TestScores.Clone(); //memberwise clone produces a shallow copy , for reference types call the clone method on the field itself 
            snew.Addr = (Address)this.Addr.Clone();
            return snew;
        }
        //compareto method implementation from IComparable
        public int CompareTo(Student? other)
        {
            int retVal = 0;
            if (other != null)
                //comparing by ID and Last Name
                //retVal = this.Id.CompareTo(other.Id);
                retVal = this.Lname.CompareTo(other.Lname);
            return retVal;
        }
    }
}
