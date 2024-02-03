using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    internal class Employee2 : Element2
    {
        public Employee2(string nm, int hworked, double rate)
        {
            name = nm;
            hoursWorked = hworked;
            this.payRate = rate;
        }
        string name;
        public string Name
        {
            get { return name; }
            set { name = value; }
        }
        int hoursWorked;
        public int HoursWorked
        {
            get { return hoursWorked; }
            set { hoursWorked = value; }
        }
        double payRate;
        public double PayRate
        {
            get { return payRate; }
            set { payRate = value; }
        }
        public override T Accept<T>(IVisitor2<T> visitor)
        {
            return visitor.Visit(this);
        }
        public override string ToString()
        {
            return name + " : " + hoursWorked.ToString() + " : " +
            payRate.ToString();
        }
    }
}
