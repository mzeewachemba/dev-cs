using DBStudentApp.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DBStudentApp.DataLayer
{
    internal interface IRepository
    {
        List<Course> GetAllCourses();
        List<Enrollment> GetEnrollment(string courseNum);
    }
}
