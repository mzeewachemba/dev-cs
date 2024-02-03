using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace OOPConcepts
{
    internal class Student
    {
        //non parameterized 
        //public Student() { }
        //constructor, to initialize an class as its being created
        //public Student(int Id, string Name , int Test1, int Test2) {
        //    this.Id = Id;
        //    this.Name = Name;
        //    this.Test1 = Test1;
        //    this.Test2 = Test2;
        //}
        public int Id { get; set; }
        public string Name { get; set; }
        public int Test1 { get; set; }
        public int Test2 { get; set; }
    }
}
