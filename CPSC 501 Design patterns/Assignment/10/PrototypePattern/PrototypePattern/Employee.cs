using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace PrototypePattern
{
    [Serializable]
    class Employee : ProtoTypeBase<Employee>
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Branch { get; set; }
        public int EmployeeId { get; set; }
        public Address Addr { get; set; }
    }
}
