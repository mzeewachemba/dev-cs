using DBStudentApp.Models;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace DBStudentApp.DataLayer
{
    internal class Repository : IRepository //compose sql and send it to datalayer
    {
        IDataAccess _idac = new DataAccess();

        public List<Course> GetAllCourses()
        {
            List<Course> CList = new List<Course>();
            try
            {
                string sql = "select * from Courses";
                DataTable dt = _idac.GetManyRowsCols(sql);
                Console.WriteLine("Retrieved dt is  " + dt);
                foreach(DataRow dr in dt.Rows)
                {
                    Course c = new Course();
                    c.CourseNum = (string)dr["CourseNum"];
                    c.CourseName = (string)dr["CourseName"];
                    CList.Add(c);
                }
            }
            catch(Exception ex){ throw; }
            return CList;
        }

        public List<Enrollment> GetEnrollment(string courseNum)
        {
            throw new NotImplementedException();
        }
    }
}
