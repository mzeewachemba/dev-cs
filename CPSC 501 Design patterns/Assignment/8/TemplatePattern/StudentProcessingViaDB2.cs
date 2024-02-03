using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TemplatePattern
{
    //read from DB
    internal class StudentProcessingViaDB2 : TemplateStudent
    {
        //combining strategy and template for plugability
        IGradeStrategy igradeStrategy; // flexible grade strategy 
        public StudentProcessingViaDB2(IGradeStrategy igr) 
        {
            igradeStrategy = igr;
        }
        public override void ReadStudents()
        {
            string sql = "select * from Students";
            DataTable dt = DataAccess.GetDataTable(sql);
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                Student s1 = new Student();
                s1.FirstName = dt.Rows[i]["FirstName"].ToString();
                s1.LastName = dt.Rows[i]["LastName"].ToString();
                s1.Id = int.Parse(dt.Rows[i]["Id"].ToString());
                s1.Test1Score =
               int.Parse(dt.Rows[i]["Test1Score"].ToString());
                s1.Test2Score =
               int.Parse(dt.Rows[i]["Test2Score"].ToString());
                _STList.Add(s1);
            }
        }
        public override void AssignGrades()
        {
            foreach (Student st in _STList)
            {
                //allowing flexibility
                st.Grade = igradeStrategy.ComputeGrade(st);
            }
        }
        public override void SortStudents()
        {
            // depends on db arangements
        }
        public override void StoreStudents()
        {
            foreach (Student st in _STList)
            {
                string sql = "Update Students set " +
                "FirstName='" + st.FirstName + "'," +
                "Lastname='" + st.LastName + "'," +
                "Test1Score=" + st.Test1Score + "," +
                "Test2Score=" + st.Test2Score + "," +
                "Grade='" + st.Grade + "' where Id=" + st.Id.ToString();
                DataAccess.InsertOrUpdateOrDelete(sql);
            }
        }
    }
}
