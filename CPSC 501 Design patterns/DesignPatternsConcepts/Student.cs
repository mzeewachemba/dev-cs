using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal class Student : ICloneable
    {
        public Student(Address addr1)
        {
            //to initialize memory for address  #COMPOSITION
            //this.Addr = new Address();
            this.Addr = addr1; // #AGREGATION
        }
        public int Id { get; set; }
        public string Name { get; set; }
        public int test1;
        public int Test1 
        {
            get {return test1;}
            set {if (value > 100)
                throw new Exception("Invalid data for Test1");
            else
                    test1 = value;
            } 
        }
        public int Test2 { get; set; }
        //public Address Addr { get; set; } = new Address();  one way of writting it or use the constructor
        public Address Addr { get; set; }

        public object Clone()
        {
            //return this.MemberwiseClone(); //shallow copy, because if inside you have another class it wont create memory for that class
            Student s2 = (Student) this.MemberwiseClone();
            s2.Addr = (Address)this.Addr.Clone();
            return s2;
        }
    }
}
