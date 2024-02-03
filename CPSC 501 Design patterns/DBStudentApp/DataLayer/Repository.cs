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
        //private DataTable dt;

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
            List<Enrollment> eList = new List<Enrollment>();
            try
            {
                string sql = "SELECT s.StudentId, s.FirstName, s.LastName, c.Credits " +
                             "FROM Students s " +
                             "JOIN Enrollments e ON s.StudentId = e.StudentId " +
                             "JOIN Courses c ON e.CourseNum = c.CourseNum " +
                             "WHERE c.CourseNum = '" + courseNum + "'"; ;

                DataTable dt = _idac.GetManyRowsCols(sql); //datatable is mainly for repository class

                foreach (DataRow dr in dt.Rows)
                {
                    Enrollment e = new Enrollment();
                    e.StuedntId = (int)dr["StudentId"];
                    e.FirstName = (string)dr["FirstName"];
                    e.LastName = (string)dr["LastName"];
                    e.Credits = (int)dr["Credits"];

                    eList.Add(e);
                }
            }
            catch (Exception ex) { throw; }
            return eList;
            
        }
    }
}
