using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatternsConcepts
{
    internal class Student
    {
        public Student(Address addr1)
        {
            //to initialize memory for address  #COMPOSITION
            //this.Addr = new Address();
            this.Addr = addr1; // #AGREGATION
        }
        public int Id { get; set; }
        public string Name { get; set; }
        public int Test1 { get; set; }
        public int Test2 { get; set; }
        //public Address Addr { get; set; } = new Address();  one way of writting it or use the constructor
        public Address Addr { get; set; }
    }
}
