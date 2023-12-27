using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{//class for different types of employees
    internal class Employee : Element
    {
        public Employee(string nm, int vacDays, double bonus)
        {
            name = nm;
            vacationDays = vacDays;
            this.bonus = bonus;
        }
        string name;
        public string Name
        {
            get { return name; }
            set { name = value; }
        }
        int vacationDays;
        public int VacationDays
        {
            get { return vacationDays; }
            set { vacationDays = value; }
        }
        double bonus;
        public double Bonus
        {
            get { return bonus; }
            set { bonus = value; }
        }
        public override void Accept(IVisitor visitor)
        {
            visitor.Visit(this);
        }
        public override string ToString()
        {
            return name + " : " + vacationDays.ToString() + " : " + bonus.ToString();
        }

    }
}
