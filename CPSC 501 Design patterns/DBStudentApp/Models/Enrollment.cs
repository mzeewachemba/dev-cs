using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DBStudentApp.Models
{
    internal class Enrollment
    {
        public int StuedntId { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public int Credits { get; set; }
    }
}
