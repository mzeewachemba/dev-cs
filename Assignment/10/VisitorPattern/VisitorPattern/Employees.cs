using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VisitorPattern
{
    //maintains list of employees and makes sure each employee accept a visitor
    internal class Employees
    {
        List<Employee> _EList = new List<Employee>();
        internal List<Employee> EList
        {
            get { return _EList; }
        }
        public void Add(Employee emp)
        {
            _EList.Add(emp);
        }
        public void Remove(Employee emp)
        {
            _EList.Remove(emp);
        }
        public void Accept(IVisitor visitor)
        {
            foreach (Employee em in _EList)
            {
                em.Accept(visitor);
            }
        }
    }
}
