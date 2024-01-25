using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PrototypePattern
{//this class generate a copy of an employee with the default field already populated
    class EmployeeCopyManager : ProtoTypeBase<Employee>
    {
        Dictionary<String, Employee> DTable = new Dictionary<String,Employee>();
        public EmployeeCopyManager()
        {
            Address a1 = new Address
            {
                StreetAddress = "55 Pizza Lane",
                City = "Austin"
            };
            Employee e1 = new Employee();
            e1.FirstName = "";
            e1.LastName = "";
            e1.EmployeeId = 0;
            e1.Branch = "Austin";
            e1.Addr = a1;
            DTable.Add(e1.Branch, e1);
        }
        public Employee this[string bran] //creates a copy
        {
            get
            {
                return (DTable[bran]).Copy();
            }
        }
    }
}
